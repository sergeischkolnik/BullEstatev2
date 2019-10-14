import contactadorPortalMercadoLibre
import pymysql as mysql
from datetime import datetime, timedelta

def getPropiedades(op,tipo,comuna):
    past = datetime.now() - timedelta(days=120)
    sql="SELECT * FROM portalinmobiliario WHERE fechascrap>='" + str(past) + "' and operacion='" + str(op) + \
        "' and tipo='" + str(tipo) + "' and link LIKE '%" + str(comuna) + "%' and id2 NOT IN (Select idProp from ofertador)"


    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    props = cur.fetchall()
    mariadb_connection.close()
    return props

def main(op,tipo,comuna,rentmin):
    getPropiedades(op,tipo,comuna)

if __name__ == "__main__":
    main()
