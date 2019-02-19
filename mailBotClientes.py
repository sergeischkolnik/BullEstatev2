
import pymysql as mysql
from datetime import datetime, timedelta
import random
import sendMailVendetudepto as mailer
import time

past = datetime.now() - timedelta(days=30)
past=datetime.date(past)
yesterday = datetime.now() - timedelta(days=2)
yesterday=datetime.date(yesterday)

def checkClient(clientMail,comision):
    sql = "UPDATE duenos SET contactado='si',comision='"+str(comision)+"' WHERE mail='"+str(clientMail)+"'"
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    mariadb_connection.commit()
    mariadb_connection.close()

def sendClientMails():
    sql = "select duenos.mail,portalinmobiliario.nombre from duenos inner join portalinmobiliario where " \
          "duenos.idProp=portalinmobiliario.id2 and duenos.contactado IS NULL and " \
          "duenos.esDueno='si' and portalinmobiliario.operacion='venta' and portalinmobiliario.tipo='departamento' and " \
          "portalinmobiliario.fechascrap>'"+str(yesterday)+"' and portalinmobiliario.fechapublicacion>'" + str(past) + "' and " \
          "(portalinmobiliario.link like '%santiago-metropolitana%' or portalinmobiliario.link like '%lo-barnechea%' or " \
          "portalinmobiliario.link like '%vitacuraa%' or portalinmobiliario.link like '%providencia%' or " \
           "portalinmobiliario.link like '%las-condes%' or portalinmobiliario.link like '%nunoa%');"

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')

    cur = mariadb_connection.cursor()
    cur.execute(sql)
    lista = cur.fetchall()
    mariadb_connection.close()

    print("[" + str(datetime.now()) +"]Sending mails to "+str(len(lista))+ " clients:")
    for i,l in enumerate(lista):
        to = str(l[0])
        nombreProp = str(l[1])

        r = random.randint(1, 2)
        if r == 1:
            #gratis
            mailer.sendMailGratis(to,nombreProp,gratis=True)
            checkClient(to,"0")
        elif r == 2:
            #0.5%
            mailer.sendMailGratis(to,nombreProp,gratis=False)
            checkClient(to,"0.5")

        time.sleep(random.randint(200,300))
		
sendClientMails()
hasSendDailyMails = True

while True:
    if hasSendDailyMails and datetime.now().hour == 10:
            hasSendDailyMails = False
    if not hasSendDailyMails and datetime.now().hour == 11:
            #mandar mails aca
            sendClientMails()
            hasSendDailyMails = True
    time.sleep(600)