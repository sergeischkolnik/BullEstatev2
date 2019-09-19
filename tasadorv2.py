import math
import pymysql as mysql
import math
from math import radians, sin, cos, acos, asin,pi,sqrt
from datetime import datetime, timedelta, date
past = datetime.now() - timedelta(days=90)
past=datetime.date(past)
yesterday = datetime.now() - timedelta(days=15)
yesterday=datetime.date(yesterday)
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import uf
import statistics as stat
import reportes
import time

uf1=uf.getUf()


def regresion(x_train,y_train,x_test):

    regr = linear_model.LinearRegression()

    regr.fit(x_train, y_train)

    price=regr.intercept_
    c=0

    utilnegativa=regr.coef_[0]<-0.001
    terrazanegativa = regr.coef_[1]<-0.001
    estacionamientosnegativa =regr.coef_[4]<-0.001

    for coef in regr.coef_:
        price=price+coef*x_test[c]
        c=c+1

    return price,utilnegativa,terrazanegativa,estacionamientosnegativa,regr.coef_

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

def from_portalinmobiliario(operacion,tipo,region):
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT id2,fechapublicacion,fechascrap,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,lat,lon,estacionamientos,link FROM portalinmobiliario "
    sqlWhere="WHERE operacion='"+str(operacion)+"' and region='"+str(region)+"' and tipo='"+str(tipo)+"'"
    sql=sql+sqlWhere
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



def calcularTasacionData(operacion,tipo,lat,lon,util,total,dormitorios,banos,estacionamientos,data):

    ufn=uf.getUf()
    es_venta=operacion=="venta"

    #Generar Regresion General con datos:

    y_train = []
    x_train = []


    #Data=id2,fechapublicacion,fechascrap,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,lat,lon,estacionamientos,link
    for prop in data:
        reg_total = prop[9]
        reg_util = prop[8]
        reg_dorms = prop[6]
        reg_banos = prop[7]
        reg_precio = prop[5]
        reg_estacionamientos = prop[12]
        x_train.append([reg_util, reg_total, reg_dorms, reg_banos, reg_estacionamientos])
        y_train.append(reg_precio)

    # y2_train=[]
    # y2_train.append(y_train)
    # y_train=y2_train
    x_train = np.array(x_train)
    y_train = np.array(y_train)

    x_test = [util, total, dormitorios, banos, estacionamientos]
    x_test = np.array(x_test)
    x_test = np.transpose(x_test)
    # Make predictions using the testing set

    p, utilnegativo, terrazanegativo, estacionamientosnegativo, coef = regresion(x_train, y_train, x_test)

    #print("Regresion Hecha")

    #print(coef)
    promcoef=sum(abs(coef))/len(coef)
    matrix=[]
    data=sorted(data, key=lambda x:x[5])
    #Data=id2,fechapublicacion,fechascrap,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,lat,lon,estacionamientos,link
    for j in data:
        # i3=op, i4=tipo, i5=precio, i6=dorms, i7=baños, i12= estacionamientos i8=util, i9=total
        if (j[1]>past) and (j[2]>yesterday) and (operacion==j[3]) and (tipo==j[4]):
            lat1=lat
            long1=lon
            lat2=j[10]
            long2=j[11]
            r=6371000
            c=pi/180
            distance= 2*r*asin(sqrt(sin(c*(lat2-lat1)/2)**2 + cos(c*lat1)*cos(c*lat2)*sin(c*(long2-long1)/2)**2))
            distance2=((promcoef*distance)**2+(coef[0]*(j[8]-util))**2+(coef[1]*(j[9]-util))**2+(coef[2]*(j[6]-util))**2+(coef[3]*(j[7]-util))**2+(coef[4]*(j[12]-util))**2)
            j.append(distance2)
            matrix.append(j)
    matrix = sorted(matrix, key=lambda x: x[14])
    links=[]
    totalDistance=0
    count=0
    totalPrice=0
    totalAntiDistance=0
    lastDistance=0
    for m in matrix:
        count+=1
        mprom=(m[8]+m[9])/2
        totalDistance+=m[14]
        totalAntiDistance+=1/m[14]
        totalPrice+=m[5]/(m[14]*mprom)
        links.append(m[13])

        if count>10 and (m[14]-lastDistance)>(m[14]/count):
            break
        lastDistance=m[14]
    price=totalPrice/totalAntiDistance
    price=price*((util+total)/2)



    try:
        if es_venta:
            price = int(price/ufn)
        else:
            price = int(price)
        return(price,totalDistance,count,links,es_venta,1)

    except:

        return (0,"N",count,["No hay links para tasación inválida",""],es_venta,13)

if __name__ == "__main__":

    operacion = "venta"
    tipo = "departamento"
    lat =-33.4526
    lon=-70.6321
    util = 45
    total = 45
    dormitorios = 2
    banos = 1
    estacionamientos=1
    comunas=[]
    comunas.append("santiago")
    data=reportes.from_portalinmobiliario(tipo,"metropolitana",comunas,False)
    precio,confianza,nrProps,links,venta,g = calcularTasacionData(operacion,tipo,lat,lon,util,total,dormitorios,banos,estacionamientos,data)
    print(precio)
    print(confianza)
    print(nrProps)
    links=links[:5]
    for link in links:
        print(link)