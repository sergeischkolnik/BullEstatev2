import math
from lxml import html
import requests
import datetime
from threading import Thread
import pymysql as mysql
from itertools import cycle
import agentCreator
import time
import random
from requests_html import HTMLSession
session = HTMLSession()

def getBanned():
    sql="SELECT mail FROM baneados"
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    baneados = cur.fetchall()
    mariadb_connection.close()
    return baneados

def quitarDueno(mail):

    sql = "UPDATE duenos SET esDueno='no' WHERE mail='"+str(mail)+"'"

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')

    cur = mariadb_connection.cursor()
    cur.execute(sql)
    mariadb_connection.commit()
    mariadb_connection.close()

banned=getBanned()
print(banned)
for ban in banned:
    quitarDueno(ban)
print("dueños actualizados")
