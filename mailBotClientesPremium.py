
import pymysql as mysql
from datetime import datetime, timedelta
import random
import sendMailVendetudeptoPremium as mailer
import time
import threading

past = datetime.now() - timedelta(days=360)
past = datetime.date(past)
yesterday = datetime.now() - timedelta(days=5)
yesterday = datetime.date(yesterday)

sleeptime = random.randint(150, 250)

sql = "select duenos.mail,portalinmobiliario.nombre,portalinmobiliario.link from duenos inner join portalinmobiliario where " \
          "duenos.idProp=portalinmobiliario.id2 and duenos.contactado IS NULL and " \
          "duenos.esDueno='si' and (portalinmobiliario.link like '%las-condes%' or portalinmobiliario.link like '%vitacura%' or " \
          "portalinmobiliario.link like '%lo-barnechea%' or portalinmobiliario.link like '%la-reina%' or portalinmobiliario.link like '%providencia%' or " \
          "portalinmobiliario.link like '%nuna%' or portalinmobiliario.link like '%chicureo%') and " \
          "portalinmobiliario.fechascrap>='"+str(yesterday)+"' and portalinmobiliario.fechapublicacion>'" + str(past) + "' and " \
          "portalinmobiliario.precio>='200000000'"



def checkClient(clientMail,comision):
    sql = "UPDATE duenos SET contactado='si',comision='"+str(comision)+"' WHERE mail='"+str(clientMail)+"'"
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    mariadb_connection.commit()
    mariadb_connection.close()

def sendClientMails():
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    lista = cur.fetchall()
    mariadb_connection.close()
    print(sql)
    print("[mailerFer][" + str(datetime.now()) +"]Sending mails (dptos) to "+str(len(lista))+ " clients:")

    for i,l in enumerate(lista):

        to = str(l[0])
        nombreProp = str(l[1])
        linkProp=str(l[2])

        #gratis
        mailer.sendMailGratis(to,nombreProp,linkProp)
        checkClient(to,"1")

        time.sleep(sleeptime)


def threadSendMails():
    t = threading.currentThread()

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()

    cur.execute(sqlDptos)
    listaDeptos = cur.fetchall()

    cur.execute(sqlCasas)
    listaCasas = cur.fetchall()

    cur.execute(sqlOficinas)
    listaOficinas = cur.fetchall()

    mariadb_connection.close()

    print("[mailbotFer][" + str(datetime.now()) + "]Sending mails (dptos) to " + str(len(listaDeptos)) + " clients:")
    for i,l in enumerate(listaDeptos):
        if not getattr(t, "do_run", True):
            print("[mailbotFer] Deteniendo mailer")
            return
        to = str(l[0])
        nombreProp = str(l[1])
        linkProp=str(l[2])

        #gratis
        mailer.sendMailGratis(to,nombreProp,linkProp)
        checkClient(to,"1")


        time.sleep(sleeptime)

    print("[mailbotFer][" + str(datetime.now()) +"]Sending mails (casas) to "+str(len(listaCasas))+ " clients:")

    for i,l in enumerate(listaCasas):
        if not getattr(t, "do_run", True):
            print("[mailbotFer] Deteniendo mailer")
            return
        to = str(l[0])
        nombreProp = str(l[1])
        linkProp=str(l[2])

        mailer.sendMailGratis(to,nombreProp,linkProp)
        checkClient(to,"1")

        time.sleep(sleeptime)

    print("[mailbotFer][" + str(datetime.now()) +"]Sending mails (oficinas) to "+str(len(listaOficinas))+ " clients:")

    for i,l in enumerate(listaOficinas):
        if not getattr(t, "do_run", True):
            print("[mailbotFer] Deteniendo mailer")
            return
        to = str(l[0])
        nombreProp = str(l[1])

        linkProp=str(l[2])

        mailer.sendMailGratis(to,nombreProp,linkProp)
        checkClient(to,"1")

        time.sleep(sleeptime)

def main():
    sendClientMails()


if __name__ == '__main__':
    main()


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
