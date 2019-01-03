import math
import pymysql as mysql
import math
from math import radians, sin, cos, acos, asin,pi,sqrt
from datetime import datetime, timedelta, date
past = datetime.now() - timedelta(days=90)
past=datetime.date(past)
yesterday = datetime.now() - timedelta(days=60)
yesterday=datetime.date(yesterday)
from threading import Thread
from time import sleep

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

def insertarTasacion(precio,preciomin,preciomax,id):
    sql = "UPDATE tasaciones SET precio='"+str(precio)+"',preciomin='"+str(preciomin)+"',preciomax='"+str(preciomax)+"' WHERE id='"+str(id)+"'"


    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')

    cur = mariadb_connection.cursor()
    cur.execute(sql)
    mariadb_connection.commit()
    mariadb_connection.close()

def from_tasaciones():
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT id,cliente,descripcion,operacion,tipo,precio,dormitorios,banos,util,total,lat,lon,estacionamientos,estado FROM tasaciones"
    cur.execute(sql)
    tasaciones=cur.fetchall()
    return tasaciones

def from_portalinmobiliario():
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
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
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT precio,metrosmin,metrosmax,lat,lon,dormitorios,banos FROM portalinmobiliario WHERE id2='"+str(id2)+"'"
    cur.execute(sql)
    precio = cur.fetchall()

    return precio

def calcularDistancia(i,data):

    distancia=[]
    for j in data:

        if (j[1]>past) and (i[3]==j[3]) and (i[4]==j[4]) and (i[6]==j[6]) and (i[7]==j[7]) and (i[12]==j[12]) and (j!=i):
            lat1=i[10]
            long1=i[11]
            lat2=j[10]
            long2=j[11]
            r=6371000
            c=pi/180
            distance= 2*r*asin(sqrt(sin(c*(lat2-lat1)/2)**2 + cos(c*lat1)*cos(c*lat2)*sin(c*(long2-long1)/2)**2))

            if (distance < 1000) and (abs(i[8]/j[8]-1)<0.1) and (abs(i[9]/j[9]-1)<0.2):
                d=sqrt(distance*distance+(100*abs(i[8]-j[8])*(100*abs(i[8]-j[8])))+(100*abs(i[9]-j[9])*(100*abs(i[9]-j[9]))))
                subdistancia=[]
                subdistancia.append(j[0])
                subdistancia.append(d)
                distancia.append(subdistancia)


    distancias=sorted(distancia,key=lambda x:x[1])
    try:
        distancias=distancias[:40]
    except:
        distancias=distancia
    print(len(distancias))
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
        std=cosa[1]
        preciomin=precio-std
        preciomax=precio+std

        insertarTasacion(precio,preciomin,preciomax,i[0])
    except:
        print("No existen departamentos para comparar")

data=from_portalinmobiliario()
#data2=from_proyectos()
tasaciones=from_tasaciones()
threadList=[]
b=0
for i in tasaciones:
    if i[13]=="usado":
        t=Thread(target=calcularDistancia, args=(i,data))
        t.start()
        print(str(b+1)+" Thread Started")
        b=b+1
        threadList.append(t)
        sleep(0.05)
for t in threadList:
    t.join
#
# for i in tasaciones:
#     if i[13]=="nuevo":
#         t=Thread(target=calcularDistancia, args=(i,data2))
#         t.start()
#         print(str(b+1)+" Thread Started")
#         b=b+1
#         threadList.append(t)
#         sleep(0.05)
# for t in threadList:
#     t.join
