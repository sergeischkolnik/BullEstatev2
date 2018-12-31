import psycopg2
from datetime import datetime, timedelta
import csvWriter as w


limiteFechaPublicacion = 6
columnNames=["Id","Precio","Sup. util","Sup. total","Dormitorios","Baños","Rentabilidad","Link"]

pubLimit = (datetime.now() - timedelta(limiteFechaPublicacion)).strftime('%Y-%m-%d')
yesterday = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
today = datetime.today().strftime('%Y-%m-%d')

sqlFechaU = "(\"fecha ultima\" >= '" + yesterday + "' and \"fecha ultima\" <= '" + today + "')"
sqlFechaP = "\"fecha publicacion\" >= '" + pubLimit + "'"

try:
    conn = psycopg2.connect(database="bullestate", user="supersergei", password="sergei", port=5432)
except:
    print("I am unable to connect to the database.")

cur = conn.cursor()

sql = "SELECT * FROM clientes WHERE activo=1"
cur.execute(sql)
clientes = cur.fetchall()

for cliente in clientes:
    nombreArchivo = cliente[1] + " " + today

    sqlSelect = "propiedades.id,precio,\"metros min\",\"metros max\",dormitorios,banos, rentabilidades.rentabilidad, link"
    sqlWhere = " " + sqlFechaU + " and " + sqlFechaP
    sql = "SELECT " + sqlSelect +  " FROM propiedades INNER JOIN rentabilidades ON propiedades.id=rentabilidades.prop " \
                                   "INNER JOIN cliente_propiedades ON cliente_propiedades.propiedad=propiedades.id " \
                                   "WHERE cliente_propiedades.invalido=0 AND cliente_propiedades.cliente=" + \
          str(cliente[0]) + " AND " + sqlWhere

    cur.execute(sql)
    propiedades = cur.fetchall()
    if len(propiedades)>0:
        #crear excel
        w.writeCsv(nombreArchivo + " props.csv",[columnNames] + propiedades)