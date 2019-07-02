
import math
import pymysql as mysql
from math import radians, sin, cos, acos, asin,pi,sqrt
from datetime import datetime, timedelta, date
past = datetime.now() - timedelta(days=90)
past=datetime.date(past)
yesterday = datetime.now() - timedelta(days=10)
yesterday=datetime.date(yesterday)
from threading import Thread
from time import sleep
from datetime import datetime, timedelta
import pdfCreatorReportes as pdfC
import uf
import numpy as np
from sklearn import datasets, linear_model
import sendmail
import tasadorbot2 as tb2
import pubPortalExiste
import math
import csv
from csvWriter import writeCsv
from csvWriter import writeCsvCanje
import bot1 as tgbot
import googleMapApi as gm
import datetime


fechahoy = datetime.datetime.now()
fechahoy=str(fechahoy.year)+'-'+str(fechahoy.month)+'-'+str(fechahoy.day)
uf1=uf.getUf()

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


def estaciones():
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='metro')
    cur = mariadb_connection.cursor()
    sql = "SELECT * FROM estaciones"
    cur.execute(sql)
    tupla = cur.fetchall()
    return tupla

def rentabilidad(prop):
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT rentabilidad FROM rentabilidades_portalinmobiliario WHERE prop="+str(prop)
    cur.execute(sql)
    rent = cur.fetchall()
    rent=rent[0]
    rent=rent[0]
    return rent

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

def from_portalinmobiliario_select(past,yesterday,preciomin,preciomax,utilmin,utilmax,totalmin,totalmax,latmin,latmax,
                                   lonmin,lonmax,dormitoriosmin,dormitoriosmax,banosmin,banosmax,estacionamientos,tipo,
                                   operacion,region,comuna1,comuna2,comuna3,comuna4,comuna5,comuna6,verboso=False):

        if verboso:
            print("----------------------")
            print("Seleccionando propiedades especificas de portal.")
        mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
        cur = mariadb_connection.cursor()

        sqlselect = "SELECT id2,fechapublicacion,fechascrap,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,lat,lon,estacionamientos,link,id FROM portalinmobiliario WHERE "

        sqlwhere="fechascrap>='"+str(yesterday)+"' AND "
        sql=sqlselect+sqlwhere

        sqlwhere="fechapublicacion>='"+str(past)+"' AND "
        sql=sql+sqlwhere

        sqlwhere="precio>="+str(preciomin)+" AND "
        sql=sql+sqlwhere

        sqlwhere="precio<="+str(preciomax)+" AND "
        sql=sql+sqlwhere

        sqlwhere="metrosmin>="+str(utilmin)+" AND "
        sql=sql+sqlwhere

        sqlwhere="metrosmin<="+str(utilmax)+" AND "
        sql=sql+sqlwhere

        sqlwhere="metrosmax>="+str(totalmin)+" AND "
        sql=sql+sqlwhere

        sqlwhere="metrosmax<="+str(totalmax)+" AND "
        sql=sql+sqlwhere

        sqlwhere="lat>="+str(latmin)+" AND "
        sql=sql+sqlwhere

        sqlwhere="lat<="+str(latmax)+" AND "
        sql=sql+sqlwhere

        sqlwhere="lon>="+str(lonmin)+" AND "
        sql=sql+sqlwhere

        sqlwhere="lon<="+str(lonmax)+" AND "
        sql=sql+sqlwhere

        sqlwhere="dormitorios>="+str(dormitoriosmin)+" AND "
        sql=sql+sqlwhere

        sqlwhere="dormitorios<="+str(dormitoriosmax)+" AND "
        sql=sql+sqlwhere

        sqlwhere="banos>="+str(banosmin)+" AND "
        sql=sql+sqlwhere

        sqlwhere="banos<="+str(banosmax)+" AND "
        sql=sql+sqlwhere

        sqlwhere="estacionamientos>="+str(estacionamientos)+" AND "
        sql=sql+sqlwhere


        sqlwhere="tipo LIKE '%" + str(tipo) + "%' AND "
        sql=sql+sqlwhere

        sqlwhere="operacion LIKE '%"+str(operacion)+"%' AND "
        sql=sql+sqlwhere

        sqlwhere="region LIKE '%"+str(region)+"%' AND "
        sql=sql+sqlwhere

        sqlwhere="(link LIKE '%" + comuna1 + "%' or link LIKE '%"+ comuna2 + "%' or link LIKE '%"+ comuna3 + "%' or link LIKE '%"+ comuna4 + "%' or link LIKE '%"+ comuna5 +"%' or link LIKE '%"+ comuna6 +"%')"
        sql=sql+sqlwhere

        print("Consulta:")
        print(sql)
        cur.execute(sql)
        tupla = cur.fetchall()
        print("Datos de consulta especifica de portal listos")
        print("----------------------")
        return tupla


def from_portalinmobiliario_select_canje(past, yesterday, preciomin, preciomax, utilmin, utilmax, totalmin, totalmax, latmin,
                                   latmax,
                                   lonmin, lonmax, dormitoriosmin, dormitoriosmax, banosmin, banosmax, estacionamientos,
                                   tipo,
                                   operacion, region, comuna1, comuna2, comuna3, comuna4, comuna5, comuna6,
                                   verboso=False):
    if verboso:
        print("----------------------")
        print("Seleccionando propiedades especificas de portal.")
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()

    sqlselect = "SELECT id2,fechapublicacion,fechascrap,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,lat,lon,estacionamientos,link,mail,esDueno FROM portalinmobiliario INNER JOIN duenos WHERE "

    sqlwhere = "id2=idProp" + " AND "
    sql = sqlselect + sqlwhere

    sqlwhere = "fechascrap>='" + str(yesterday) + "' AND "
    sql = sql + sqlwhere

    sqlwhere = "fechapublicacion>='" + str(past) + "' AND "
    sql = sql + sqlwhere

    sqlwhere = "precio>=" + str(preciomin) + " AND "
    sql = sql + sqlwhere

    sqlwhere = "precio<=" + str(preciomax) + " AND "
    sql = sql + sqlwhere

    sqlwhere = "metrosmin>=" + str(utilmin) + " AND "
    sql = sql + sqlwhere

    sqlwhere = "metrosmin<=" + str(utilmax) + " AND "
    sql = sql + sqlwhere

    sqlwhere = "metrosmax>=" + str(totalmin) + " AND "
    sql = sql + sqlwhere

    sqlwhere = "metrosmax<=" + str(totalmax) + " AND "
    sql = sql + sqlwhere

    sqlwhere = "lat>=" + str(latmin) + " AND "
    sql = sql + sqlwhere

    sqlwhere = "lat<=" + str(latmax) + " AND "
    sql = sql + sqlwhere

    sqlwhere = "lon>=" + str(lonmin) + " AND "
    sql = sql + sqlwhere

    sqlwhere = "lon<=" + str(lonmax) + " AND "
    sql = sql + sqlwhere

    sqlwhere = "dormitorios>=" + str(dormitoriosmin) + " AND "
    sql = sql + sqlwhere

    sqlwhere = "dormitorios<=" + str(dormitoriosmax) + " AND "
    sql = sql + sqlwhere

    sqlwhere = "banos>=" + str(banosmin) + " AND "
    sql = sql + sqlwhere

    sqlwhere = "banos<=" + str(banosmax) + " AND "
    sql = sql + sqlwhere

    sqlwhere = "estacionamientos>=" + str(estacionamientos) + " AND "
    sql = sql + sqlwhere

    sqlwhere = "tipo LIKE '%" + str(tipo) + "%' AND "
    sql = sql + sqlwhere

    sqlwhere = "operacion LIKE '%" + str(operacion) + "%' AND "
    sql = sql + sqlwhere

    sqlwhere = "region LIKE '%" + str(region) + "%' AND "
    sql = sql + sqlwhere

    sqlwhere = "(link LIKE '%" + comuna1 + "%' or link LIKE '%" + comuna2 + "%' or link LIKE '%" + comuna3 + "%' or link LIKE '%" + comuna4 + "%' or link LIKE '%" + comuna5 + "%' or link LIKE '%" + comuna6 + "%')"
    sql = sql + sqlwhere

    print("Consulta:")
    print(sql)
    cur.execute(sql)
    tupla = cur.fetchall()
    print("Datos de consulta especifica de portal listos")
    print("----------------------")
    return tupla

def clientes():
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT * FROM clientes"
    cur.execute(sql)
    tupla = cur.fetchall()
    if tupla[38] is None:
        tupla[38]=8
    return tupla

def insertarClientes_Propiedades(resultado):
    sql = """INSERT INTO clientes_propiedades(uni,cliente,prop)
             VALUES(%s,%s,%s) ON DUPLICATE KEY UPDATE prop=%s"""

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')

    cur = mariadb_connection.cursor()
    cur.execute(sql, (resultado))
    mariadb_connection.commit()
    mariadb_connection.close()

def actualizarActividad(cliente):

    sql = "UPDATE clientes SET activo=2 WHERE id="+str(cliente)

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')

    cur = mariadb_connection.cursor()
    cur.execute(sql)
    mariadb_connection.commit()
    mariadb_connection.close()

def precio_from_portalinmobiliario(id2):
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT precio,metrosmin,metrosmax,lat,lon,dormitorios,banos FROM portalinmobiliario WHERE id2='"+str(id2)+"'"
    cur.execute(sql)
    precio = cur.fetchall()

    return precio

def calcularDistanciaV(i,data):

    distanciat0=[]
    distanciat1=[]
    distanciat2_1=[]
    distanciat2_2=[]
    distanciat3_1=[]
    distanciat3_2=[]
    distanciat4_1=[]
    distanciat4_2=[]
    k0=[0]*14
    k1=[0]*14
    k21=[0]*14
    k22=[0]*14
    k31=[0]*14
    k32=[0]*14
    k41=[0]*14
    k42=[0]*14

    for j in data:
        # i3=op, i4=tipo, i5=precio, i6=dorms, i7=baños, i12= estacionamientos i8=util, i9=total
        if (j[1]>past) and ("venta"==j[3]) and (i[4]==j[4]) and (j!=i):
            lat1=i[10]
            long1=i[11]
            lat2=j[10]
            long2=j[11]
            r=6371000
            c=pi/180
            distance= 2*r*asin(sqrt(sin(c*(lat2-lat1)/2)**2 + cos(c*lat1)*cos(c*lat2)*sin(c*(long2-long1)/2)**2))

            #T0
            if (distance < 1000) and (abs(i[8]/j[8]-1)<0.1) and (abs(i[9]/j[9]-1)<0.2) and (i[6]==j[6]) and (i[7]==j[7]) and (i[12]==j[12]) and ((k0[5]!=j[5]) or (k0[8]!=j[8]) or (k0[9]!=j[9]) or (k0[6]!=j[6]) or (k0[7]!=j[7]) or (k0[12]!=j[12])):
                d=sqrt(distance*distance+(100*abs(i[8]-j[8])*(100*abs(i[8]-j[8])))+(100*abs(i[9]-j[9])*(100*abs(i[9]-j[9]))))
                j.append(d)
                distanciat0.append(j)
                k0=j
                j=j[:-1]


            #T1 REVISAR
            if (distance < 1000) and (abs(i[8]/j[8]-1)<0.2) and (abs(i[9]/j[9]-1)<0.4) and (i[6]==j[6]) and (i[7]==j[7]) and (i[12]==j[12]) and ((k1[5]!=j[5]) or (k1[8]!=j[8]) or (k1[9]!=j[9]) or (k1[6]!=j[6]) or (k1[7]!=j[7]) or (k1[12]!=j[12])) :
                d=sqrt(distance*distance+(100*abs(i[8]-j[8])*(100*abs(i[8]-j[8])))+(100*abs(i[9]-j[9])*(100*abs(i[9]-j[9]))))
                j.append(d)
                distanciat1.append(j)
                j=j[:-1]
                k1=j

            #T2.1
            if (distance < 1000) and (abs(i[8]/j[8]-1)<0.2) and (abs(i[9]/j[9]-1)<0.4) and (i[6]==j[6]) and (i[7]==j[7]) and (int(i[12])>=(int(j[12])-1) and (int(i[12])<=(int(j[12])+1))) and ((k21[5]!=j[5]) or (k21[8]!=j[8]) or (k21[9]!=j[9]) or (k21[6]!=j[6]) or (k21[7]!=j[7]) or (k21[12]!=j[12])) :
                d=sqrt(distance*distance+(100*abs(i[8]-j[8])*(100*abs(i[8]-j[8])))+(100*abs(i[9]-j[9])*(100*abs(i[9]-j[9]))))
                j.append(d)
                distanciat2_1.append(j)
                j=j[:-1]
                k21=j

            #T2.2
            if (distance < 1000) and (abs(i[8]/j[8]-1)<0.2) and (abs(i[9]/j[9]-1)<0.4) and (i[6]==j[6]) and (i[7]==j[7]) and ((k22[5]!=j[5]) or (k22[8]!=j[8]) or (k22[9]!=j[9]) or (k22[6]!=j[6]) or (k22[7]!=j[7]) or (k22[12]!=j[12])) :
                d=sqrt(distance*distance+(100*abs(i[8]-j[8])*(100*abs(i[8]-j[8])))+(100*abs(i[9]-j[9])*(100*abs(i[9]-j[9]))))
                j.append(d)
                distanciat2_2.append(j)
                j=j[:-1]
                k22=j

            #T3.1
            if (distance < 1000) and (abs(i[8]/j[8]-1)<0.2) and (abs(i[9]/j[9]-1)<0.4) and (int(i[6])>=(int(j[6])-1) and (int(i[6])<=(int(j[6])+1))) and (i[7]==j[7]) and ((k31[5]!=j[5]) or (k31[8]!=j[8]) or (k31[9]!=j[9]) or (k31[6]!=j[6]) or (k31[7]!=j[7]) or (k31[12]!=j[12])) :
                d=sqrt(distance*distance+(100*abs(i[8]-j[8])*(100*abs(i[8]-j[8])))+(100*abs(i[9]-j[9])*(100*abs(i[9]-j[9]))))
                j.append(d)
                distanciat3_1.append(j)
                j=j[:-1]
                k31=j

            #T3.2
            if (distance < 1000) and (abs(i[8]/j[8]-1)<0.2) and (abs(i[9]/j[9]-1)<0.4) and (i[7]==j[7]) and ((k32[5]!=j[5]) or (k32[8]!=j[8]) or (k32[9]!=j[9]) or (k32[6]!=j[6]) or (k32[7]!=j[7]) or (k32[12]!=j[12])):
                d=sqrt(distance*distance+(100*abs(i[8]-j[8])*(100*abs(i[8]-j[8])))+(100*abs(i[9]-j[9])*(100*abs(i[9]-j[9]))))
                j.append(d)
                distanciat3_2.append(j)
                j=j[:-1]
                k32=j

            #T4.1
            if (distance < 1000) and (abs(i[8]/j[8]-1)<0.2) and (abs(i[9]/j[9]-1)<0.4) and (int(i[7])>=(int(j[7])-1) and (int(i[7])<=(int(j[7])+1))) and ((k41[5]!=j[5]) or (k41[8]!=j[8]) or (k41[9]!=j[9]) or (k41[6]!=j[6]) or (k41[7]!=j[7]) or (k41[12]!=j[12])):
                d=sqrt(distance*distance+(100*abs(i[8]-j[8])*(100*abs(i[8]-j[8])))+(100*abs(i[9]-j[9])*(100*abs(i[9]-j[9]))))
                j.append(d)
                distanciat4_1.append(j)
                j=j[:-1]
                k41=j

            #T4.2
            if (distance < 1000) and (abs(i[8]/j[8]-1)<0.2) and (abs(i[9]/j[9]-1)<0.4) and ((k42[5]!=j[5]) or (k42[8]!=j[8]) or (k42[9]!=j[9]) or (k42[6]!=j[6]) or (k42[7]!=j[7]) or (k42[12]!=j[12])):
                d=sqrt(distance*distance+(100*abs(i[8]-j[8])*(100*abs(i[8]-j[8])))+(100*abs(i[9]-j[9])*(100*abs(i[9]-j[9]))))
                j.append(d)
                distanciat4_2.append(j)
                j=j[:-1]
                k42=j

    t_actual="0"
    cota=5
    for cot in range (1,6):
        if len(distanciat0)>=cota:
            distancia=distanciat0

        elif len(distanciat1)>=cota:
            distancia=distanciat1
            t_actual="1"
        elif len(distanciat2_1)>=cota:
            distancia=distanciat2_1
            t_actual="2.1"
        elif len(distanciat2_2)>=cota:
            distancia=distanciat2_2
            t_actual="2.2"
        elif len(distanciat3_1)>=cota:
            distancia=distanciat3_1
            t_actual="3.1"
        elif len(distanciat3_2)>=cota:
            distancia=distanciat3_2
            t_actual="3.2"
        elif len(distanciat4_1)>=cota:
            distancia=distanciat4_1
            t_actual="4.1"
        elif len(distanciat4_2)>=cota:
            distancia=distanciat4_2
            t_actual="4.2"

        else:
            return

        distancias=sorted(distancia,key=lambda x:x[14])
        try:
            distancias=distancias[:40]
        except:
            distancias=distancia
        #print("propiedades encontradas "+str(len(distancias)))
        #print ("nivel de confianza: "+str(t_actual))
        #for link in [x[13] for x in distancias]:
             #print (link)


        # i3=op, i4=tipo, i5=precio, i6=dorms, i7=baños, i12= estacionamientos i8=util, i9=total

        y_train = []
        x_train = []
        for e in distancias:
            x_train.append([e[8],e[9],e[6],e[7],e[12]])
            y_train.append(e[5])

        #y2_train=[]
        #y2_train.append(y_train)
        #y_train=y2_train
        x_train=np.array(x_train)
        y_train=np.array(y_train)
        #x_train=np.transpose(x_train)


        #print (x_train)
        #print(x_train.shape)
        #print (y_train)
        #print(y_train.shape)

        # Create linear regression object
        regr = linear_model.LinearRegression()

        # Train the model using the training sets
        regr.fit(x_train, y_train)
        #try:
         #   print("constante: "+str(regr.intercept_)+" coeficientes: " +str(regr.coef_))
        #except:
         #   print("unable to print coef")
        x_test = [i[8],i[9],i[6],i[7],i[12]]
        x_test=np.array(x_test)
        x_test=np.transpose(x_test)
        # Make predictions using the testing set

        price=regr.intercept_
        c=0
        for coef in regr.coef_:
            price=price+coef*x_test[c]
            c=c+1
        #print(price)
        cota=len(distancias)+1
    #print("y_pred = " + str(y_pred))
    # The coefficients
    #print('Coefficients: \n', regr.coef_)


    try:
        return price
    except:
        return -1

def calcularDistanciaA(i,data):

    distanciat0=[]
    distanciat1=[]
    distanciat2_1=[]
    distanciat2_2=[]
    distanciat3_1=[]
    distanciat3_2=[]
    distanciat4_1=[]
    distanciat4_2=[]
    k0=[0]*14
    k1=[0]*14
    k21=[0]*14
    k22=[0]*14
    k31=[0]*14
    k32=[0]*14
    k41=[0]*14
    k42=[0]*14

    for j in data:
        # i3=op, i4=tipo, i5=precio, i6=dorms, i7=baños, i12= estacionamientos i8=util, i9=total
        if (j[1]>past) and ("arriendo"==j[3]) and (i[4]==j[4]) and (j!=i):
            lat1=i[10]
            long1=i[11]
            lat2=j[10]
            long2=j[11]
            r=6371000
            c=pi/180
            distance= 2*r*asin(sqrt(sin(c*(lat2-lat1)/2)**2 + cos(c*lat1)*cos(c*lat2)*sin(c*(long2-long1)/2)**2))

            #T0
            if (distance < 1000) and (abs(i[8]/j[8]-1)<0.1) and (abs(i[9]/j[9]-1)<0.2) and (i[6]==j[6]) and (i[7]==j[7]) and (i[12]==j[12]) and ((k0[5]!=j[5]) or (k0[8]!=j[8]) or (k0[9]!=j[9]) or (k0[6]!=j[6]) or (k0[7]!=j[7]) or (k0[12]!=j[12])):
                d=sqrt(distance*distance+(100*abs(i[8]-j[8])*(100*abs(i[8]-j[8])))+(100*abs(i[9]-j[9])*(100*abs(i[9]-j[9]))))
                j.append(d)
                distanciat0.append(j)
                k0=j
                j=j[:-1]


            #T1 REVISAR
            if (distance < 1000) and (abs(i[8]/j[8]-1)<0.2) and (abs(i[9]/j[9]-1)<0.4) and (i[6]==j[6]) and (i[7]==j[7]) and (i[12]==j[12]) and ((k1[5]!=j[5]) or (k1[8]!=j[8]) or (k1[9]!=j[9]) or (k1[6]!=j[6]) or (k1[7]!=j[7]) or (k1[12]!=j[12])) :
                d=sqrt(distance*distance+(100*abs(i[8]-j[8])*(100*abs(i[8]-j[8])))+(100*abs(i[9]-j[9])*(100*abs(i[9]-j[9]))))
                j.append(d)
                distanciat1.append(j)
                j=j[:-1]
                k1=j

            #T2.1
            if (distance < 1000) and (abs(i[8]/j[8]-1)<0.2) and (abs(i[9]/j[9]-1)<0.4) and (i[6]==j[6]) and (i[7]==j[7]) and (int(i[12])>=(int(j[12])-1) and (int(i[12])<=(int(j[12])+1))) and ((k21[5]!=j[5]) or (k21[8]!=j[8]) or (k21[9]!=j[9]) or (k21[6]!=j[6]) or (k21[7]!=j[7]) or (k21[12]!=j[12])) :
                d=sqrt(distance*distance+(100*abs(i[8]-j[8])*(100*abs(i[8]-j[8])))+(100*abs(i[9]-j[9])*(100*abs(i[9]-j[9]))))
                j.append(d)
                distanciat2_1.append(j)
                j=j[:-1]
                k21=j

            #T2.2
            if (distance < 1000) and (abs(i[8]/j[8]-1)<0.2) and (abs(i[9]/j[9]-1)<0.4) and (i[6]==j[6]) and (i[7]==j[7]) and ((k22[5]!=j[5]) or (k22[8]!=j[8]) or (k22[9]!=j[9]) or (k22[6]!=j[6]) or (k22[7]!=j[7]) or (k22[12]!=j[12])) :
                d=sqrt(distance*distance+(100*abs(i[8]-j[8])*(100*abs(i[8]-j[8])))+(100*abs(i[9]-j[9])*(100*abs(i[9]-j[9]))))
                j.append(d)
                distanciat2_2.append(j)
                j=j[:-1]
                k22=j

            #T3.1
            if (distance < 1000) and (abs(i[8]/j[8]-1)<0.2) and (abs(i[9]/j[9]-1)<0.4) and (int(i[6])>=(int(j[6])-1) and (int(i[6])<=(int(j[6])+1))) and (i[7]==j[7]) and ((k31[5]!=j[5]) or (k31[8]!=j[8]) or (k31[9]!=j[9]) or (k31[6]!=j[6]) or (k31[7]!=j[7]) or (k31[12]!=j[12])) :
                d=sqrt(distance*distance+(100*abs(i[8]-j[8])*(100*abs(i[8]-j[8])))+(100*abs(i[9]-j[9])*(100*abs(i[9]-j[9]))))
                j.append(d)
                distanciat3_1.append(j)
                j=j[:-1]
                k31=j

            #T3.2
            if (distance < 1000) and (abs(i[8]/j[8]-1)<0.2) and (abs(i[9]/j[9]-1)<0.4) and (i[7]==j[7]) and ((k32[5]!=j[5]) or (k32[8]!=j[8]) or (k32[9]!=j[9]) or (k32[6]!=j[6]) or (k32[7]!=j[7]) or (k32[12]!=j[12])):
                d=sqrt(distance*distance+(100*abs(i[8]-j[8])*(100*abs(i[8]-j[8])))+(100*abs(i[9]-j[9])*(100*abs(i[9]-j[9]))))
                j.append(d)
                distanciat3_2.append(j)
                j=j[:-1]
                k32=j

            #T4.1
            if (distance < 1000) and (abs(i[8]/j[8]-1)<0.2) and (abs(i[9]/j[9]-1)<0.4) and (int(i[7])>=(int(j[7])-1) and (int(i[7])<=(int(j[7])+1))) and ((k41[5]!=j[5]) or (k41[8]!=j[8]) or (k41[9]!=j[9]) or (k41[6]!=j[6]) or (k41[7]!=j[7]) or (k41[12]!=j[12])):
                d=sqrt(distance*distance+(100*abs(i[8]-j[8])*(100*abs(i[8]-j[8])))+(100*abs(i[9]-j[9])*(100*abs(i[9]-j[9]))))
                j.append(d)
                distanciat4_1.append(j)
                j=j[:-1]
                k41=j

            #T4.2
            if (distance < 1000) and (abs(i[8]/j[8]-1)<0.2) and (abs(i[9]/j[9]-1)<0.4) and ((k42[5]!=j[5]) or (k42[8]!=j[8]) or (k42[9]!=j[9]) or (k42[6]!=j[6]) or (k42[7]!=j[7]) or (k42[12]!=j[12])):
                d=sqrt(distance*distance+(100*abs(i[8]-j[8])*(100*abs(i[8]-j[8])))+(100*abs(i[9]-j[9])*(100*abs(i[9]-j[9]))))
                j.append(d)
                distanciat4_2.append(j)
                j=j[:-1]
                k42=j

    t_actual="0"
    cota=5
    for cot in range (1,6):
        if len(distanciat0)>=cota:
            distancia=distanciat0

        elif len(distanciat1)>=cota:
            distancia=distanciat1
            t_actual="1"
        elif len(distanciat2_1)>=cota:
            distancia=distanciat2_1
            t_actual="2.1"
        elif len(distanciat2_2)>=cota:
            distancia=distanciat2_2
            t_actual="2.2"
        elif len(distanciat3_1)>=cota:
            distancia=distanciat3_1
            t_actual="3.1"
        elif len(distanciat3_2)>=cota:
            distancia=distanciat3_2
            t_actual="3.2"
        elif len(distanciat4_1)>=cota:
            distancia=distanciat4_1
            t_actual="4.1"
        elif len(distanciat4_2)>=cota:
            distancia=distanciat4_2
            t_actual="4.2"

        else:
            return

        distancias=sorted(distancia,key=lambda x:x[14])
        try:
            distancias=distancias[:40]
        except:
            distancias=distancia
        #print("propiedades encontradas "+str(len(distancias)))
        #print ("nivel de confianza: "+str(t_actual))
        # for link in [x[13] for x in distancias]:
        #     print (link)

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


        # i3=op, i4=tipo, i5=precio, i6=dorms, i7=baños, i12= estacionamientos i8=util, i9=total

        y_train = []
        x_train = []
        for e in distancias:
            x_train.append([e[8],e[9],e[6],e[7],e[12]])
            y_train.append(e[5])

        #y2_train=[]
        #y2_train.append(y_train)
        #y_train=y2_train
        x_train=np.array(x_train)
        y_train=np.array(y_train)
        #x_train=np.transpose(x_train)


        #print (x_train)
        #print(x_train.shape)
        #print (y_train)
        #print(y_train.shape)

        # Create linear regression object
        regr = linear_model.LinearRegression()

        # Train the model using the training sets
        regr.fit(x_train, y_train)
        #try:
         #   print("constante: "+str(regr.intercept_)+" coeficientes: " +str(regr.coef_))
        #except:
         #   print("unable to print coef")
        x_test = [i[8],i[9],i[6],i[7],i[12]]
        x_test=np.array(x_test)
        x_test=np.transpose(x_test)
        # Make predictions using the testing set

        price=regr.intercept_
        c=0
        for coef in regr.coef_:
            price=price+coef*x_test[c]
            c=c+1
        price=price
        #print(price)
        cota=len(distancias)+1
    #print("y_pred = " + str(y_pred))
    # The coefficients
    #print('Coefficients: \n', regr.coef_)

    try:
        cosa=mean(prices)
        precio=cosa[0]
        std=cosa[1]
        preciomin=precio-std
        preciomax=precio+std
        return price
    except:
        return -1

def from_portalinmobiliario(tipo,region,verboso=False):
    if verboso:
        print("----------------------")
        print("Extrayendo propiedades de portal.")
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT id2,fechapublicacion,fechascrap,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,lat,lon,estacionamientos,link FROM portalinmobiliario WHERE tipo='"+str(tipo)+"' and region='"+str(region)+"'"
    if verboso:
        print("Consulta:")
        print(sql)
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

    if verboso:
        print("Data de portal Lista.")
        print("----------------------")
    return data

def main():
    data=clientes()
    for i in data:

        print("[GeneradorReportes] Buscando propiedades para el cliente "+str(i[1]))
        if i[34]==0:
            continue
        elif i[34]==1:
            activo=2
            #actualizarActividad(i[0])
        else:
            past = datetime.now() - timedelta(days=1)


        nombreCliente=str(i[1])
        mail = str(i[3])

        preciomin=float(i[5])
        preciomax=float(i[6])
        utilmin=float(i[7])
        utilmax=float(i[8])
        totalmin=float(i[9])
        totalmax=float(i[10])
        latmin=float(i[11])
        latmax=float(i[12])
        lonmin=float(i[13])
        lonmax=float(i[14])
        dormitoriosmin=float(i[15])
        dormitoriosmax=float(i[16])
        banosmin=float(i[17])
        banosmax=float(i[18])

        rentmin=float(i[35])
        estacionamientos=float(i[19])

        if i[38] is not None:
            confmin=int(i[38])
        else:
            confmin=i[38]

        tipo=i[20]
        operacion=i[21]
        region=i[23]
        comuna1=i[24]
        if comuna1 is None:
            comuna1=""
        comuna2=i[25]
        if comuna2 is None:
            comuna2="abcdefghij"
        comuna3=i[26]
        if comuna3 is None:
            comuna3="abcdefghij"
        metrodistance=i[30]
        linea1=i[31]
        if linea1 is None:
            linea1="abcdefghij"
        linea2=i[32]
        if linea2 is None:
            linea2="abcdefghij"
        linea3=i[33]
        if linea3 is None:
            linea3="abcdefghij"

        comuna4=i[27]
        if comuna4 is None:
            comuna4="abcdefghij"
        comuna5=i[28]
        if comuna5 is None:
            comuna5="abcdefghij"
        comuna6=i[29]
        if comuna6 is None:
            comuna6="abcdefghij"

        prioridad = i[37]
        flagMail = int(i[36])


        generarReporte(preciomin,preciomax,utilmin,utilmax,totalmin,totalmax,latmin,latmax,lonmin,lonmax,dormitoriosmin,
                       dormitoriosmax,banosmin,banosmax,confmin,rentmin, estacionamientos,metrodistance,tipo,operacion,region,comuna1,comuna2,
                       comuna3,comuna4,comuna5,comuna6,prioridad,flagMail,mail,nombreCliente,True)

def generarReporte(preciomin, preciomax, utilmin, utilmax, totalmin, totalmax, latmin, latmax, lonmin, lonmax,
                       dormitoriosmin,
                       dormitoriosmax, banosmin, banosmax, confmin, rentmin, estacionamientos, metrodistance, tipo,
                       operacion, region, comuna1, comuna2,
                       comuna3, comuna4, comuna5, comuna6,prioridad, flagMail, mail,nombreCliente,verboso,
                   enviarActualizacionTG=False,chat="",URL=""):

    preciomin=int(preciomin)
    preciomax=int(preciomax)
    utilmin=int(utilmin)
    utilmax=int(utilmax)
    totalmin=int(totalmin)
    totalmax=int(totalmax)
    latmin=float(latmin)
    latmax=float(latmax)
    lonmin=float(lonmin)
    lonmax=float(lonmax)
    dormitoriosmin=int(dormitoriosmin)
    dormitoriosmax=int(dormitoriosmax)
    banosmax=int(banosmax)
    confmin=int(confmin)
    rentmin=float(rentmin)
    estacionamientos=int(estacionamientos)
    metrodistance=int(metrodistance)
    tipo=str(tipo)
    operacion=str(operacion)
    region=str(region)
    comuna1=str(comuna1)
    comuna2=str(comuna2)
    comuna3=str(comuna3)
    comuna4=str(comuna4)
    comuna5=str(comuna5)
    comuna6=str(comuna6)
    prioridad=str(prioridad)
    flagMail=int(flagMail)
    mail=str(mail)
    nombreCliente=str(nombreCliente)

    props=from_portalinmobiliario(tipo,region,verboso)
    propiedades=from_portalinmobiliario_select(past,yesterday,preciomin,preciomax,utilmin,utilmax,totalmin,totalmax,
                                               latmin,latmax,lonmin,lonmax,dormitoriosmin,dormitoriosmax,banosmin,
                                               banosmax,estacionamientos,tipo,operacion,region,comuna1,comuna2,comuna3,
                                               comuna4,comuna5,comuna6,verboso)
    resultado = []
    estaciones1=estaciones()
    if verboso:
        print("[GeneradorReportes] total propiedades encontradas: "+str(len(propiedades)))

    if enviarActualizacionTG:
        tgbot.send_message("[GeneradorReportes] Encontradas " + str(len(propiedades)) + " propiedades.", chat, URL)

    count=0

    porc25 = int(len(propiedades)/4)
    porc50 = int(len(propiedades)/2)
    porc75 = porc25+porc50

    for i,prop in enumerate(propiedades):

        count=count+1
        if verboso:
            print("GeneradorReportes] " + str(count)+"/"+str(len(propiedades)))

        if enviarActualizacionTG:
            if porc25!=0 and count>porc25 and count < porc50:
                tgbot.send_message("[GeneradorReportes] 25 porciento filtrado. ", chat, URL)
                porc25 = 0
            elif porc50 != 0 and count > porc50 and count < porc75:
                tgbot.send_message("[GeneradorReportes] 50 porciento filtrado. ", chat, URL)
                porc50 = 0
            elif porc75 != 0 and count > porc75:
                tgbot.send_message("[GeneradorReportes] 75 porciento filtrado. ", chat, URL)
                porc75 = 0

        estaciones2=[]
        for e in estaciones1:
            subestacion=[]
            late=e[3]
            lone=e[4]
            lat1=prop[10]
            long1=prop[11]
            r=6371000
            c=pi/180
            distance= 2*r*asin(sqrt(sin(c*(late-lat1)/2)**2 + cos(c*lat1)*cos(c*late)*sin(c*(lone-long1)/2)**2))
            subestacion.append(e[1])
            subestacion.append(e[2])
            subestacion.append(distance)
            estaciones2.append(subestacion)
        estaciones2=sorted(estaciones2,key=lambda x:x[2])
        estacioncercana=estaciones2[0]

        if metrodistance != None:
            if estacioncercana[2]>float(metrodistance):
                continue


        subresultado=[]
        subresultado.append(int(prop[5]))
        subresultado.append(int(prop[8]))
        subresultado.append(int(prop[9]))
        subresultado.append(int(prop[6]))
        subresultado.append(int(prop[7]))
        subresultado.append(int(prop[12]))
        auxestacion="("+str(estacioncercana[0])+") "+str(estacioncercana[1])
        subresultado.append(auxestacion)
        subresultado.append(estacioncercana[2])
        link=prop[13]
        link=link.split('/')
        comuna=link[5]

        rentaPromedio=rentaPProm(prop[4],int(prop[6]),int(prop[7]),int(prop[12]),comuna)
        if (rentaPromedio<=0):
            continue

        if verboso:
            print("[GeneradorReportes] renta promedio para la comuna de: "+str(comuna)+" para propiedades tipo "+str(tipo)+" de "+str(int(prop[6]))+" dormitorios, "+str(int(prop[7]))+" baños , y "+str(int(prop[12]))+" estacionamientos, es de: "+str(rentaPromedio))
        if (operacion=="venta"):

            tasacionVenta=tb2.calcularTasacionData("venta",prop[4],prop[10],prop[11],prop[8],prop[9],prop[6],prop[7],prop[12],props)

            tasacionArriendo=tb2.calcularTasacionData("arriendo",prop[4],prop[10],prop[11],prop[8],prop[9],prop[6],prop[7],prop[12],props)

            precioV=tasacionVenta[0]*uf.getUf()

            try:
                conftasacion=tasacionVenta[5]
            except:
                if verboso:
                    print("[GeneradorReportes] " + str(tasacionVenta))
                continue

            if confmin is not None:
                if confmin<conftasacion:
                    continue

            precioA=tasacionArriendo[0]


            if precioV is None or precioV<0.1:
                if verboso:
                    print("[GeneradorReportes] no hay precio predicho")

                continue


            rentaV=((precioV-prop[5])/prop[5])
            # if rentaV<rentmin or rentaV>1:
            #     continue


            if rentaV<rentmin and (prioridad=="venta"):
                if verboso:
                    print("[GeneradorReportes] renta de venta muy baja")
                continue

            if rentaV<rentmin and (prioridad!="venta") and (prioridad!="arriendo"):
                if verboso:
                    print("[GeneradorReportes] renta de venta muy baja")
                continue

            if precioA is None or precioA<0.01:
                if verboso:
                    print("[GeneradorReportes] no existe precio de arriendo")
                continue


            rentaA=(precioA*12/prop[5])
            rentaPP=(precioA*12/precioV)
            if verboso:
                print("[GeneradorReportes] rentapp: "+str(rentaPP))
            if rentaA>0.2:
                if verboso:
                    print("[GeneradorReportes] renta de arriendo muy alta")
                continue

            if rentaPP<rentaPromedio:
                if verboso:
                    print("[GeneradorReportes] renta pp muy baja, recalculando precio")
                precioV=precioA*12/rentaPromedio
                rentaV=((precioV-prop[5])/prop[5])
                rentaPP=(precioA*12/precioV)
                if verboso:
                    print("[GeneradorReportes] rentapp: "+str(rentaPP))

            if rentaV<rentmin and (prioridad=="venta"):
                if verboso:
                    print("[GeneradorReportes] renta de venta muy baja")
                continue

            if rentaV<rentmin and (prioridad!="venta") and (prioridad!="arriendo"):
                if verboso:
                    print("[GeneradorReportes] renta de venta muy baja")
                continue

            if rentaPP>0.15:

                if verboso:
                    print("[GeneradorReportes] renta pp muy alta, recalculando precio")
                precioV=precioA*12/0.15
                rentaV=((precioV-prop[5])/prop[5])

            if rentaA<0:
                if verboso:
                    print("[GeneradorReportes] renta de arriendo muy baja")
                continue

            if rentaA<rentmin and (prioridad=="arriendo"):
                if verboso:
                    print("[GeneradorReportes] renta de arriendo mas baja que minima")
                continue
            subresultado.append(precioV)
            subresultado.append(float(rentaV))
            subresultado.append(precioA)
            subresultado.append(float(rentaA))
            if verboso:
                print("[GeneradorReportes] depto encontrado para "+nombreCliente)

        else:

            tasacionArriendo=tb2.calcularTasacionData("arriendo",prop[4],prop[10],prop[11],prop[8],prop[9],prop[6],prop[7],prop[12],props)

            precioA=tasacionArriendo[0]

            if precioA is None:
                continue

            subresultado.append(precioA)
            rentaA=((precioA-prop[5])/prop[5])
            if verboso:
                print("[GeneradorReportes] arriendo real: "+str(prop[5]))
            if verboso:
                print("[GeneradorReportes] arriendo predicho: "+str(precioA))
            if verboso:
                print("[GeneradorReportes] rentabildiad: "+str(rentaA))
            if rentaA>1:
                continue

            if rentaA<rentmin and (prioridad=="arriendo"):
                continue

            subresultado.append(float(rentaA))

        if not pubPortalExiste.publicacionExiste(prop[13]):
            if verboso:
                print("[GeneradorReportes] link no disponible")
            continue
        else:
            subresultado.append(prop[13])

        if verboso:
            print("[GeneradorReportes] depto encontrado para "+nombreCliente)
        resultado.append(subresultado)
        #print("sub appended")

    if enviarActualizacionTG:
        tgbot.send_message("[GeneradorReportes] 100 porciento filtrado.", chat, URL)

    if len(resultado)>0:
        if verboso:
            print("[GeneradorReportes] Generando Reporte para el cliente "+nombreCliente)

        if enviarActualizacionTG:
            tgbot.send_message("[GeneradorReportes] Generando reporte para cliente " + nombreCliente, chat, URL)

        if (prioridad=="arriendo"):
            resultado=sorted(resultado, key=lambda x:x[11],reverse=True)
        elif (prioridad=="venta"):
            resultado=sorted(resultado, key=lambda x:x[9],reverse=True)
        else:
            resultado=sorted(resultado, key=lambda x:x[0])


        if (operacion=="venta"):
            columnNames=["Precio","Útil","Tot","D","B","E","Metro","Dist-est.","P.P","Rent.V","Arriendo","Rent.A","Link"]
        else:
            columnNames=["Precio","Útil","Tot","D","B","E","Metro","Dist-est.","Arriendo","Rent.A","Link"]


        today = datetime.today().strftime('%Y-%m-%d')
        nombreArchivo = nombreCliente + " propiedades usadas VA " +str(tipo)+" "+ today
        #FLAGMAIL=1 Si es reporte normal
        if (flagMail==1):
            pdfC.createPdfReport(nombreCliente, "reporte " + nombreArchivo + ".pdf", resultado, columnNames,operacion)
            sendmail.sendMail(mail,nombreCliente,("reporte "+str(nombreArchivo)+".pdf"))

            if verboso:
                print("[GeneradorReportes] Enviando reporte a cliente "+nombreCliente)

        #FLAGMAIL=2 Si es reporte interno
        elif (flagMail==2):
            writeCsv("reporte " + nombreArchivo+'.csv', resultado, columnNames, operacion)
            sendmail.sendMail(mail,nombreCliente,("reporte "+str(nombreArchivo)+".csv"))

            if verboso:
                print("[GeneradorReportes] Enviando reporte a cliente "+nombreCliente)
    else:
        if enviarActualizacionTG:
            tgbot.send_message("[GeneradorReportes] No se han encontrado propiedades para el cliente " + str(nombreCliente), chat, URL)
        if verboso:
            print("[GeneradorReportes] No se han encontrado propiedades para el cliente "+nombreCliente)

def generarReporteInterno(preciomin, preciomax, utilmin, utilmax, totalmin, totalmax, latmin, latmax, lonmin, lonmax,
                       dormitoriosmin,
                       dormitoriosmax, banosmin, banosmax, confmin, rentminventa, rentminarriendo, estacionamientos, metrodistance, tipo,
                       operacion, region, comuna1, comuna2,
                       comuna3, comuna4, comuna5, comuna6,prioridad, flagMail, mail,nombreCliente,verboso,
                          enviarActualizacionTG=False,chat="",URL=""):

    preciomin=float(preciomin)
    preciomax=float(preciomax)
    utilmin=int(utilmin)
    utilmax=int(utilmax)
    totalmin=int(totalmin)
    totalmax=int(totalmax)
    latmin=float(latmin)
    latmax=float(latmax)
    lonmin=float(lonmin)
    lonmax=float(lonmax)
    dormitoriosmin=int(dormitoriosmin)
    dormitoriosmax=int(dormitoriosmax)
    banosmax=int(banosmax)
    confmin=int(confmin)
    rentminventa=float(rentminventa)
    rentminarriendo=float(rentminarriendo)
    estacionamientos=int(estacionamientos)
    metrodistance=int(metrodistance)
    tipo=str(tipo)
    operacion=str(operacion)
    region=str(region)
    comuna1=str(comuna1)
    comuna2=str(comuna2)
    comuna3=str(comuna3)
    comuna4=str(comuna4)
    comuna5=str(comuna5)
    comuna6=str(comuna6)
    prioridad=str(prioridad)
    flagMail=int(flagMail)
    mail=str(mail)
    nombreCliente=str(nombreCliente)

    props=from_portalinmobiliario(tipo,region,verboso)
    propiedades=from_portalinmobiliario_select(past,yesterday,preciomin,preciomax,utilmin,utilmax,totalmin,totalmax,
                                               latmin,latmax,lonmin,lonmax,dormitoriosmin,dormitoriosmax,banosmin,
                                               banosmax,estacionamientos,tipo,operacion,region,comuna1,comuna2,comuna3,
                                               comuna4,comuna5,comuna6,verboso)
    resultado = []
    estaciones1=estaciones()
    if verboso:
        print("[GeneradorReportes] total propiedades encontradas: "+str(len(propiedades)))

    if enviarActualizacionTG:
        tgbot.send_message("[GeneradorReportes] Encontradas " + str(len(propiedades)) + " propiedades.", chat, URL)

    count=0

    porc25 = int(len(propiedades)/4)
    porc50 = int(len(propiedades)/2)
    porc75 = porc25+porc50

    for prop in propiedades:
        count=count+1

        if verboso:
            print("GeneradorReportes] " + str(count)+"/"+str(len(propiedades)))

        if enviarActualizacionTG:
            if porc25!=0 and count>porc25 and count < porc50:
                tgbot.send_message("[GeneradorReportes] 25 porciento filtrado. ", chat, URL)
                porc25 = 0
            elif porc50 != 0 and count > porc50 and count < porc75:
                tgbot.send_message("[GeneradorReportes] 50 porciento filtrado. ", chat, URL)
                porc50 = 0
            elif porc75 != 0 and count > porc75:
                tgbot.send_message("[GeneradorReportes] 75 porciento filtrado. ", chat, URL)
                porc75 = 0


        estaciones2=[]
        for e in estaciones1:
            subestacion=[]
            late=e[3]
            lone=e[4]
            lat1=prop[10]
            long1=prop[11]
            r=6371000
            c=pi/180
            distance= 2*r*asin(sqrt(sin(c*(late-lat1)/2)**2 + cos(c*lat1)*cos(c*late)*sin(c*(lone-long1)/2)**2))
            subestacion.append(e[1])
            subestacion.append(e[2])
            subestacion.append(distance)
            estaciones2.append(subestacion)
        estaciones2=sorted(estaciones2,key=lambda x:x[2])
        estacioncercana=estaciones2[0]

        if metrodistance != None:
            if estacioncercana[2]>float(metrodistance):
                continue


        subresultado=[]
        subresultado.append(int(prop[5]))
        subresultado.append(int(prop[8]))
        subresultado.append(int(prop[9]))
        subresultado.append(int(prop[6]))
        subresultado.append(int(prop[7]))
        subresultado.append(int(prop[12]))
        auxestacion="("+str(estacioncercana[0])+") "+str(estacioncercana[1])
        subresultado.append(auxestacion)
        subresultado.append(estacioncercana[2])
        link=prop[13]
        link=link.split('/')
        comuna=link[5]

        rentaPromedio=rentaPProm(prop[4],int(prop[6]),int(prop[7]),int(prop[12]),comuna)
        if (rentaPromedio<=0):
            continue

        if verboso:
            print("[GeneradorReportes] renta promedio para la comuna de: "+str(comuna)+" para propiedades tipo "+str(tipo)+" de "+str(int(prop[6]))+" dormitorios, "+str(int(prop[7]))+" baños , y "+str(int(prop[12]))+" estacionamientos, es de: "+str(rentaPromedio))
        if (operacion=="venta"):

            tasacionVenta=tb2.calcularTasacionData("venta",prop[4],prop[10],prop[11],prop[8],prop[9],prop[6],prop[7],prop[12],props)

            tasacionArriendo=tb2.calcularTasacionData("arriendo",prop[4],prop[10],prop[11],prop[8],prop[9],prop[6],prop[7],prop[12],props)

            precioV=tasacionVenta[0]*uf.getUf()

            try:
                conftasacion=tasacionVenta[5]
            except:
                if verboso:
                    print("[GeneradorReportes] " + str(tasacionVenta))
                continue

            if confmin is not None:
                if confmin<conftasacion:
                    continue

            precioA=tasacionArriendo[0]


            if precioV is None or precioV<0.1:
                if verboso:
                    print("[GeneradorReportes] no hay precio predicho")

                continue


            rentaV=((precioV-prop[5])/prop[5])
            # if rentaV<rentmin or rentaV>1:
            #     continue


            if rentaV<rentminventa:
                if verboso:
                    print("[GeneradorReportes] renta de venta muy baja")
                continue



            if precioA is None or precioA<0.01:
                if verboso:
                    print("[GeneradorReportes] no existe precio de arriendo")
                continue


            rentaA=(precioA*12/prop[5])
            rentaPP=(precioA*12/precioV)
            if verboso:
                print("[GeneradorReportes] rentapp: "+str(rentaPP))
            if rentaA>0.2:
                if verboso:
                    print("[GeneradorReportes] renta de arriendo muy alta")
                continue

            if rentaPP<rentaPromedio:
                if verboso:
                    print("[GeneradorReportes] renta pp muy baja, recalculando precio")
                precioV=precioA*12/rentaPromedio
                rentaV=((precioV-prop[5])/prop[5])
                rentaPP=(precioA*12/precioV)
                if verboso:
                    print("[GeneradorReportes] rentapp: "+str(rentaPP))

            if rentaV<rentminventa:
                if verboso:
                    print("[GeneradorReportes] renta de venta muy baja")
                continue



            if rentaPP>0.15:

                if verboso:
                    print("[GeneradorReportes] renta pp muy alta, recalculando precio")
                precioV=precioA*12/0.15
                rentaV=((precioV-prop[5])/prop[5])

            if rentaA<0:
                if verboso:
                    print("[GeneradorReportes] renta de arriendo muy baja")
                continue

            if rentaA<rentminarriendo:
                if verboso:
                    print("[GeneradorReportes] renta de arriendo mas baja que minima")
                continue
            subresultado.append(precioV)
            subresultado.append(float(rentaV))
            subresultado.append(precioA)
            subresultado.append(float(rentaA))
            if verboso:
                print("[GeneradorReportes] depto encontrado para "+nombreCliente)

        else:

            tasacionArriendo=tb2.calcularTasacionData("arriendo",prop[4],prop[10],prop[11],prop[8],prop[9],prop[6],prop[7],prop[12],props)

            precioA=tasacionArriendo[0]

            if precioA is None:
                continue

            subresultado.append(precioA)
            rentaA=((precioA-prop[5])/prop[5])
            if verboso:
                print("[GeneradorReportes] arriendo real: "+str(prop[5]))
            if verboso:
                print("[GeneradorReportes] arriendo predicho: "+str(precioA))
            if verboso:
                print("[GeneradorReportes] rentabildiad: "+str(rentaA))
            if rentaA>1:
                continue

            if rentaA<rentminarriendo:
                continue

            subresultado.append(float(rentaA))

        if not pubPortalExiste.publicacionExiste(prop[13]):
            if verboso:
                print("[GeneradorReportes] link no disponible")
            continue
        else:
            subresultado.append(prop[13])

        if verboso:
            print("[GeneradorReportes] depto encontrado para "+nombreCliente)
        resultado.append(subresultado)
        #print("sub appended")

    if enviarActualizacionTG:
        tgbot.send_message("[GeneradorReportes] 100 porciento filtrado.", chat, URL)

    if len(resultado)>0:
        if verboso:
            print("[GeneradorReportes] Generando Reporte para el cliente "+nombreCliente)

        if enviarActualizacionTG:
            tgbot.send_message("[GeneradorReportes] Generando reporte para cliente " + nombreCliente, chat, URL)

        if (prioridad=="arriendo"):
            resultado=sorted(resultado, key=lambda x:x[11],reverse=True)
        elif (prioridad=="venta"):
            resultado=sorted(resultado, key=lambda x:x[9],reverse=True)
        else:
            resultado=sorted(resultado, key=lambda x:x[0])


        if (operacion=="venta"):
            columnNames=["Precio","Útil","Tot","D","B","E","Metro","Dist-est.","P.P","Rent.V","Arriendo","Rent.A","Link"]
        else:
            columnNames=["Precio","Útil","Tot","D","B","E","Metro","Dist-est.","Arriendo","Rent.A","Link"]


        today = datetime.today().strftime('%Y-%m-%d')
        nombreArchivo = nombreCliente + " propiedades usadas VA " +str(tipo)+" "+ today
        #FLAGMAIL=1 Si es reporte normal
        if (flagMail==1):
            pdfC.createPdfReport(nombreCliente, "reporte " + nombreArchivo + ".pdf", resultado, columnNames,operacion)
            sendmail.sendMail(mail,nombreCliente,("reporte "+str(nombreArchivo)+".pdf"))

            if verboso:
                print("[GeneradorReportes] Enviando reporte a cliente "+nombreCliente)

        #FLAGMAIL=2 Si es reporte interno
        elif (flagMail==2):
            writeCsv("reporte " + nombreArchivo+'.csv', resultado, columnNames, operacion)
            sendmail.sendMail(mail,nombreCliente,("reporte "+str(nombreArchivo)+".csv"))

            if verboso:
                print("[GeneradorReportes] Enviando reporte a cliente "+nombreCliente)
            if enviarActualizacionTG:
                tgbot.send_message("[GeneradorReportes]Enviando reporte a cliente " + str(nombreCliente), chat, URL)

    else:
        if enviarActualizacionTG:
            tgbot.send_message("[GeneradorReportes] No se han encontrado propiedades para el cliente " + str(nombreCliente), chat, URL)
        if verboso:
            print("[GeneradorReportes] No se han encontrado propiedades para el cliente "+nombreCliente)

   #insertarClientes_Propiedades(subresultado)

def generarCanjeador(preciomin, preciomax, utilmin, utilmax, totalmin, totalmax, lat,lon,
                       dormitoriosmin, dormitoriosmax, banosmin, banosmax, estacionamientos, tipo,
                       operacion, region,comuna, mail,nombreCliente,distancia,verboso,
                          enviarActualizacionTG=False,chat="",URL=""):

    preciomin=float(preciomin)
    preciomax=float(preciomax)
    utilmin=int(utilmin)
    utilmax=int(utilmax)
    totalmin=int(totalmin)
    totalmax=int(totalmax)

    distancia = int(distancia)

    lat = float(lat)
    lon = float(lon)

    latmin = lat-((0.009/1000)*distancia)
    latmax = lat+((0.009/1000)*distancia)
    lonmin = lon-((0.01/1000)*distancia)
    lonmax = lon+((0.01/1000)*distancia)


    dormitoriosmin=int(dormitoriosmin)
    dormitoriosmax=int(dormitoriosmax)
    banosmax=int(banosmax)

    estacionamientos=int(estacionamientos)

    tipo=str(tipo)
    operacion=str(operacion)
    region=str(region)
    comuna=str(comuna)

    mail=str(mail)
    nombreCliente=str(nombreCliente)

    propiedades=from_portalinmobiliario_select_canje(past,yesterday,preciomin,preciomax,utilmin,utilmax,totalmin,totalmax,
                                               latmin,latmax,lonmin,lonmax,dormitoriosmin,dormitoriosmax,banosmin,
                                               banosmax,estacionamientos,tipo,operacion,region,comuna,"asdddd","asdddd",
                                               "asdddd","asdddd","asdddd",verboso)

    if verboso:
        print("[GeneradorReportes] total propiedades encontradas: "+str(len(propiedades)))

    if enviarActualizacionTG:
        tgbot.send_message("[GeneradorReportes] Encontradas " + str(len(propiedades)) + " propiedades.", chat, URL)

    count=0

    porc25 = int(len(propiedades)/4)
    porc50 = int(len(propiedades)/2)
    porc75 = porc25+porc50

    resultado = []

    for prop in propiedades:
        count=count+1

        if verboso:
            print("GeneradorReportes] " + str(count)+"/"+str(len(propiedades)))

        if enviarActualizacionTG:
            if porc25!=0 and count>porc25 and count < porc50:
                tgbot.send_message("[GeneradorReportes] 25 porciento filtrado. ", chat, URL)
                porc25 = 0
            elif porc50 != 0 and count > porc50 and count < porc75:
                tgbot.send_message("[GeneradorReportes] 50 porciento filtrado. ", chat, URL)
                porc50 = 0
            elif porc75 != 0 and count > porc75:
                tgbot.send_message("[GeneradorReportes] 75 porciento filtrado. ", chat, URL)
                porc75 = 0

        subresultado=[]

        subresultado.append(int(prop[5]))
        subresultado.append(int(prop[8]))
        subresultado.append(int(prop[9]))
        subresultado.append(int(prop[6]))
        subresultado.append(int(prop[7]))
        subresultado.append(int(prop[12]))
        subresultado.append(str(prop[14]))
        subresultado.append(str(prop[15]))

        if not pubPortalExiste.publicacionExiste(prop[13]):
            if verboso:
                print("[GeneradorReportes] link no disponible")
            continue
        else:
            subresultado.append(prop[13])

        if verboso:
            print("[GeneradorReportes] depto encontrado para "+ nombreCliente)

        resultado.append(subresultado)

    if enviarActualizacionTG:
        tgbot.send_message("[GeneradorReportes] 100 porciento filtrado.", chat, URL)

    if len(resultado)>0:
        if verboso:
            print("[GeneradorReportes] Generando Reporte para el cliente "+nombreCliente)

        if enviarActualizacionTG:
            tgbot.send_message("[GeneradorReportes] Generando reporte para cliente " + nombreCliente, chat, URL)

        resultado=sorted(resultado, key=lambda x:x[0])

        columnNames=["Precio","Útil","Total","Dormitorios","Banos","Estacionamientos","Mail","esDueno","Link"]

        today = datetime.today().strftime('%Y-%m-%d')
        nombreArchivo = nombreCliente + " propiedades canje " +str(tipo)+" "+ today +'.csv'

        writeCsvCanje(nombreArchivo, resultado, columnNames, operacion)
        sendmail.sendMail(mail,nombreCliente,(nombreArchivo))

        if verboso:
            print("[GeneradorReportes] Enviando canjes de cliente "+nombreCliente)
        if enviarActualizacionTG:
                tgbot.send_message("[GeneradorReportes] Enviando canjes de cliente " + str(nombreCliente), chat, URL)

    else:
        if enviarActualizacionTG:
            tgbot.send_message("[GeneradorReportes] No se han encontrado propiedades de canje para el cliente " + str(nombreCliente), chat, URL)
        if verboso:
            print("[GeneradorReportes] No se han encontrado propiedades de canje para el cliente "+nombreCliente)


def yaReportado(idCliente,idProp):
    sql = "SELECT * from clientes_propiedades WHERE cliente =" + str(idCliente) + " and prop=" + str(idProp)
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    result = cur.fetchall()

    if len(result) > 0:
        fechareporte=result[3]
        return True,fechareporte
    else:
        return False,'2000-01-01'

def guardarRegistro(idCliente,idProp,fechareporte):
    sql = "INSERT INTO clientes_propiedades(cliente,prop,fecha) VALUES('" + str(idCliente) + "','" + str(idProp) + "','" + str(fechareporte) + "') ON DUPLICATE KEY UPDATE prop='" + str(idProp) + "';"
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    mariadb_connection.commit()
    mariadb_connection.close()


def getDatosDueno(idProp2):
    sql = "SELECT mail,telefono,esDueno from duenos WHERE idProp =" + str(idProp2)
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    result = result[0]
    return result[0],result[1],result[2]

def generarReporteSeparado(preciomin, preciomax, utilmin, utilmax, totalmin, totalmax, latmin, latmax, lonmin, lonmax,
                       dormitoriosmin,dormitoriosmax, banosmin, banosmax, confmin, rentminventa, rentminarriendo,
                           estacionamientos, metrodistance, tipo,operacion, region, listaComunas,prioridad, mail,
                           nombreCliente,idCliente,direccion,radioDireccion,verboso):

    columnNames = []

    if preciomin is not None:
        preciomin = float(preciomin)
    else:
        preciomin=0
    columnNames.append("Precio")

    if preciomax is not None:
        preciomax = float(preciomax)
    else:
        preciomax=999999999999

    if utilmin is not None:
        utilmin = int(utilmin)
    else:
        utilmin=0
    columnNames.append("Util")

    if utilmax is not None:
        utilmax = int(utilmax)
    else:
        utilmax=99999999

    if totalmin is not None:
        totalmin = int(totalmin)
    else:
        totalmin=0
    columnNames.append("Total")

    columnNames.append("Dormitorios")

    columnNames.append("Banos")

    columnNames.append("Estacionamientos")

    if totalmax is not None:
        totalmax = int(totalmax)
    else:
        totalmax=99999999

    if latmin is not None:
        latmin = float(latmin)
    else:
        latmin=-999999

    if latmax is not None:
        latmax = float(latmax)
    else:
        latmax=999999

    if lonmin is not None:
        lonmin = float(lonmin)
    else:
        lonmin=-9999999

    if lonmax is not None:
        lonmax = float(lonmax)
    else:
        lonmax=9999999

    if dormitoriosmin is not None:
        dormitoriosmin = int(dormitoriosmin)
    else:
        dormitoriosmin=1

    if dormitoriosmax is not None:
        dormitoriosmax = int(dormitoriosmax)
    else:
        dormitoriosmax=10

    if banosmin is not None:
        banosmin = int(banosmin)
    else:
        banosmin=1

    if banosmax is not None:
        banosmax = int(banosmax)
    else:
        banosmax=6

    if metrodistance is not None:
        metrodistance = int(metrodistance)
        columnNames.append("Metro")
        columnNames.append("Distancia metro")


    else:
        metrodistance=999999999

    if confmin is not None:
        confmin = int(confmin)
    else:
        confmin=1

    if rentminventa is not None:
        rentminventa = float(rentminventa)
        columnNames.append("Precio Venta Tasado")
        columnNames.append("Rentabilidad Venta")


    else:
        rentminventa=-1

    if rentminarriendo is not None:
        rentminarriendo = float(rentminarriendo)
        columnNames.append("Precio Arriendo Tasado")
        columnNames.append("Rentabilidad Arriendo")
    else:
        rentminarriendo=0

    if estacionamientos is not None:
        estacionamientos = int(estacionamientos)
    else:
        estacionamientos=0


    if tipo is not None:
        tipo = str(tipo)
    else:
        print("Error, debe haber tipo")
        return


    if operacion is not None:
        operacion = str(operacion)
    else:
        print("Error, debe haber operacion")
        return

    if region is not None:
        region = str(region)
    else:
        print("Error, debe haber region")
        return

    if region is not None:
        prioridad = str(prioridad)


    if mail is not None:
        mail = str(mail)
    else:
        print("Error, debe haber mail")
        return

    if nombreCliente is not None:
        nombreCliente = str(nombreCliente)
    else:
        print("Error, debe haber nombre Cliente")
        return

    if direccion is not None and radioDireccion is not None:
        direccion = str(direccion)
        distancia = int(radioDireccion)
        latD, lonD = gm.getCoordsWithAdress(direccion)

        latD = float(latD)
        lonD = float(lonD)

        latminD = latD - ((0.009 / 1000) * distancia)
        latmaxD = latD + ((0.009 / 1000) * distancia)
        lonminD = lonD - ((0.01 / 1000) * distancia)
        lonmaxD = lonD + ((0.01 / 1000) * distancia)

        latmin = max(latmin,latminD)
        latmax = min(latmax,latmaxD)
        lonmin = max(lonmin,lonminD)
        lonmax = min(lonmax,lonmaxD)

    
    props=from_portalinmobiliario(tipo,region,verboso)
    estaciones1 = estaciones()
    columnNames.append("Link")

    columnNames.append("Mail")
    columnNames.append("Telefono")
    columnNames.append("es dueno")
    columnNames.append('fecha encontrado')

    listaAdjuntos=[]

    for comuna in listaComunas:
        for d in range(dormitoriosmin, dormitoriosmax + 1):
            for b in range(banosmin, banosmax + 1):

                propiedades=from_portalinmobiliario_select(past,yesterday,preciomin,preciomax,utilmin,utilmax,totalmin,totalmax,
                                               latmin,latmax,lonmin,lonmax,d,d,b,
                                               b,estacionamientos,tipo,operacion,region,comuna,"asdasd","asdasd",
                                               "asdasd","asdasd","asdasd",verboso)
                resultado = []

                if verboso:
                    print("[GeneradorReportes] total propiedades encontradas: "+str(len(propiedades)))

                count=0

                for prop in propiedades:
                    count=count+1

                    idProp = prop[14]
                    ya=yaReportado(idCliente=idCliente,idProp=idProp)
                    if ya[0]:
                        fechareporte=ya[1]
                    else:
                        fechareporte=fechahoy

                    if verboso:
                        print("GeneradorReportes] " + str(count)+"/"+str(len(propiedades)))

                    estaciones2=[]
                    for e in estaciones1:
                        subestacion=[]
                        late=e[3]
                        lone=e[4]
                        lat1=prop[10]
                        long1=prop[11]
                        r=6371000
                        c=pi/180
                        distance= 2*r*asin(sqrt(sin(c*(late-lat1)/2)**2 + cos(c*lat1)*cos(c*late)*sin(c*(lone-long1)/2)**2))
                        subestacion.append(e[1])
                        subestacion.append(e[2])
                        subestacion.append(distance)
                        estaciones2.append(subestacion)
                    estaciones2=sorted(estaciones2,key=lambda x:x[2])
                    estacioncercana=estaciones2[0]

                    if metrodistance != None:
                        if estacioncercana[2]>float(metrodistance):
                            continue


                    subresultado=[]
                    # precio
                    subresultado.append(int(prop[5]))
                    # util
                    subresultado.append(int(prop[8]))
                    # total
                    subresultado.append(int(prop[9]))
                    #Dormitorios
                    subresultado.append(int(d))
                    #Baños
                    subresultado.append(int(b))
                    # estacionamiento
                    subresultado.append(int(prop[12]))

                    auxestacion="("+str(estacioncercana[0])+") "+str(estacioncercana[1])
                    if metrodistance < 999999999:
                        # metro
                        subresultado.append(auxestacion)
                        # distancia metro
                        subresultado.append(estacioncercana[2])


                    rentaPromedio=rentaPProm(prop[4],int(prop[6]),int(prop[7]),int(prop[12]),comuna)
                    if (rentaPromedio<=0):
                        continue

                    if verboso:
                        print("[GeneradorReportes] renta promedio para la comuna de: "+str(comuna)+" para propiedades tipo "+str(tipo)+" de "+str(int(prop[6]))+" dormitorios, "+str(int(prop[7]))+" baños , y "+str(int(prop[12]))+" estacionamientos, es de: "+str(rentaPromedio))
                    if (operacion=="venta" and (rentminventa>-1 or rentminarriendo>0)):

                        tasacionVenta=tb2.calcularTasacionData("venta",prop[4],prop[10],prop[11],prop[8],prop[9],prop[6],prop[7],prop[12],props)
                        tasacionArriendo=tb2.calcularTasacionData("arriendo",prop[4],prop[10],prop[11],prop[8],prop[9],prop[6],prop[7],prop[12],props)
                        precioV=tasacionVenta[0]*uf.getUf()

                        try:
                            conftasacion=tasacionVenta[5]
                        except:
                            if verboso:
                                print("[GeneradorReportes] " + str(tasacionVenta))
                            continue

                        if confmin is not None:
                            if confmin<conftasacion:
                                continue

                        precioA=tasacionArriendo[0]


                        if precioV is None or precioV<0.1:
                            if verboso:
                                print("[GeneradorReportes] no hay precio predicho")
                            continue


                        rentaV=((precioV-prop[5])/prop[5])
                        # if rentaV<rentmin or rentaV>1:
                        #     continue


                        if rentaV<rentminventa:
                            if verboso:
                                print("[GeneradorReportes] renta de venta muy baja")
                            continue

                        if precioA is None or precioA<0.01:
                            if verboso:
                                print("[GeneradorReportes] no existe precio de arriendo")
                            continue

                        rentaA=(precioA*12/prop[5])
                        rentaPP=(precioA*12/precioV)
                        if verboso:
                            print("[GeneradorReportes] rentapp: "+str(rentaPP))
                        if rentaA>0.2:
                            if verboso:
                                print("[GeneradorReportes] renta de arriendo muy alta")
                            continue

                        if rentaPP<rentaPromedio:
                            if verboso:
                                print("[GeneradorReportes] renta pp muy baja, recalculando precio")
                            precioV=precioA*12/rentaPromedio
                            rentaV=((precioV-prop[5])/prop[5])
                            rentaPP=(precioA*12/precioV)
                            if verboso:
                                print("[GeneradorReportes] rentapp: "+str(rentaPP))

                        if rentaV<rentminventa:
                            if verboso:
                                print("[GeneradorReportes] renta de venta muy baja")
                            continue

                        if rentaPP>0.15:

                            if verboso:
                                print("[GeneradorReportes] renta pp muy alta, recalculando precio")
                            precioV=precioA*12/0.15
                            rentaV=((precioV-prop[5])/prop[5])

                        if rentaA<0:
                            if verboso:
                                print("[GeneradorReportes] renta de arriendo muy baja")
                            continue

                        if rentaA<rentminarriendo:
                            if verboso:
                                print("[GeneradorReportes] renta de arriendo mas baja que minima")
                            continue
                        if rentminventa>-1:
                            # precio venta tasado
                            subresultado.append(precioV)
                            # rentabilidad de venta
                            subresultado.append(float(rentaV))

                        if rentminarriendo>0:
                            # precio arriendo tasado
                            subresultado.append(precioA)
                            # rentabilidad de arriendo
                            subresultado.append(float(rentaA))
                        if verboso:
                            print("[GeneradorReportes] depto encontrado para "+nombreCliente)

                    else:
                        if rentminarriendo>0:
                            tasacionArriendo=tb2.calcularTasacionData("arriendo",prop[4],prop[10],prop[11],prop[8],prop[9],prop[6],prop[7],prop[12],props)
                            precioA=tasacionArriendo[0]

                        if precioA is None:
                            continue

                        # precio arriendo tasado
                        subresultado.append(precioA)
                        rentaA=((precioA-prop[5])/prop[5])
                        if verboso:
                            print("[GeneradorReportes] arriendo real: "+str(prop[5]))
                        if verboso:
                            print("[GeneradorReportes] arriendo predicho: "+str(precioA))
                        if verboso:
                            print("[GeneradorReportes] rentabildiad: "+str(rentaA))
                        if rentaA>1:
                            continue

                        if rentaA<rentminarriendo:
                            continue

                        # rentabilidad arriendo
                        subresultado.append(float(rentaA))

                    if not pubPortalExiste.publicacionExiste(prop[13]):
                        if verboso:
                            print("[GeneradorReportes] link no disponible")
                        continue
                    else:
                        # link
                        subresultado.append(prop[13])


                    #agregar mail, telefono y dueño
                    email,telefono,dueno = getDatosDueno(prop[0])

                    subresultado.append(email)
                    subresultado.append(telefono)
                    subresultado.append(dueno)



                    subresultado.append(fechahoy)

                    if verboso:
                        print("[GeneradorReportes] depto encontrado para "+nombreCliente)
                    resultado.append(subresultado)
                    #print("sub appended")

                    guardarRegistro(idCliente, idProp, fechareporte)
                if len(resultado)>0:
                    if verboso:
                        print("[GeneradorReportes] Generando Reporte para el cliente "+nombreCliente)


                    if (prioridad=="arriendo"):
                        index = columnNames.index("Rentabilidad Arriendo")
                        resultado=sorted(resultado, key=lambda x:x[index],reverse=True)
                    elif (prioridad=="venta"):
                        index = columnNames.index("Rentabilidad Venta")
                        resultado=sorted(resultado, key=lambda x:x[index],reverse=True)
                    else:
                        resultado=sorted(resultado, key=lambda x:x[0])


                    #if (operacion=="venta"):
                     #   columnNames=["Precio","Útil","Tot","Estacionamiento","Metro","Dist-est.","P.P","Rent.V","Arriendo","Rent.A","Link"]
                    #else:
                     #   columnNames=["Precio","Útil","Tot","D","B","E","Metro","Dist-est.","Arriendo","Rent.A","Link"]


                    nombreArchivo = "reporte "+ nombreCliente + str(tipo)+" "+ str(comuna) + " " +str(d) + " " + str(b)+ " " + str(fechahoy)+'.csv'


                    writeCsv(nombreArchivo, resultado, columnNames, operacion)



                    listaAdjuntos.append(nombreArchivo)

                    if verboso:
                        print("[GeneradorReportes] Enviando reporte a cliente "+nombreCliente)

                else:
                    if verboso:
                        print("[GeneradorReportes] No se han encontrado propiedades para el cliente "+nombreCliente)

    sendmail.sendMailMultiple(mail, nombreCliente, listaAdjuntos)


if __name__ == '__main__':
    #main()
    # generarReporte(preciomin=70000000, preciomax=140000000,utilmin=0,utilmax=99,totalmin=0,totalmax=99,latmin=-9999,
    #                latmax=9999,lonmin=-9999,lonmax=9999,dormitoriosmin=1,dormitoriosmax=2,banosmin=1,banosmax=2,
    #                confmin=8,rentmin=0.00,estacionamientos=1,metrodistance=9999,tipo='departamento',operacion='venta',
    #                region='metropolitana',comuna1='vitacura',comuna2='asdasdasd',comuna3='asdasd',comuna4='asdasdasd',
    #                comuna5='asdasd',comuna6='asdasdasd',prioridad='arriendo',flagMail=1,mail='joaquin.gonzalez@alumnos.usm.cl',
    #                nombreCliente='PruebaSergei',verboso=True)

    generarReporteInterno(preciomin=20000000, preciomax=60000000,utilmin=0,utilmax=99,totalmin=0,totalmax=99,latmin=-9999,
                   latmax=9999,lonmin=-9999,lonmax=9999,dormitoriosmin=1,dormitoriosmax=1,banosmin=1,banosmax=2,
                   confmin=8,rentminventa=0.15,rentminarriendo=0.05,estacionamientos=0,metrodistance=9999,tipo='departamento',operacion='venta',
                   region='metropolitana',comuna1='la-cisterna',comuna2='asdasdasd',comuna3='asdasd',comuna4='asdasdasd',
                   comuna5='asdasd',comuna6='asdasdasd',prioridad='venta',flagMail=2,mail='sergei.schkolnik@gmail.com',
                   nombreCliente='la-cisterna-1-1',verboso=True)
