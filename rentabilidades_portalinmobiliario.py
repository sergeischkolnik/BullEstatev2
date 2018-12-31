import math
import mysql.connector
from math import radians, sin, cos, acos, asin,pi,sqrt
from datetime import datetime, timedelta, date
past = datetime.now() - timedelta(days=90)
past=datetime.date(past)
yesterday = datetime.now() - timedelta(days=2)
yesterday=datetime.date(yesterday)
from threading import Thread

def insertarRentabilidad(rentabilidad):
    sql = """INSERT INTO rentabilidades_portalinmobiliario(prop,precio,promedio,rentabilidad)
             VALUES(%s,%s,%s,%s) ON DUPLICATE KEY UPDATE precio=%s,promedio=%s,rentabilidad=%s"""


    mariadb_connection = mysql.connector.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')

    cur = mariadb_connection.cursor()
    cur.execute(sql, (rentabilidad))
    mariadb_connection.commit()
    mariadb_connection.close()


def get_precios(prop,precios_seleccionados,precios):
    for z in precios:
        if prop==z[0]:
            precios_seleccionados.append(z[1])
def from_distancias_portalinmobiliario():
    mariadb_connection = mysql.connector.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT prop1,prop2,distancia FROM distancias_portalinmobiliario"
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
v=True
while v==True:
    data=from_distancias_portalinmobiliario()
    data=sorted(data,key=lambda x:x[0])
    precios=precios_from_portalinmobiliario()
    prop1a=None
    prop2a=None
    count=-1
    validator=False
    for i in data:
        count=count+1
        print(str(count)+"/"+str(len(data)))
        prop1=i[0]
        prop2=i[1]
        distancia=i[2]
        if (prop1!=prop1a):
            if validator==True:
                distancias=sorted(distancias,key=lambda x:x[1])
                try:
                    distancias=distancias[:40]
                except:
                    distancias=distancias
                threadlist=[]
                precios_seleccionados=[]
                for d in distancias:
                    t=Thread(target=get_precios,args=(d[0],precios_seleccionados,precios))
                    t.start()
                    threadlist.append(t)
                for i in threadlist:
                    t.join()
                for z in precios:
                    if (prop1a==z[0]):
                        precio_propiedad=z[1]
                precio_promedio=sum(precios_seleccionados)/float(len(precios_seleccionados))
                rentabilidad=((precio_promedio-precio_propiedad)/precio_promedio)
                rentabilidades=[]
                rentabilidades.append(prop1a)
                rentabilidades.append(precio_propiedad)
                rentabilidades.append(precio_promedio)
                rentabilidades.append(rentabilidad)
                rentabilidades.append(precio_propiedad)
                rentabilidades.append(precio_promedio)
                rentabilidades.append(rentabilidad)
                try:
                    insertarRentabilidad(rentabilidades)
                except:
                    continue
                    print("exception")
            validator=True
            distancias=[]
            subdistancias=[]
            subdistancias.append(prop2)
            subdistancias.append(distancia)
            distancias.append(subdistancias)
            prop1a=prop1
        else:
            subdistancias=[]
            subdistancias.append(prop2)
            subdistancias.append(distancia)
            distancias.append(subdistancias)
            prop1a=prop1
