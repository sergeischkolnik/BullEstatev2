import pymysql as mysql
from datetime import datetime, timedelta
past = datetime.now() - timedelta(days=180)
past=datetime.date(past)
yesterday = datetime.now() - timedelta(days=10)
yesterday=datetime.date(yesterday)

def main():
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='yapo')
    cur = mariadb_connection.cursor()
    sql ='select id2,fechapublicacion,fechascrap,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,lat,lon,' \
         'estacionamientos,link from duenos inner join portalinmobiliario where ' \
    'duenos.idProp = portalinmobiliario.id2 and ' \
    'duenos.contactado is NULL and ' \
    'duenos.esDueno = "si" and ' \
    'region = "metropolitana" and ' \
    'tipo = "departamento" and ' \
    'fechascrap > "' + str(yesterday) + '"'
    cur.execute(sql)
    props = cur.fetchall()
    print(props)

if __name__ == "__main__":
    main()
