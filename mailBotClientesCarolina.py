import threading
import pymysql as mysql
from datetime import datetime, timedelta
import random
import sendMailVendetudeptoCarolina as mailer
import sendMailVendetudeptoDaniela as mailerDaniela
import time

past = datetime.now() - timedelta(days=60)
past=datetime.date(past)
yesterday = datetime.now() - timedelta(days=2)
yesterday=datetime.date(yesterday)

sleepTime=random.randint(75,125)

sqlDeptosArriendo = "select duenos.mail,portalinmobiliario.nombre,portalinmobiliario.link from duenos inner join portalinmobiliario where " \
          "duenos.idProp=portalinmobiliario.id2 and duenos.contactado IS NULL and " \
          "duenos.esDueno='si' and (portalinmobiliario.operacion='arriendo') and portalinmobiliario.tipo='departamento' and " \
          "portalinmobiliario.fechascrap>='"+str(yesterday)+"' and portalinmobiliario.fechapublicacion>'" + str(past) + "' and " \
          "((portalinmobiliario.link like '%providencia%') or " \
          "(portalinmobiliario.link like '%huechuraba%' and ((portalinmobiliario.lat<'-33.374926' and portalinmobiliario.lat>'-33.396264' and portalinmobiliario.lon<'-70.603082' and portalinmobiliario.lon>'-70.630241'))) or " \
          "(portalinmobiliario.link like '%las-condes%' and ((portalinmobiliario.dormitorios='1') or (portalinmobiliario.dormitorios='2') or (portalinmobiliario.dormitorios>'2') )) or "\
          "(portalinmobiliario.link like '%vitacura%') or (portalinmobiliario.link like '%lo-barnechea%') or "\
          "(portalinmobiliario.link like '%nunoa%') or " \
          "(portalinmobiliario.link like '%santiago-metropolitana%') or " \
          "(portalinmobiliario.link like '%san-miguel%') or " \
          "(portalinmobiliario.link like '%estacion-central%') or " \
          "(portalinmobiliario.link like '%macul%') or " \
          "(portalinmobiliario.link like '%quinta-normall%') or " \
          "(portalinmobiliario.link like '%san-joaquin%') or " \
          "(portalinmobiliario.link like '%la-florida%') or " \
          "(portalinmobiliario.link like '%maipu%') or " \
          "(portalinmobiliario.link like '%la-cisterna%') or " \
          "(portalinmobiliario.link like '%recoleta%') or " \
          "(portalinmobiliario.link like '%independencia%'));"

sqlDeptosVenta = "select duenos.mail,portalinmobiliario.nombre,portalinmobiliario.link from duenos inner join portalinmobiliario where " \
          "duenos.idProp=portalinmobiliario.id2 and duenos.contactado IS NULL and portalinmobiliario.precio<'180000000' and " \
          "duenos.esDueno='si' and (portalinmobiliario.operacion='venta') and portalinmobiliario.tipo='departamento' and " \
          "portalinmobiliario.fechascrap>='"+str(yesterday)+"' and portalinmobiliario.fechapublicacion>'" + str(past) + "' and " \
          "((portalinmobiliario.link like '%providencia%') or " \
          "(portalinmobiliario.link like '%huechuraba%' and ((portalinmobiliario.lat<'-33.374926' and portalinmobiliario.lat>'-33.396264' and portalinmobiliario.lon<'-70.603082' and portalinmobiliario.lon>'-70.630241'))) or " \
          "(portalinmobiliario.link like '%las-condes%' and ((portalinmobiliario.dormitorios='1') or (portalinmobiliario.dormitorios='2') or (portalinmobiliario.dormitorios>'2') )) or "\
          "(portalinmobiliario.link like '%vitacura%') or (portalinmobiliario.link like '%reina%') or (portalinmobiliario.link like '%lo-barnechea%' and portalinmobiliario.precio>'80000000') or "\
          "(portalinmobiliario.link like '%nunoa%') or " \
          "(portalinmobiliario.link like '%santiago-metropolitana%') or " \
          "(portalinmobiliario.link like '%san-miguel%') or " \
          "(portalinmobiliario.link like '%estacion-central%') or " \
          "(portalinmobiliario.link like '%macul%') or " \
          "(portalinmobiliario.link like '%quinta-normall%') or " \
          "(portalinmobiliario.link like '%san-joaquin%') or " \
          "(portalinmobiliario.link like '%la-florida%') or " \
          "(portalinmobiliario.link like '%maipu%') or " \
          "(portalinmobiliario.link like '%la-cisterna%') or " \
          "(portalinmobiliario.link like '%recoleta%') or " \
          "(portalinmobiliario.link like '%independencia%'));"

sqlCasas = "select duenos.mail,portalinmobiliario.nombre,portalinmobiliario.link from duenos inner join portalinmobiliario where " \
      "duenos.idProp=portalinmobiliario.id2 and duenos.contactado IS NULL and portalinmobiliario.precio<'180000000' and " \
      "duenos.esDueno='si' and portalinmobiliario.precio>'400000' and (portalinmobiliario.operacion='arriendo' or portalinmobiliario.operacion='venta') and portalinmobiliario.tipo='casa' and " \
      "portalinmobiliario.fechascrap>='" + str(yesterday) + "' and portalinmobiliario.fechapublicacion>'" + str(
    past) + "' and " \
            "(portalinmobiliario.link like '%lo-barnechea%' or " \
            "portalinmobiliario.link like '%vitacura%' or " \
            "portalinmobiliario.link like '%la-florida%' or " \
            "portalinmobiliario.link like '%providencia%' or " \
            "portalinmobiliario.link like '%nunoa%' or " \
            "(portalinmobiliario.link like '%colina%' and ((portalinmobiliario.lat<'-33.264536' and portalinmobiliario.lat>'-33.470723' and portalinmobiliario.lon<'-70.618245' and portalinmobiliario.lon>'-70.699193') or (portalinmobiliario.lat<'-33.301430' and portalinmobiliario.lat>'-33.335555' and portalinmobiliario.lon<'-70.622641' and portalinmobiliario.lon>'-70.666652'))) or " \
            "(portalinmobiliario.link like '%pudahuel%' and ((portalinmobiliario.lat<'-33.438598' and portalinmobiliario.lat>'-33.308362' and portalinmobiliario.lon<'-70.817323' and portalinmobiliario.lon>'-70.868874') or (portalinmobiliario.lat<'-33.301430' and portalinmobiliario.lat>'-33.335555' and portalinmobiliario.lon<'-70.622641' and portalinmobiliario.lon>'-70.666652'))) or " \
            "portalinmobiliario.link like '%maipu%' or " \
            "portalinmobiliario.link like '%penalolen%' or " \
            "portalinmobiliario.link like '%las-condes%' or portalinmobiliario.link like '%la-reina%');"

sqlOficinas = "select duenos.mail,portalinmobiliario.nombre,portalinmobiliario.link from duenos inner join portalinmobiliario where " \
      "duenos.idProp=portalinmobiliario.id2 and duenos.contactado IS NULL and portalinmobiliario.precio<'180000000' and " \
      "duenos.esDueno='si' and (portalinmobiliario.operacion='arriendo' or portalinmobiliario.operacion='venta') and (portalinmobiliario.tipo='oficina' or portalinmobiliario.tipo='comercial') and " \
      "portalinmobiliario.fechascrap>='" + str(yesterday) + "' and portalinmobiliario.fechapublicacion>'" + str(
    past) + "' and " \
            "((portalinmobiliario.link like '%lo-barnechea%') or " \
            "(portalinmobiliario.link like '%vitacura%') or " \
            "(portalinmobiliario.link like '%huechuraba%' and ((portalinmobiliario.lat<'-33.374926' and portalinmobiliario.lat>'-33.396264' and portalinmobiliario.lon<'-70.603082' and portalinmobiliario.lon>'-70.630241'))) or " \
            "(portalinmobiliario.link like '%nunoa%') or " \
            "(portalinmobiliario.link like '%las-condes%' or portalinmobiliario.link like '%providencia%') or " \
            "(portalinmobiliario.link like '%santiago-metropolitana%') or " \
            "(portalinmobiliario.link like '%san-miguel%') or " \
            "(portalinmobiliario.link like '%estacion-central%') or " \
            "(portalinmobiliario.link like '%macul%') or " \
            "(portalinmobiliario.link like '%quinta-normall%') or " \
            "(portalinmobiliario.link like '%san-joaquin%') or " \
            "(portalinmobiliario.link like '%la-florida%') or " \
            "(portalinmobiliario.link like '%maipu%') or " \
            "(portalinmobiliario.link like '%recoleta%') or " \
            "(portalinmobiliario.link like '%independencia%'));"

sqlTerrenos = "select duenos.mail,portalinmobiliario.nombre,portalinmobiliario.link from duenos inner join portalinmobiliario where " \
      "duenos.idProp=portalinmobiliario.id2 and duenos.contactado IS NULL and portalinmobiliario.precio<'180000000' and " \
      "duenos.esDueno='si' and (portalinmobiliario.operacion='venta') and " \
      "(portalinmobiliario.tipo='sitio' or portalinmobiliario.tipo='loteo' or portalinmobiliario.tipo='industrial' or portalinmobiliario.tipo='agricola' or portalinmobiliario.tipo='parcela' or portalinmobiliario.tipo='terreno-en-construccion') and " \
      "portalinmobiliario.fechascrap>='" + str(yesterday) + "' and portalinmobiliario.fechapublicacion>'" + str(
    past) + "' and " \
            "(portalinmobiliario.link like '%lo-barnechea%' or " \
            "portalinmobiliario.link like '%vitacura%' or " \
            "(portalinmobiliario.link like '%huechuraba%' and ((portalinmobiliario.lat<'-33.374926' and portalinmobiliario.lat>'-33.396264' and portalinmobiliario.lon<'-70.603082' and portalinmobiliario.lon>'-70.630241'))) or " \
            "portalinmobiliario.link like '%nunoa%' or " \
            "portalinmobiliario.link like '%las-condes%' or portalinmobiliario.link like '%providencia%');"

def checkClient(clientMail,comision):
    sql = "UPDATE duenos SET contactado='si',comision='"+str(comision)+"' WHERE mail='"+str(clientMail)+"'"
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    mariadb_connection.commit()
    mariadb_connection.close()

def sendClientMailsDeptosArriendo():

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sqlDeptosArriendo)
    lista = cur.fetchall()
    mariadb_connection.close()

    print("[" + str(datetime.now()) +"]Sending mails (dptos arriendo) to "+str(len(lista))+ " clients:")
    carolina=True
    for i,l in enumerate(lista):

        to = str(l[0])
        nombreProp = str(l[1])
        linkProp=str(l[2])

        gratis=True
        if carolina:
            mailer.sendMailGratis(to,nombreProp,linkProp,gratis)
            carolina=False
        else:
            mailerDaniela.sendMailGratis(to,nombreProp,linkProp)
            carolina=True
        checkClient(to,"1")

        time.sleep(sleepTime)

def sendClientMailsDeptosVenta():

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sqlDeptosVenta)
    lista = cur.fetchall()
    mariadb_connection.close()

    print("[" + str(datetime.now()) +"]Sending mails (dptos venta) to "+str(len(lista))+ " clients:")
    carolina=True

    for i,l in enumerate(lista):

        to = str(l[0])
        nombreProp = str(l[1])
        linkProp=str(l[2])

        gratis=True
        if carolina:
            mailer.sendMailGratis(to,nombreProp,linkProp,gratis)
            carolina=False
        else:
            mailerDaniela.sendMailGratis(to,nombreProp,linkProp)
            carolina=True
        checkClient(to,"1")

        time.sleep(sleepTime)


def sendClientMailsCasas():

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sqlCasas)
    lista = cur.fetchall()
    mariadb_connection.close()

    print("[" + str(datetime.now()) +"]Sending mails (casas) to "+str(len(lista))+ " clients:")
    carolina=True

    for i,l in enumerate(lista):
        to = str(l[0])
        nombreProp = str(l[1])
        linkProp=str(l[2])
        gratis=True
        if carolina:
            mailer.sendMailGratis(to,nombreProp,linkProp,gratis)
            carolina=False
        else:
            mailerDaniela.sendMailGratis(to,nombreProp,linkProp)
            carolina=True
        checkClient(to,"1")

        time.sleep(sleepTime)

def sendClientMailsOficinas():


    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sqlOficinas)
    lista = cur.fetchall()
    mariadb_connection.close()

    print("[" + str(datetime.now()) +"]Sending mails (oficinas) to "+str(len(lista))+ " clients:")
    carolina=True

    for i,l in enumerate(lista):
        to = str(l[0])
        nombreProp = str(l[1])

        linkProp=str(l[2])
        gratis=True
        if carolina:
            mailer.sendMailGratis(to,nombreProp,linkProp,gratis)
            carolina=False
        else:
            mailerDaniela.sendMailGratis(to,nombreProp,linkProp)
            carolina=True
        checkClient(to,"1")

        time.sleep(sleepTime)

def sendClientMailsTerrenos():


    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sqlTerrenos)
    lista = cur.fetchall()
    mariadb_connection.close()

    print("[" + str(datetime.now()) +"]Sending mails (terrenos) to "+str(len(lista))+ " clients:")
    carolina=True

    for i,l in enumerate(lista):
        to = str(l[0])
        nombreProp = str(l[1])

        linkProp=str(l[2])
        gratis=True
        if carolina:
            mailer.sendMailGratis(to,nombreProp,linkProp,gratis)
            carolina=False
        else:
            mailerDaniela.sendMailGratis(to,nombreProp,linkProp)
            carolina=True
        checkClient(to,"1")

        time.sleep(sleepTime)

def threadSendMails():
    t = threading.currentThread()

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()

    cur.execute(sqlDeptos)
    listaDeptos = cur.fetchall()

    cur.execute(sqlCasas)
    listaCasas = cur.fetchall()

    cur.execute(sqlOficinas)
    listaOficinas = cur.fetchall()

    mariadb_connection.close()

    print("[mailbotFran][" + str(datetime.now()) + "]Sending mails (dptos) to " + str(len(listaDeptos)) + " clients:")
    for i,l in enumerate(listaDeptos):
        if not getattr(t, "do_run", True):
            print("[mailbotFran] Deteniendo mailer")
            return
        to = str(l[0])
        nombreProp = str(l[1])
        linkProp=str(l[2])

        #gratis
        mailer.sendMailGratis(to,nombreProp,linkProp)
        checkClient(to,"1")

        time.sleep(sleepTime)

    print("[mailbotFran][" + str(datetime.now()) +"]Sending mails (casas) to "+str(len(listaCasas))+ " clients:")

    for i,l in enumerate(listaCasas):
        if not getattr(t, "do_run", True):
            print("[mailbotFran] Deteniendo mailer")
            return
        to = str(l[0])
        nombreProp = str(l[1])
        linkProp=str(l[2])

        mailer.sendMailGratis(to,nombreProp,linkProp)
        checkClient(to,"1")

        time.sleep(sleepTime)

    print("[mailbotFran][" + str(datetime.now()) +"]Sending mails (oficinas) to "+str(len(listaOficinas))+ " clients:")

    for i,l in enumerate(listaOficinas):
        if not getattr(t, "do_run", True):
            print("[mailbotFran] Deteniendo mailer")
            return
        to = str(l[0])
        nombreProp = str(l[1])

        linkProp=str(l[2])

        mailer.sendMailGratis(to,nombreProp,linkProp)
        checkClient(to,"1")

        time.sleep(sleepTime)

def main():
    sendClientMailsDeptosArriendo()
    sendClientMailsDeptosVenta()
    sendClientMailsCasas()
    sendClientMailsOficinas()
    sendClientMailsTerrenos()


# hasSendDailyMails = True
# while True:
#     if hasSendDailyMails and datetime.now().hour == 17:
#             hasSendDailyMails = False
#     if not hasSendDailyMails and datetime.now().hour == 22:
#             #mandar mails aca
#             sendClientMailsDeptos()
#             sendClientMailsCasas()
#             hasSendDailyMails = True
#     time.sleep(600)

if __name__ == '__main__':
    main()
