import psycopg2
import math
import mysql.connector
import math
from math import radians, sin, cos, acos, asin,pi,sqrt
from datetime import datetime, timedelta, date
past = datetime.now() - timedelta(days=90)
past=datetime.date(past)
yesterday = datetime.now() - timedelta(days=2)
yesterday=datetime.date(yesterday)
from threading import Thread
from time import sleep
import scipy
import uf

def mean(numbers):
    suma=0
    for i in numbers:
        i=i[0]
        i=i[0]

        suma=suma+i
    promedio=suma/len(numbers)
    suma=0
    for i in numbers:
        i=i[0]
        i=i[0]
        suma=suma+abs(i-promedio)
    desvest=suma/len(numbers)

    cosa=[]
    cosa.append(promedio)
    cosa.append(desvest)
    return cosa

def mean2(numbers):
    suma=0
    for i in numbers:


        suma=suma+i
    promedio=suma/len(numbers)
    suma=0
    for i in numbers:

        suma=suma+abs(i-promedio)
    desvest=suma/len(numbers)

    cosa=[]
    cosa.append(promedio)
    cosa.append(desvest)
    return cosa

def insertarRentabilidada(preciopromedio,rentabilidad,id):
    sql = "UPDATE deptos SET pproma='"+str(preciopromedio)+"',rentabilidada='"+str(rentabilidad)+"' WHERE id='"+str(id)+"'"


    mariadb_connection = mysql.connector.connect(user='root', password='sergei', host='127.0.0.1', database='proyectos')

    cur = mariadb_connection.cursor()
    cur.execute(sql)
    mariadb_connection.commit()
    mariadb_connection.close()

def insertarRentabilidadv(preciopromedio,rentabilidad,id):
    sql = "UPDATE deptos SET ppromv='"+str(preciopromedio)+"',rentabilidadv='"+str(rentabilidad)+"' WHERE id='"+str(id)+"'"
    print(sql)

    mariadb_connection = mysql.connector.connect(user='root', password='sergei', host='127.0.0.1', database='proyectos')

    cur = mariadb_connection.cursor()
    cur.execute(sql)
    mariadb_connection.commit()
    mariadb_connection.close()

def from_deptos():
    mariadb_connection = mysql.connector.connect(user='root', password='sergei', host='127.0.0.1', database='proyectos')
    cur = mariadb_connection.cursor()
    sql = "SELECT deptos.id,deptos.precio,deptos.dormitorios,deptos.banos,deptos.utiles,deptos.totales,deptos.fechascrap,proyectos.tipo,proyectos.lat,proyectos.lon,proyectos.estacionamiento FROM deptos,proyectos WHERE deptos.id_proyecto=proyectos.id2"
    cur.execute(sql)
    deptos=cur.fetchall()
    return deptos

def from_portalinmobiliario():
    mariadb_connection = mysql.connector.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
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

def precio_from_portalinmobiliario(id2):
    mariadb_connection = mysql.connector.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT precio,metrosmin,metrosmax,lat,lon,dormitorios,banos FROM portalinmobiliario WHERE id2='"+str(id2)+"'"
    cur.execute(sql)
    precio = cur.fetchall()

    return precio

def calcularDistancia(i,data,fail):

    distancia=[]
    for j in data:
        if i[7]=="Departamento":
            tipo="departamento"
        elif i[7]=="Casa":
            tipo="casa"
        elif i[7]=="Oficina":
            tipo="oficina"
        try:
            if (j[1]>past) and (tipo==j[4]) and ("arriendo"==j[3]) and (float(i[2])==j[6]) and (float(i[3])==j[7]) and (float(i[10])==j[12]):
                lat1=i[8]
                long1=i[9]
                lat2=j[10]
                long2=j[11]
                r=6371000
                c=pi/180
                distance= 2*r*asin(sqrt(sin(c*(lat2-lat1)/2)**2 + cos(c*lat1)*cos(c*lat2)*sin(c*(long2-long1)/2)**2))

                if (distance < 1500) and (abs(i[4]/j[8]-1)<0.2) and (abs(i[5]/j[9]-1)<0.4):
                    d=sqrt(distance*distance+(100*abs(i[4]-j[8])*(100*abs(i[4]-j[8])))+(100*abs(i[5]-j[9])*(100*abs(i[5]-j[9]))))
                    subdistancia=[]
                    subdistancia.append(j[0])
                    subdistancia.append(d)
                    distancia.append(subdistancia)
        except:
            continue

    distancias=sorted(distancia,key=lambda x:x[1])
    try:
        distancias=distancias[:40]
    except:
        distancias=distancia

    prices=[]
    count=0
    for d in distancias:
        p=precio_from_portalinmobiliario(d[0])
        if (count==1) and (q==p):
            continue
        else:
            prices.append(p)
            count=1
            q=p
    try:
        cosa=mean(prices)
        precio=cosa[0]
        unf=uf.getUf()
        precio2=precio/unf

        rentabilidad=(precio2*12)/i[1]

        insertarRentabilidada(precio,rentabilidad,i[0])
    except:
        fail=fail+1

def calcularDistancia2(i,deptos,fail):

    distancia=[]
    for j in deptos:
        if (j[0]==i[0]):
            continue
        try:
            if (i[7]==j[7]) and (float(i[2])==j[2]) and (float(i[3])==j[3]) and (float(i[10])==float(j[10])):
                lat1=i[8]
                long1=i[9]
                lat2=j[8]
                long2=j[9]
                r=6371000
                c=pi/180
                distance= 2*r*asin(sqrt(sin(c*(lat2-lat1)/2)**2 + cos(c*lat1)*cos(c*lat2)*sin(c*(long2-long1)/2)**2))

                if (distance < 1500) and (abs(i[4]/j[4]-1)<0.1) and (abs(i[5]/j[4]-1)<0.15):
                    d=sqrt(distance*distance+(100*abs(i[4]-j[4])*(100*abs(i[4]-j[4])))+(100*abs(i[5]-j[5])*(100*abs(i[5]-j[5]))))
                    subdistancia=[]
                    subdistancia.append(j[0])
                    subdistancia.append(j[1])
                    subdistancia.append(d)
                    distancia.append(subdistancia)
        except:
            continue

    distancias=sorted(distancia,key=lambda x:x[2])
    try:
        distancias=distancias[:40]
    except:
        distancias=distancia

    prices=[]
    count=0
    for d in distancias:
        p=d[1]
        prices.append(p)
    try:
        cosa=mean2(prices)
        precio=cosa[0]


        rentabilidad=((precio)-i[1])/i[1]

        insertarRentabilidadv(precio,rentabilidad,i[0])
    except:
        fail=fail+1

data=from_portalinmobiliario()
deptos=from_deptos()
l=len(deptos)
faillist=0
threadList1=[]
threadList2=[]
b=0
for i in deptos:
    t1=Thread(target=calcularDistancia, args=(i,data,faillist))
    t2=Thread(target=calcularDistancia2, args=(i,deptos,faillist))
    #calcularDistancia2(i,deptos,faillist)
    t1.start()
    t2.start()
    b=b+1
    threadList1.append(t1)
    threadList1.append(t2)
    sleep(0.05)
for t in threadList1:
    t.join
for t in threadList2:
    t.join
