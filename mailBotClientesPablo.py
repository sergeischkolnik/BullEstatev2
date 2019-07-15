import threading
import pymysql as mysql
from datetime import datetime, timedelta
import random
import sendMailVendetudeptoPablo as mailer
import time

past = datetime.now() - timedelta(days=60)
past=datetime.date(past)
yesterday = datetime.now() - timedelta(days=5)
yesterday=datetime.date(yesterday)

sleepTime=random.randint(150,250)

sqlAux1="((portalinmobiliario.dormitorios='1') or (portalinmobiliario.dormitorios='2'))"

sqlDeptosArriendo = "select duenos.mail,portalinmobiliario.nombre,portalinmobiliario.link from duenos inner join portalinmobiliario where " \
          "duenos.idProp=portalinmobiliario.id2 and duenos.contactado IS NULL and " \
          "duenos.esDueno='si' and (portalinmobiliario.operacion='arriendo') and portalinmobiliario.tipo='departamento' and " \
          "portalinmobiliario.fechascrap>='"+str(yesterday)+"' and portalinmobiliario.fechapublicacion>'" + str(past) + "' and " \
          "((portalinmobiliario.link like '%concon%' and "+sqlAux1+") or " \
          "(portalinmobiliario.link like '%renaca%' and "+sqlAux1+"));"
          # "(portalinmobiliario.link like '%estacion-central%' and "+sqlAux1+") or " \
          # "(portalinmobiliario.link like '%macul%' and "+sqlAux1+") or " \
          # "(portalinmobiliario.link like '%quinta-normall%' and "+sqlAux1+") or " \
          # "(portalinmobiliario.link like '%san-joaquin%' and "+sqlAux1+") or " \
          # "(portalinmobiliario.link like '%la-florida%' and "+sqlAux1+") or " \
          # "(portalinmobiliario.link like '%maipu%' and "+sqlAux1+") or " \
          # "(portalinmobiliario.link like '%la-cisterna%' and "+sqlAux1+") or " \
          # "(portalinmobiliario.link like '%recoleta%' and "+sqlAux1+") or " \
          # "(portalinmobiliario.link like '%renaca%'));"

sqlAux="((portalinmobiliario.dormitorios='1') or (portalinmobiliario.dormitorios='2'))"

sqlDeptosVenta = "select duenos.mail,portalinmobiliario.nombre,portalinmobiliario.link from duenos inner join portalinmobiliario where " \
          "duenos.idProp=portalinmobiliario.id2 and duenos.contactado IS NULL and " \
          "duenos.esDueno='si' and (portalinmobiliario.operacion='venta') and portalinmobiliario.tipo='departamento' and " \
          "portalinmobiliario.fechascrap>='"+str(yesterday)+"' and portalinmobiliario.fechapublicacion>'" + str(past) + "' and " \
          "((portalinmobiliario.link like '%con-con%' and "+sqlAux1+") or " \
          "(portalinmobiliario.link like '%renaca%' and "+sqlAux1+"));"
          # "(portalinmobiliario.link like '%estacion-central%' and "+sqlAux1+") or " \
          # "(portalinmobiliario.link like '%macul%' and "+sqlAux1+") or " \
          # "(portalinmobiliario.link like '%quinta-normall%' and "+sqlAux1+") or " \
          # "(portalinmobiliario.link like '%san-joaquin%' and "+sqlAux1+") or " \
          # "(portalinmobiliario.link like '%la-florida%' and "+sqlAux1+") or " \
          # "(portalinmobiliario.link like '%maipu%' and "+sqlAux1+") or " \
          # "(portalinmobiliario.link like '%la-cisterna%' and "+sqlAux1+") or " \
          # "(portalinmobiliario.link like '%recoleta%' and "+sqlAux1+") or " \
          # "(portalinmobiliario.link like '%renaca%'));"

sqlCasas = "select duenos.mail,portalinmobiliario.nombre,portalinmobiliario.link from duenos inner join portalinmobiliario where " \
      "duenos.idProp=portalinmobiliario.id2 and duenos.contactado IS NULL and " \
      "duenos.esDueno='si' and portalinmobiliario.precio>'400000' and (portalinmobiliario.operacion='arriendo') and portalinmobiliario.tipo='casa' and " \
      "portalinmobiliario.fechascrap>='" + str(yesterday) + "' and portalinmobiliario.fechapublicacion>'" + str(
    past) + "' and " \
            "(portalinmobiliario.link like '%lo-barnechea%' or " \
            "portalinmobiliario.link like '%vitacura%' or " \
            "portalinmobiliario.link like '%la-florida%' or " \
            "portalinmobiliario.link like '%providencia%' or " \
            "portalinmobiliario.link like '%nunoa%' or " \
            "(portalinmobiliario.link like '%colina%' and ((portalinmobiliario.lat<'-33.264536' and portalinmobiliario.lat>'-33.308362' and portalinmobiliario.lon<'-70.618245' and portalinmobiliario.lon>'-70.699193') or (portalinmobiliario.lat<'-33.301430' and portalinmobiliario.lat>'-33.335555' and portalinmobiliario.lon<'-70.622641' and portalinmobiliario.lon>'-70.666652'))) or " \
            "portalinmobiliario.link like '%maipu%' or " \
            "portalinmobiliario.link like '%las-condes%' or portalinmobiliario.link like '%la-reina%');"

sqlOficinasArriendo = "select duenos.mail,portalinmobiliario.nombre,portalinmobiliario.link from duenos inner join portalinmobiliario where " \
          "duenos.idProp=portalinmobiliario.id2 and duenos.contactado IS NULL and " \
          "duenos.esDueno='si' and (portalinmobiliario.operacion='arriendo') and (portalinmobiliario.tipo='oficina' or portalinmobiliario.tipo='comercial') and " \
          "portalinmobiliario.fechascrap>='"+str(yesterday)+"' and portalinmobiliario.fechapublicacion>'" + str(past) + "' and " \
          "((portalinmobiliario.link like '%santiago-metropolitana%') or " \
          "(portalinmobiliario.link like '%san-miguel%') or " \
          "(portalinmobiliario.link like '%estacion-central%') or " \
          "(portalinmobiliario.link like '%macul%') or " \
          "(portalinmobiliario.link like '%quinta-normall%') or " \
          "(portalinmobiliario.link like '%san-joaquin%') or " \
          "(portalinmobiliario.link like '%la-florida%') or " \
          "(portalinmobiliario.link like '%maipu%') or " \
          "(portalinmobiliario.link like '%recoleta%') or " \
          "(portalinmobiliario.link like '%independencia%'));"

sqlAux=""

sqlOficinasVenta = "select duenos.mail,portalinmobiliario.nombre,portalinmobiliario.link from duenos inner join portalinmobiliario where " \
          "duenos.idProp=portalinmobiliario.id2 and duenos.contactado IS NULL and " \
          "duenos.esDueno='si' and (portalinmobiliario.operacion='venta') and (portalinmobiliario.tipo='oficina' or portalinmobiliario.tipo='comercial') and " \
          "portalinmobiliario.fechascrap>='"+str(yesterday)+"' and portalinmobiliario.fechapublicacion>'" + str(past) + "' and " \
          "((portalinmobiliario.link like '%santiago-metropolitana%') or " \
          "(portalinmobiliario.link like '%san-miguel%') or " \
          "(portalinmobiliario.link like '%quinta-normall%') or " \
          "(portalinmobiliario.link like '%estacion-central%') or " \
          "(portalinmobiliario.link like '%macul%') or " \
          "(portalinmobiliario.link like '%san-joaquin%') or " \
          "(portalinmobiliario.link like '%la-florida%') or " \
          "(portalinmobiliario.link like '%maipu%') or " \
          "(portalinmobiliario.link like '%recoleta%') or " \
          "(portalinmobiliario.link like '%independencia%'));"

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

    for i,l in enumerate(lista):

        to = str(l[0])
        nombreProp = str(l[1])
        linkProp=str(l[2])

        #gratis
        mailer.sendMailGratis(to,nombreProp,linkProp)
        checkClient(to,"1")

        time.sleep(sleepTime)
def sendClientMailsDeptosVenta():

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sqlDeptosVenta)
    lista = cur.fetchall()
    mariadb_connection.close()

    print("[" + str(datetime.now()) +"]Sending mails (dptos venta) to "+str(len(lista))+ " clients:")

    for i,l in enumerate(lista):

        to = str(l[0])
        nombreProp = str(l[1])
        linkProp=str(l[2])

        #gratis
        mailer.sendMailGratis(to,nombreProp,linkProp)
        checkClient(to,"1")

        time.sleep(sleepTime)

def sendClientMailsCasas():

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sqlCasas)
    lista = cur.fetchall()
    mariadb_connection.close()

    print("[" + str(datetime.now()) +"]Sending mails (casas) to "+str(len(lista))+ " clients:")

    for i,l in enumerate(lista):
        to = str(l[0])
        nombreProp = str(l[1])
        linkProp=str(l[2])

        mailer.sendMailGratis(to,nombreProp,linkProp)
        checkClient(to,"1")

        time.sleep(sleepTime)

def sendClientMailsOficinasArriendo():


    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sqlOficinasArriendo)
    lista = cur.fetchall()
    mariadb_connection.close()

    print("[" + str(datetime.now()) +"]Sending mails (oficinas arriendo) to "+str(len(lista))+ " clients:")

    for i,l in enumerate(lista):
        to = str(l[0])
        nombreProp = str(l[1])

        linkProp=str(l[2])

        mailer.sendMailGratis(to,nombreProp,linkProp)
        checkClient(to,"1")

        time.sleep(sleepTime)

def sendClientMailsOficinasVenta():


    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sqlOficinasVenta)
    lista = cur.fetchall()
    mariadb_connection.close()

    print("[" + str(datetime.now()) +"]Sending mails (oficinas venta) to "+str(len(lista))+ " clients:")

    for i,l in enumerate(lista):
        to = str(l[0])
        nombreProp = str(l[1])

        linkProp=str(l[2])

        mailer.sendMailGratis(to,nombreProp,linkProp)
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

    print("[mailbotPahola][" + str(datetime.now()) + "]Sending mails (dptos) to " + str(len(listaDeptos)) + " clients:")
    for i,l in enumerate(listaDeptos):
        if not getattr(t, "do_run", True):
            print("[mailbotPahola] Deteniendo mailer")
            return
        to = str(l[0])
        nombreProp = str(l[1])
        linkProp=str(l[2])

        #gratis
        mailer.sendMailGratis(to,nombreProp,linkProp)
        checkClient(to,"1")

        time.sleep(sleepTime)

    # print("[mailbotFran][" + str(datetime.now()) +"]Sending mails (casas) to "+str(len(listaCasas))+ " clients:")
    #
    # for i,l in enumerate(listaCasas):
    #     if not getattr(t, "do_run", True):
    #         print("[mailbotFran] Deteniendo mailer")
    #         return
    #     to = str(l[0])
    #     nombreProp = str(l[1])
    #     linkProp=str(l[2])
    #
    #     mailer.sendMailGratis(to,nombreProp,linkProp)
    #     checkClient(to,"1")
    #
    #     time.sleep(sleepTime)
    #
    # print("[mailbotFran][" + str(datetime.now()) +"]Sending mails (oficinas) to "+str(len(listaOficinas))+ " clients:")
    #
    # for i,l in enumerate(listaOficinas):
    #     if not getattr(t, "do_run", True):
    #         print("[mailbotFran] Deteniendo mailer")
    #         return
    #     to = str(l[0])
    #     nombreProp = str(l[1])
    #
    #     linkProp=str(l[2])
    #
    #     mailer.sendMailGratis(to,nombreProp,linkProp)
    #     checkClient(to,"1")
    #
    #     time.sleep(sleepTime)

def main():
    sendClientMailsDeptosArriendo()
    sendClientMailsDeptosVenta()
    #sendClientMailsCasas()
    #sendClientMailsOficinasArriendo()
    #sendClientMailsOficinasVenta()



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
