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


def rentaPProm(tipo,dormitorios,banos,estacionamientos,comuna):
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT (precio/metrosmin) FROM portalinmobiliario WHERE operacion='arriendo' and tipo='"+str(tipo)+"' and dormitorios='"+str(dormitorios)+"' and banos='"+str(banos)+"' and estacionamientos='"+str(estacionamientos)+"' and link like '%"+str(comuna)+"%'"
    cur.execute(sql)
    arriendo = cur.fetchall()
    cur = mariadb_connection.cursor()
    sql = "SELECT (precio/metrosmin) FROM portalinmobiliario WHERE operacion='venta' and dormitorios='"+str(dormitorios)+"' and banos='"+str(banos)+"' and estacionamientos='"+str(estacionamientos)+"' and link like '%"+str(comuna)+"%'"
    cur.execute(sql)
    venta = cur.fetchall()
    arriendo=sorted(arriendo)
    venta=sorted(venta)
    larriendo=len(arriendo)
    lventa=len(venta)
    minarriendo=int(larriendo*0.1)
    minventa=int(lventa*0.1)
    maxarriendo=int(larriendo*0.9)
    maxventa=int(lventa*0.9)
    arriendo=arriendo[minarriendo:maxarriendo]
    venta=venta[minventa:maxventa]
    sumarriendo=0
    sumventa=0
    for i in arriendo:
        sumarriendo+=i[0]
    for j in venta:
        sumventa+=j[0]

    promarriendo=(sumarriendo) / max(len(arriendo), 1)
    promventa=float(sumventa)/max(len(venta),1)
    try:
        valor=promarriendo*12/promventa
        return valor
    except:
        return 0


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
    print(comuna)
    for tipo in tipos:
        print(tipo)
        for dormitorio in dormitorios:
            print(dormitorio)
            for bano in banos:
                print (bano)
                for estacionamiento in estacionamientos:

                    try:
                        rent=rentaPProm(tipo,dormitorio,bano,estacionamiento,comuna)
                        if rent>0.01:
                            print ("la rentabilidad en "+str(comuna)+" para el tipo de propiedad "+str(tipo)+" con "+str(dormitorio)+" dormitorio, "+(str(bano)+" baños, y "+str(estacionamiento)+" estacionamientos, es de "+str(rent*100)+"%."))
                    except:
                        continue
