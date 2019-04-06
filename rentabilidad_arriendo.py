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

def insertarRentabilidad(rent):
    #Inserta una propiedad en una base de datos

    sql = """INSERT INTO rentabilidad(id2,comuna,tipo,dormitorios,banos,estacionamientos,rentabilidad)
             VALUES(%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE rentabilidad=%s"""

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')

    cur = mariadb_connection.cursor()
    cur.execute(sql, (rent))

    mariadb_connection.commit()
    mariadb_connection.close()


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
    maxarriendo=int(larriendo*0.95)
    maxventa=int(lventa*0.95)
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
        return valor,len(arriendo),len(venta)
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
        if comuna not in comunas and ('metropolitana' in comuna):

            comunas.append(comuna)

    return comunas

comunas=obtenercomunas()
tipos=obtenertipos()
dormitorios=[1,2]
banos=[1,2]
estacionamientos=[0,1]
tipos=["departamento"]
for comuna in comunas:
    for tipo in tipos:
        for dormitorio in dormitorios:
            for bano in banos:
                for estacionamiento in estacionamientos:

                    try:
                        rent,lena,lenv=rentaPProm(tipo,dormitorio,bano,estacionamiento,comuna)
                        if rent>0.01 and lena>49 and lenv>49:
                            comunasinmet=comuna[:-14]
                            idrent=str(comunasinmet)+str(tipo)+str(dormitorio)+str(bano)+str(estacionamiento)
                            rentabilidad=[]
                            rentabilidad.append(idrent)
                            rentabilidad.append(comunasinmet)
                            rentabilidad.append(tipo)
                            rentabilidad.append(dormitorio)
                            rentabilidad.append(bano)
                            rentabilidad.append(estacionamiento)
                            rentabilidad.append(rent)
                            rentabilidad.append(rent)
                            insertarRentabilidad(rentabilidad)
                            print ("la rentabilidad en "+str(comunasinmet)+" para el tipo de propiedad "+str(tipo)+" con "+str(dormitorio)+" dormitorio, "+(str(bano)+" baños, y "+str(estacionamiento)+" estacionamientos, es de "+str(float(int(rent*10000))/100)+"%."))
                    except:
                        continue
