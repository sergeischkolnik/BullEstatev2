
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
          "((portalinmobiliario.link like '%santiago-metropolitana%' and (portalinmobiliario.dormitorios>'2' or portalinmobiliario.precio<'290000')) or " \
          "(portalinmobiliario.link like '%providencia%' and portalinmobiliario.dormitorios='1') or " \
          "(portalinmobiliario.link like '%las-condes%' and ((portalinmobiliario.dormitorios='1' and portalinmobiliario.precio<'450000') or (portalinmobiliario.dormitorios='2' and portalinmobiliario.precio<'550000') or (portalinmobiliario.dormitorios>'2') )) or "\
          "(portalinmobiliario.link like '%la-florida%' and ((portalinmobiliario.dormitorios='1' and portalinmobiliario.precio<'300000') or (portalinmobiliario.dormitorios='2' and portalinmobiliario.precio<'370000') or (portalinmobiliario.dormitorios>'2' and portalinmobiliario.banos>'1' and portalinmobiliario.precio<'420000'))) or "\
          "(portalinmobiliario.link like '%estacion-central%' and ((portalinmobiliario.dormitorios='1' and portalinmobiliario.precio<'280000') or (portalinmobiliario.dormitorios='2' and portalinmobiliario.precio<'330000') or (portalinmobiliario.dormitorios>'2' and portalinmobiliario.precio<'380000'))) or "\
          "(portalinmobiliario.link like '%independencia%' and ((portalinmobiliario.dormitorios='1' and portalinmobiliario.precio<'280000') or (portalinmobiliario.dormitorios='2' and portalinmobiliario.precio<'330000') or (portalinmobiliario.dormitorios>'2' and portalinmobiliario.precio<'380000'))) or "\
          "(portalinmobiliario.link like '%vitacura%') or (portalinmobiliario.link like '%lo-barnechea%' and portalinmobiliario.precio>'600000') or"\
          "(portalinmobiliario.link like '%nunoa%' and ((portalinmobiliario.dormitorios='1' and portalinmobiliario.precio<'430000') or portalinmobiliario.dormitorios>'1')) or "\
          "(portalinmobiliario.link like 'san-miguel' and ((portalinmobiliario.dormitorios='1' and portalinmobiliario.precio<'300000') or (portalinmobiliario.dormitorios>'1'))));"

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    print(sql)
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    lista = cur.fetchall()
    mariadb_connection.close()

    print("[" + str(datetime.now()) +"]Sending mails (dptos) to "+str(len(lista))+ " clients:")

    for i,l in enumerate(lista):

        to = str(l[0])
        nombreProp = str(l[1])
        linkProp=str(l[2])

        #gratis
        mailer.sendMailGratis(to,nombreProp,linkProp)
        checkClient(to,"1")

        time.sleep(random.randint(150,250))

def sendClientMailsCasas():
    sql = "select duenos.mail,portalinmobiliario.nombre,portalinmobiliario.link from duenos inner join portalinmobiliario where " \
          "duenos.idProp=portalinmobiliario.id2 and duenos.contactado IS NULL and " \
          "duenos.esDueno='si' and portalinmobiliario.precio>'500000' and (portalinmobiliario.operacion='arriendo') and portalinmobiliario.tipo='casa' and " \
          "portalinmobiliario.fechascrap>='"+str(yesterday)+"' and portalinmobiliario.fechapublicacion>'" + str(past) + "' and " \
          "(portalinmobiliario.link like '%lo-barnechea%' or " \
          "portalinmobiliario.link like '%vitacura%' or " \
          "portalinmobiliario.link like '%la-florida%' or " \
          "portalinmobiliario.link like '%providencia%' or " \
          "portalinmobiliario.link like '%nunoa%' or " \
          "(portalinmobiliario.link like '%colina%' and ((portalinmobiliario.lat<'-33.264536' and portalinmobiliario.lat>'-33.308362' and portalinmobiliario.lon<'-70.618245' and portalinmobiliario.lon>'-70.699193') or (portalinmobiliario.lat<'-33.301430' and portalinmobiliario.lat>'-33.335555' and portalinmobiliario.lon<'-70.622641' and portalinmobiliario.lon>'-70.666652'))) or " \
          "portalinmobiliario.link like '%maipu%' or " \
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
        linkProp=str(l[2])

        mailer.sendMailGratis(to,nombreProp,linkProp)
        checkClient(to,"1")

        time.sleep(random.randint(150,250))

def sendClientMailsOficinas():
    sql = "select duenos.mail,portalinmobiliario.nombre,portalinmobiliario.link from duenos inner join portalinmobiliario where " \
          "duenos.idProp=portalinmobiliario.id2 and duenos.contactado IS NULL and " \
          "duenos.esDueno='si' and (portalinmobiliario.operacion='arriendo') and (portalinmobiliario.tipo='oficina' or portalinmobiliario.tipo='comercial') and " \
          "portalinmobiliario.fechascrap>='"+str(yesterday)+"' and portalinmobiliario.fechapublicacion>'" + str(past) + "' and " \
          "(portalinmobiliario.link like '%santiago-metropolitana%' or " \
          "portalinmobiliario.link like '%lo-barnechea%' or " \
          "portalinmobiliario.link like '%vitacura%' or " \
          "(portalinmobiliario.link like '%huechuraba%' and ((portalinmobiliario.lat<'-33.374926' and portalinmobiliario.lat>'-33.396264' and portalinmobiliario.lon<'-70.603082' and portalinmobiliario.lon>'-70.630241'))) or " \
          "portalinmobiliario.link like '%nunoa%' or " \
          "portalinmobiliario.link like '%las-condes%' or portalinmobiliario.link like '%providencia%');"
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    lista = cur.fetchall()
    mariadb_connection.close()

    print("[" + str(datetime.now()) +"]Sending mails (oficinas) to "+str(len(lista))+ " clients:")

    for i,l in enumerate(lista):
        to = str(l[0])
        nombreProp = str(l[1])

        linkProp=str(l[2])

        mailer.sendMailGratis(to,nombreProp,linkProp)
        checkClient(to,"1")

        time.sleep(random.randint(150,250))

sendClientMailsDeptos()
sendClientMailsCasas()
sendClientMailsOficinas()
hasSendDailyMails = True

while True:
    if hasSendDailyMails and datetime.now().hour == 17:
            hasSendDailyMails = False
    if not hasSendDailyMails and datetime.now().hour == 22:
            #mandar mails aca
            sendClientMailsDeptos()
            sendClientMailsCasas()
            hasSendDailyMails = True
    time.sleep(600)
