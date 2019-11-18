import sendmail as sm
import pymysql as mysql
from datetime import datetime, timedelta
import time

reportar_a = ["demian@bullestate.cl"]

tipos=["casa","departamento","otro"]
operaciones = ["venta","arriendo"]
regiones = ["metropolitana","valparaiso","otra"]
yesterday = datetime.now() - timedelta(days=1)
yesterday=datetime.date(yesterday)



def main():
    text = ""
    for tipo in tipos:
        for operacion in operaciones:
            for region in regiones:
                sql = "SELECT COUNT('id') from portalinmobiliario where "

                if tipo != "otros":
                    sql += "tipo='"+str(tipo)+"' and "
                else:
                    sql += "tipo!='departamento' and tipo!='casa' and "


                sql += "operacion='"+operacion+"' and "

                sql += "fechascrap>='"+str(yesterday)+"' and "

                if region != "otra":
                    sql += "region='"+str(region)+"'"
                else:
                    sql += "region!='metropolitana' and region!='valparaiso'"

                mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
                cur = mariadb_connection.cursor()
                cur.execute(sql)
                elem = cur.fetchall()
                text += tipo+","+operacion+","+region+"->"+str(elem[0][0])+"\n"

    for p in reportar_a:
        sm.sendMailText2(to=p,subject="informe scrapers "+str(datetime.now()),text=text)
        time.sleep(60)
    print("listo")

if __name__ == "__main__":
    main()