import pymysql as mysql
from datetime import datetime, timedelta
import random
import sendMailVendetudepto as mailer
import time

past = datetime.now() - timedelta(days=30)
past = datetime.date(past)
yesterday = datetime.now() - timedelta(days=2)
yesterday = datetime.date(yesterday)


def checkCorredor(corredorMail):
    sql = "INSERT INTO corredores (mail) (" + corredorMail + ")"
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    mariadb_connection.commit()
    mariadb_connection.close()


def sendCorredoresMails():
    sql = "SELECT DISTINCT mail FROM duenos WHERE esDueno='no'"
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    lista = cur.fetchall()
    mariadb_connection.close()

    for i, l in enumerate(lista):
        to = str(l[0])
        print(to)
        # gratis
        #mailer.sendMailGratis(to, nombreProp, gratis=True)
        #time.sleep(random.randint(200, 300))


sendCorredoresMails()

