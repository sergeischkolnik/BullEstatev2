import math
import pymysql as mysql
from math import radians, sin, cos, acos, asin,pi,sqrt
from datetime import datetime, timedelta, date
past = datetime.now() - timedelta(days=90)
past=datetime.date(past)
yesterday = datetime.now() - timedelta(days=30)
yesterday=datetime.date(yesterday)
from threading import Thread
from time import sleep
from datetime import datetime, timedelta
import pdfCreatorPropiedadescompra_arriendo as pdfC
import uf
import numpy as np
from sklearn import datasets, linear_model
import sendmail
import tasadorbot2 as tb2
import pubPortalExiste
import math
import reportes

def obtenertipos():

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT DISTINCT tipo FROM portalinmobiliario"
    cur.execute(sql)
    tipos = cur.fetchall()
    tipos2=[]
    for i in tipos:
        tipos2.append(i[0])

    return tipos2

def obtenercomunas():

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT link FROM portalinmobiliario"
    cur.execute(sql)
    links = cur.fetchall()
    comunas=[]
    for i in links:
        j=(i[0].split('/'))

        comuna=j[5]
        if comuna not in comunas and ('valparaiso' in comuna or 'metropolitana' in comuna or 'biobio' in comuna):

            comunas.append(comuna)

    return comunas

comunas=obtenercomunas()
tipos=obtenertipos()
dormitorios=[1,2,3,4,5]
banos=[1,2,3,4,5]
estacionamientos=[1,2,3]

for comuna in comunas:
    for tipo in tipos:
        for dormitorio in dormitorios:
            for bano in banos:
                for estacionamiento in estacionamientos:
                    try:
                        rent=reportes.rentaPProm(tipo,dormitorio,bano,estacionamiento,comuna)
                        print ("la rentabilidad en "+str(comuna)+" para el tipo de propiedad "+str(tipo)+" con "+str(dormitorio)+" dormitorio, "+(str(bano)+" baños, y "+str(estacionamiento)+" estacionamientos, es de "+str(rent)+"%."))
                    except:
                        continue
