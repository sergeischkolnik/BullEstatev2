import sendmail as sm
import pymysql as mysql
from datetime import datetime, timedelta, date

reportar_a = ["sergei@bullestate.cl"]

tipos=["casa","comercial","departamento","parcela","oficina","industrial","agricola","terreno-en-construccion","bodega","estacionamiento"]
operaciones = ["venta","arriendo"]
yesterday = datetime.now() - timedelta(days=10)
yesterday=datetime.date(yesterday)

def main():
    for tipo in tipos:
        for operacion in operaciones:
            sql = "SELECT COUNT('id') from portalinmobiliario where tipo='"+str(tipo)+"' and operacion='"+operacion+"' and fechascrap>='"+str(yesterday)+"'"
            mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
            cur = mariadb_connection.cursor()
            cur.execute(sql)
            elem = cur.fetchall()
            print(tipo+","+operacion+"->"+str(elem))

if __name__ == "__main__":
    while(True):
        main()