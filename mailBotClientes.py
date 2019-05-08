
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

def sendClientMailsDeptos():
    sql = "select duenos.mail,portalinmobiliario.nombre,portalinmobiliario.link from duenos inner join portalinmobiliario where " \
          "duenos.idProp=portalinmobiliario.id2 and duenos.contactado IS NULL and " \
          "duenos.esDueno='si' and (portalinmobiliario.operacion='arriendo') and portalinmobiliario.tipo='departamento' and " \
          "portalinmobiliario.fechascrap>='"+str(yesterday)+"' and portalinmobiliario.fechapublicacion>'" + str(past) + "' and " \
          "(portalinmobiliario.link like '%santiago-metropolitana%' or " \
          "portalinmobiliario.link like '%providencia%' or " \
           "portalinmobiliario.link like '%las-condes%' or portalinmobiliario.link like '%vitacura%');"

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')

    cur = mariadb_connection.cursor()
    cur.execute(sql)
    lista = cur.fetchall()
    mariadb_connection.close()

    print("[" + str(datetime.now()) +"]Sending mails (dptos) to "+str(len(lista))+ " clients:")

    for i,l in enumerate(lista):

        to = str(l[0])
        nombreProp = str(l[1])

        #gratis
        mailer.sendMailGratis(to,nombreProp,gratis=False)
        checkClient(to,"0")

        time.sleep(random.randint(200,300))

def sendClientMailsCasas():
    sql = "select duenos.mail,portalinmobiliario.nombre,portalinmobiliario.link from duenos inner join portalinmobiliario where " \
          "duenos.idProp=portalinmobiliario.id2 and duenos.contactado IS NULL and " \
          "duenos.esDueno='si' and (portalinmobiliario.operacion='arriendo') and portalinmobiliario.tipo='casa' and " \
          "portalinmobiliario.fechascrap>='"+str(yesterday)+"' and portalinmobiliario.fechapublicacion>'" + str(past) + "' and " \
          "(portalinmobiliario.link like '%lo-barnechea%' or " \
          "portalinmobiliario.link like '%vitacuraa%' or " \
           "portalinmobiliario.link like '%las-condes%' or portalinmobiliario.link like '%la-reina%');"

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')

    cur = mariadb_connection.cursor()
    cur.execute(sql)
    lista = cur.fetchall()
    mariadb_connection.close()

    print("[" + str(datetime.now()) +"]Sending mails (casas) to "+str(len(lista))+ " clients:")

    for i,l in enumerate(lista):
        to = str(l[0])
        nombreProp = str(l[1])

        mailer.sendMailGratis(to,nombreProp,gratis=False)
        checkClient(to,"0")

        time.sleep(random.randint(200,300))
		
sendClientMailsDeptos()
sendClientMailsCasas()
hasSendDailyMails = True

while True:
    if hasSendDailyMails and datetime.now().hour == 13:
            hasSendDailyMails = False
    if not hasSendDailyMails and datetime.now().hour == 14:
            #mandar mails aca
            sendClientMailsDeptos()
            sendClientMailsCasas()
            hasSendDailyMails = True
    time.sleep(600)
