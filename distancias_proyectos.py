import math
import mysql.connector
from math import radians, sin, cos, acos, asin,pi,sqrt
from datetime import datetime, timedelta, date
past = datetime.now() - timedelta(days=90)
past=datetime.date(past)
yesterday = datetime.now() - timedelta(days=2)
yesterday=datetime.date(yesterday)
from threading import Thread
from time import sleep

def insertarDistancia(distance):

    sql = """INSERT INTO distancias_pproyectos(uni,prop1,prop2,distancia)
             VALUES(%s,%s,%s,%s) ON DUPLICATE KEY UPDATE distancia=%s"""

    mariadb_connection = mysql.connector.connect(user='root', password='sergei', host='127.0.0.1', database='proyectos')

    cur = mariadb_connection.cursor()
    cur.execute(sql, (distance))
    mariadb_connection.commit()
    mariadb_connection.close()

def from_deptos():
    mariadb_connection = mysql.connector.connect(user='root', password='sergei', host='127.0.0.1', database='proyectos')
    cur = mariadb_connection.cursor()
    sql = "SELECT id2,fechapublicacion,fechascrap,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,lat,lon,estacionamientos FROM portalinmobiliario"
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

def calcularDistancia(i,data):

    if i[1]>past:
        for j in data:

            if (j[2]>yesterday) and (i[3]==j[3]) and (i[4]==j[4]) and (i[6]==j[6]) and (i[7]==j[7]) and (i[12]==j[12]) and (j!=i):
                lat1=i[10]
                long1=i[11]
                lat2=j[10]
                long2=j[11]
                r=6371000
                c=pi/180
                distance= 2*r*asin(sqrt(sin(c*(lat2-lat1)/2)**2 + cos(c*lat1)*cos(c*lat2)*sin(c*(long2-long1)/2)**2))

                if (distance < 500) and (abs(i[8]-j[8])<5) and (abs(i[9]-j[9]<10)):
                    d=sqrt(distance*distance+(100*abs(i[8]-j[8])*(100*abs(i[8]-j[8])))+(100*abs(i[9]-j[9])*(100*abs(i[9]-j[9]))))
                    distancia=[]
                    unique=(str(i[0])+str(j[0]))
                    distancia.append(unique)
                    distancia.append(i[0])
                    distancia.append(j[0])
                    distancia.append(d)
                    distancia.append(d)

                    insertarDistancia(distancia)

def Main():
    data=from_portalinmobiliario()

    validator=False
    while validator==False:
        data=from_portalinmobiliario()
        threadList=[]
        b=0
        for i in data:
            t=Thread(target=calcularDistancia, args=(i,data))
            t.start()
            print(str(b)+" Thread Started")
            b=b+1
            threadList.append(t)
            sleep(0.05)
        for t in threadList:
            t.join

Main()

