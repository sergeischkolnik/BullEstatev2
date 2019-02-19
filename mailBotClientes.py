
import pymysql as mysql
from datetime import datetime, timedelta

past = datetime.now() - timedelta(days=30)
past=datetime.date(past)
yesterday = datetime.now() - timedelta(days=1)
yesterday=datetime.date(yesterday)

print(yesterday)


def sendClientMails():
    sql = "select duenos.mail from duenos inner join portalinmobiliario where duenos.idProp=portalinmobiliario.id2 and " \
          "duenos.esDueno='si' and portalinmobiliario.operacion='venta' and portalinmobiliario.tipo='departamento' and " \
          "portalinmobiliario.fechascrap>'"+str(yesterday)+"' and portalinmobiliario.fechapublicacion>'" + str(past) + "' and " \
          "(portalinmobiliario.link like '%santiago-metropolitana%' or portalinmobiliario.link like '%lo-barnechea%' or " \
          "portalinmobiliario.link like '%vitacuraa%' or portalinmobiliario.link like '%providencia%' or " \
           "portalinmobiliario.link like '%las-condes%' or portalinmobiliario.link like '%nunoa%');"

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')

    cur = mariadb_connection.cursor()
    cur.execute(sql)

    print(sql)

    lista = cur.fetchall()
    for i,l in enumerate(lista):
        print(str(i)+". " + str(l))

    mariadb_connection.close()

sendClientMails()

hasSendDailyMails = False


while True:
    if hasSendDailyMails and datetime.now().hour == 10:
            hasSendDailyMails = False
    if not hasSendDailyMails and datetime.now().hour == 11:
            #mandar mails aca
            sendClientMails()
            hasSendDailyMails = True
