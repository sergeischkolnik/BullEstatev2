import math
import pymysql as mysql
from math import radians, sin, cos, acos, asin,pi,sqrt
from datetime import datetime, timedelta, date
past = datetime.now() - timedelta(days=90)
past=datetime.date(past)
yesterday = datetime.now() - timedelta(days=2)
yesterday=datetime.date(yesterday)
from threading import Thread
import tasador


def from_portalinmobiliario():
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT id2,fechapublicacion,fechascrap,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,lat,lon,estacionamientos,link FROM portalinmobiliario"
    cur.execute(sql)
    tupla = cur.fetchall()
    data = []
    for i in tupla:
        subdata=[]
        a=0
        for j in range (0,len(i)):
            if (i[j]==None):
                a=1
            subdata.append(i[j])
        if (a==0):
            data.append(subdata)
    return data


def insertarRentabilidad(rentabilidad):
    sql = """INSERT INTO rentabilidades_portalinmobiliario(prop,precio,promedio,rentabilidad,velocidad)
             VALUES(%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE precio=%s,promedio=%s,rentabilidad=%s,velocidad=%s"""


    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')

    cur = mariadb_connection.cursor()
    cur.execute(sql, (rentabilidad))
    mariadb_connection.commit()
    mariadb_connection.close()


# def get_precios(prop,precios_seleccionados,precios):
#     for z in precios:
#         if prop==z[0]:
#             precios_seleccionados.append(z[1])

def precios_from_portalinmobiliario():
    mariadb_connection = mysql.connector.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT id2,precio FROM portalinmobiliario"
    cur.execute(sql)
    tupla = cur.fetchall()
    data = []
    for i in tupla:
        subdata=[]
        a=0
        for j in range (0,len(i)):
            if (i[j]==None):
                a=1
            subdata.append(i[j])
        if (a==0):
            data.append(subdata)
    return data

def corrertasacion(data,prop):
    tasacion=tasador.calcularTasacion(prop,data)
    try:
        velocidad=(prop[2]-prop[1]).days
        precio_promedio=float(tasacion)
        precio_propiedad=prop[5]
        rentabilidad=float((precio_promedio-precio_propiedad)/precio_promedio)
        rentabilidades=[]
        rentabilidades.append(prop[0])
        rentabilidades.append(precio_propiedad)
        rentabilidades.append(precio_promedio)
        rentabilidades.append(rentabilidad)
        rentabilidades.append(velocidad)
        rentabilidades.append(precio_propiedad)
        rentabilidades.append(precio_promedio)
        rentabilidades.append(rentabilidad)
        rentabilidades.append(velocidad)


        insertarRentabilidad(rentabilidades)

    except:
        print("exception")



data=from_portalinmobiliario()
threadList=[]

for x,prop in enumerate (data):

    corrertasacion(data,prop)
    print(str(x)+"/"+str(len(data)))


