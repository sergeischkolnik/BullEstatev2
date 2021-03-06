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

    return price,utilnegativa,terrazanegativa,estacionamientosnegativa

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


def calcularTasacion(operacion,region,tipo,lat,lon,util,total,dormitorios,banos,estacionamientos):

    es_venta=operacion=="venta"
    print(es_venta)
    data = from_portalinmobiliario(operacion,tipo,region)
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
    print("1 corte")
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

            #T0
            if (distance < 1000) and (abs(util/j[8]-1)<0.1) and (abs(total/j[9]-1)<0.2) and (dormitorios==j[6]) and (banos==j[7]) and (estacionamientos==j[12]) and ((k0[5]!=j[5]) or (k0[8]!=j[8]) or (k0[9]!=j[9]) or (k0[6]!=j[6]) or (k0[7]!=j[7]) or (k0[12]!=j[12])):
                d=sqrt(distance*distance+(100*abs(util-j[8])*(100*abs(util-j[8])))+(100*abs(total-j[9])*(100*abs(total-j[9]))))
                j.append(d)
                distanciat0.append(j)
                k0=j
                j=j[:-1]


            #T1 REVISAR
            if (distance < 1000) and (abs(util/j[8]-1)<0.2) and (abs(total/j[9]-1)<0.4) and (dormitorios==j[6]) and (banos==j[7]) and (estacionamientos==j[12]) and ((k1[5]!=j[5]) or (k1[8]!=j[8]) or (k1[9]!=j[9]) or (k1[6]!=j[6]) or (k1[7]!=j[7]) or (k1[12]!=j[12])) :
                d=sqrt(distance*distance+(100*abs(util-j[8])*(100*abs(util-j[8])))+(100*abs(total-j[9])*(100*abs(total-j[9]))))
                j.append(d)
                distanciat1.append(j)
                j=j[:-1]
                k1=j

            #T2.1
            if (distance < 1000) and (abs(util/j[8]-1)<0.2) and (abs(total/j[9]-1)<0.4) and (dormitorios==j[6]) and (banos==j[7]) and (int(estacionamientos)>=(int(j[12])-1) and (int(estacionamientos)<=(int(j[12])+1))) and ((k21[5]!=j[5]) or (k21[8]!=j[8]) or (k21[9]!=j[9]) or (k21[6]!=j[6]) or (k21[7]!=j[7]) or (k21[12]!=j[12])) :
                d=sqrt(distance*distance+(100*abs(util-j[8])*(100*abs(util-j[8])))+(100*abs(total-j[9])*(100*abs(total-j[9]))))
                j.append(d)
                distanciat2_1.append(j)
                j=j[:-1]
                k21=j

            #T2.2
            if (distance < 1000) and (abs(util/j[8]-1)<0.2) and (abs(total/j[9]-1)<0.4) and (dormitorios==j[6]) and (banos==j[7]) and ((k22[5]!=j[5]) or (k22[8]!=j[8]) or (k22[9]!=j[9]) or (k22[6]!=j[6]) or (k22[7]!=j[7]) or (k22[12]!=j[12])) :
                d=sqrt(distance*distance+(100*abs(util-j[8])*(100*abs(util-j[8])))+(100*abs(total-j[9])*(100*abs(total-j[9]))))
                j.append(d)
                distanciat2_2.append(j)
                j=j[:-1]
                k22=j

            #T3.1
            if (distance < 1000) and (abs(util/j[8]-1)<0.2) and (abs(total/j[9]-1)<0.4) and (int(dormitorios)>=(int(j[6])-1) and (int(dormitorios)<=(int(j[6])+1))) and (banos==j[7]) and ((k31[5]!=j[5]) or (k31[8]!=j[8]) or (k31[9]!=j[9]) or (k31[6]!=j[6]) or (k31[7]!=j[7]) or (k31[12]!=j[12])) :
                d=sqrt(distance*distance+(100*abs(util-j[8])*(100*abs(util-j[8])))+(100*abs(total-j[9])*(100*abs(total-j[9]))))
                j.append(d)
                distanciat3_1.append(j)
                j=j[:-1]
                k31=j

            #T3.2
            if (distance < 1000) and (abs(util/j[8]-1)<0.2) and (abs(total/j[9]-1)<0.4) and (banos==j[7]) and ((k32[5]!=j[5]) or (k32[8]!=j[8]) or (k32[9]!=j[9]) or (k32[6]!=j[6]) or (k32[7]!=j[7]) or (k32[12]!=j[12])):
                d=sqrt(distance*distance+(100*abs(util-j[8])*(100*abs(util-j[8])))+(100*abs(total-j[9])*(100*abs(total-j[9]))))
                j.append(d)
                distanciat3_2.append(j)
                j=j[:-1]
                k32=j

            #T4.1
            if (distance < 1000) and (abs(util/j[8]-1)<0.2) and (abs(total/j[9]-1)<0.4) and (int(banos)>=(int(j[7])-1) and (int(banos)<=(int(j[7])+1))) and ((k41[5]!=j[5]) or (k41[8]!=j[8]) or (k41[9]!=j[9]) or (k41[6]!=j[6]) or (k41[7]!=j[7]) or (k41[12]!=j[12])):
                d=sqrt(distance*distance+(100*abs(util-j[8])*(100*abs(util-j[8])))+(100*abs(total-j[9])*(100*abs(total-j[9]))))
                j.append(d)
                distanciat4_1.append(j)
                j=j[:-1]
                k41=j

            #T4.2
            if (distance < 1000) and (abs(util/j[8]-1)<0.2) and (abs(total/j[9]-1)<0.4) and ((k42[5]!=j[5]) or (k42[8]!=j[8]) or (k42[9]!=j[9]) or (k42[6]!=j[6]) or (k42[7]!=j[7]) or (k42[12]!=j[12])):
                d=sqrt(distance*distance+(100*abs(util-j[8])*(100*abs(util-j[8])))+(100*abs(total-j[9])*(100*abs(total-j[9]))))
                j.append(d)
                distanciat4_2.append(j)
                j=j[:-1]
                k42=j
    print("2 corte")

    t_actual="A+"
    cota=10

    if len(distanciat0)>=cota:
        distancia=distanciat0

    elif len(distanciat1)>=cota:
        distancia=distanciat1
        t_actual="A-"
    elif len(distanciat2_1)>=cota:
        distancia=distanciat2_1
        t_actual="B+"
    elif len(distanciat2_2)>=cota:
        distancia=distanciat2_2
        t_actual="B-"
    elif len(distanciat3_1)>=cota:
        distancia=distanciat3_1
        t_actual="C+"
    elif len(distanciat3_2)>=cota:
        distancia=distanciat3_2
        t_actual="C-"
    elif len(distanciat4_1)>=cota:
        distancia=distanciat4_1
        t_actual="D+"
    elif len(distanciat4_2)>=5:
        distancia=distanciat4_2
        t_actual="D-"

    else:
        return 0,"E",len(distanciat4_2),[],False
    print("t actual definido")
    distancias=sorted(distancia,key=lambda x:x[14])
    try:
        distancias=distancias[:40]
    except:
        distancias=distancia

    links = []
    for props in distancias:
            links.append(props[13])

    y_train = []
    x_train = []

    for e in distancias:
        reg_terraza=(e[9]-e[8])
        reg_util = e[8]
        reg_dorms = e[6]
        reg_banos = e[7]
        reg_precio = e[5]
        reg_estacionamientos = e[12]
        x_train.append([reg_util,reg_terraza,reg_dorms,reg_banos,reg_estacionamientos,reg_util*reg_util,
                        reg_util*reg_terraza,reg_util*reg_dorms,reg_util*reg_banos,reg_terraza*reg_terraza,reg_terraza*reg_dorms,
                        reg_terraza*reg_banos,reg_dorms*reg_dorms,reg_dorms*reg_banos,reg_banos*reg_banos])
        y_train.append(reg_precio)

    #y2_train=[]
    #y2_train.append(y_train)
    #y_train=y2_train
    x_train=np.array(x_train)
    y_train=np.array(y_train)


    x_test = [util,(total-util),dormitorios,banos,estacionamientos,
              util*util,util*(total-util),util*dormitorios,util*banos,
              (total-util)*(total-util),(total-util)*dormitorios,(total-util)*banos,
              dormitorios*dormitorios,dormitorios*banos,banos*banos]
    x_test=np.array(x_test)
    x_test=np.transpose(x_test)
    # Make predictions using the testing set

    price,utilnegativo,terrazanegativo,estacionamientosnegativo=regresion(x_train,y_train,x_test)

    for dato in x_train:
        if utilnegativo:
            dato[0] = float(0.00000)
            dato[5] = float(0.00000)
            dato[6] = float(0.00000)
            dato[7] = float(0.00000)
            dato[8] = float(0.00000)


        if terrazanegativo:
            dato[1]=float(0.00000)
            dato[6]=float(0.00000)
            dato[9]=float(0.00000)
            dato[10]=float(0.00000)
            dato[11]=float(0.00000)


        if estacionamientosnegativo:
            dato[4]=float(0.0000)


    if utilnegativo or terrazanegativo or estacionamientosnegativo:
        price, utilnegativo, terrazanegativo, estacionamientosnegativo = regresion(x_train, y_train, x_test)
    print("regresion hecha")
    try:
        if es_venta:
            price = int(price/uf.getUf())
        else:
            price = int(price)
        print(price,t_actual,len(distancias),links,es_venta)
        return(price,t_actual,len(distancias),links,es_venta)

    except:

        return -1,"ERROR",-1,[],False

def calcularTasacionData(operacion,tipo,lat,lon,util,total,dormitorios,banos,estacionamientos,data):

    ufn=uf.getUf()
    es_venta=operacion=="venta"
    distanciat000=[]
    distanciat00=[]
    distanciat0=[]
    distanciat1=[]
    distanciat2_1=[]
    distanciat2_2=[]
    distanciat3_1=[]
    distanciat3_2=[]
    distanciat4_1=[]
    distanciat4_2=[]
    distanciat5_1=[]
    distanciat5_2=[]
    distanciat5_3=[]
    distanciat6_0=[]

    tasacionsimple=False

    k000=[0]*14
    k00=[0]*14
    k0=[0]*14
    k1=[0]*14
    k21=[0]*14
    k22=[0]*14
    k31=[0]*14
    k32=[0]*14
    k41=[0]*14
    k42=[0]*14
    k51=[0]*14
    k52=[0]*14
    k53=[0]*14
    k60=[0]*14


    data=sorted(data, key=lambda x:x[5])

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

            #T000 (AA+)
            if (distance < 50) and (abs(util/j[8]-1)<0.1) and (abs(total/j[9]-1)<0.2) and \
                    ((dormitorios==j[6]) or tipo=="comercial") and (banos==j[7]) and ((estacionamientos==j[12]) or tipo=="casa" or tipo=="comercial") and \
                    ((k000[5]!=j[5]) or (k000[8]!=j[8]) or (k000[9]!=j[9]) or (k000[6]!=j[6]) or (k000[7]!=j[7]) or (k000[12]!=j[12])):

                d=sqrt(distance*distance+(100*abs(util-j[8])*(100*abs(util-j[8])))+(100*abs(total-j[9])*(100*abs(total-j[9]))))
                j.append(d)
                distanciat000.append(j)
                k000=j
                j=j[:-1]


            #T00 (AA-)
            elif (distance < 500) and (abs(util/j[8]-1)<0.1) and (abs(total/j[9]-1)<0.2) and ((dormitorios==j[6]) or tipo=="comercial") and \
                    (banos==j[7]) and ((estacionamientos==j[12]) or tipo=="casa" or tipo=="comercial") and \
                    ((k00[5]!=j[5]) or (k00[8]!=j[8]) or (k00[9]!=j[9]) or (k00[6]!=j[6]) or (k00[7]!=j[7]) or (k00[12]!=j[12])):

                d=sqrt(distance*distance+(100*abs(util-j[8])*(100*abs(util-j[8])))+(100*abs(total-j[9])*(100*abs(total-j[9]))))
                j.append(d)
                distanciat00.append(j)
                k00=j
                j=j[:-1]

            #T0
            elif (distance < 1000) and (abs(util/j[8]-1)<0.1) and (abs(total/j[9]-1)<0.2) and ((dormitorios==j[6]) or tipo=="comercial") \
                    and (banos==j[7]) and ((estacionamientos==j[12]) or tipo=="casa" or tipo=="comercial") \
                    and ((k0[5]!=j[5]) or (k0[8]!=j[8]) or (k0[9]!=j[9]) or (k0[6]!=j[6]) or (k0[7]!=j[7]) or (k0[12]!=j[12])):

                d=sqrt(distance*distance+(100*abs(util-j[8])*(100*abs(util-j[8])))+(100*abs(total-j[9])*(100*abs(total-j[9]))))
                j.append(d)
                distanciat0.append(j)
                k0=j
                j=j[:-1]


            #T1 REVISAR
            elif (distance < 1000) and (abs(util/j[8]-1)<0.2) and (abs(total/j[9]-1)<0.4) and ((dormitorios==j[6]) or tipo=="comercial") \
                    and (banos==j[7]) and ((estacionamientos==j[12]) or tipo=="casa" or tipo=="comercial") and \
                    ((k1[5]!=j[5]) or (k1[8]!=j[8]) or (k1[9]!=j[9]) or (k1[6]!=j[6]) or (k1[7]!=j[7]) or (k1[12]!=j[12])) :

                d=sqrt(distance*distance+(100*abs(util-j[8])*(100*abs(util-j[8])))+(100*abs(total-j[9])*(100*abs(total-j[9]))))
                j.append(d)
                distanciat1.append(j)
                j=j[:-1]
                k1=j

            #T2.1
            if (distance < 1000) and (abs(util/j[8]-1)<0.2) and (abs(total/j[9]-1)<0.4) and ((dormitorios==j[6]) or tipo=="comercial") \
                    and (banos==j[7]) and ((int(estacionamientos)>=(int(j[12])-1) or tipo=="casa" or tipo=="comercial") and (int(estacionamientos)<=(int(j[12])+1))) \
                    and ((k21[5]!=j[5]) or (k21[8]!=j[8]) or (k21[9]!=j[9]) or (k21[6]!=j[6]) or (k21[7]!=j[7]) or (k21[12]!=j[12])) :

                d=sqrt(distance*distance+(100*abs(util-j[8])*(100*abs(util-j[8])))+(100*abs(total-j[9])*(100*abs(total-j[9]))))
                j.append(d)
                distanciat2_1.append(j)
                j=j[:-1]
                k21=j

            #T2.2
            elif (distance < 1000) and (abs(util/j[8]-1)<0.2) and (abs(total/j[9]-1)<0.4) and ((dormitorios==j[6]) or tipo=="comercial") \
                    and (banos==j[7]) and ((k22[5]!=j[5]) or (k22[8]!=j[8]) or (k22[9]!=j[9]) or (k22[6]!=j[6]) or (k22[7]!=j[7]) or (k22[12]!=j[12])) :

                d=sqrt(distance*distance+(100*abs(util-j[8])*(100*abs(util-j[8])))+(100*abs(total-j[9])*(100*abs(total-j[9]))))
                j.append(d)
                distanciat2_2.append(j)
                j=j[:-1]
                k22=j

            #T3.1
            elif (distance < 1000) and (abs(util/j[8]-1)<0.2) and (abs(total/j[9]-1)<0.4) and \
                    ((int(dormitorios)>=(int(j[6])-1) or tipo=="comercial") and (int(dormitorios)<=(int(j[6])+1))) and (banos==j[7]) and \
                    ((k31[5]!=j[5]) or (k31[8]!=j[8]) or (k31[9]!=j[9]) or (k31[6]!=j[6]) or (k31[7]!=j[7]) or (k31[12]!=j[12])) :

                d=sqrt(distance*distance+(100*abs(util-j[8])*(100*abs(util-j[8])))+(100*abs(total-j[9])*(100*abs(total-j[9]))))
                j.append(d)
                distanciat3_1.append(j)
                j=j[:-1]
                k31=j

            #T3.2
            elif (distance < 1000) and (abs(util/j[8]-1)<0.2) and (abs(total/j[9]-1)<0.4) and (banos==j[7]) and \
                    ((k32[5]!=j[5]) or (k32[8]!=j[8]) or (k32[9]!=j[9]) or (k32[6]!=j[6]) or (k32[7]!=j[7]) or (k32[12]!=j[12])):

                d=sqrt(distance*distance+(100*abs(util-j[8])*(100*abs(util-j[8])))+(100*abs(total-j[9])*(100*abs(total-j[9]))))
                j.append(d)
                distanciat3_2.append(j)
                j=j[:-1]
                k32=j

            #T4.1
            elif (distance < 1000) and (abs(util/j[8]-1)<0.2) and (abs(total/j[9]-1)<0.4) and (int(banos)>=(int(j[7])-1) and (int(banos)<=(int(j[7])+1))) and \
                    ((k41[5]!=j[5]) or (k41[8]!=j[8]) or (k41[9]!=j[9]) or (k41[6]!=j[6]) or (k41[7]!=j[7]) or (k41[12]!=j[12])):

                d=sqrt(distance*distance+(100*abs(util-j[8])*(100*abs(util-j[8])))+(100*abs(total-j[9])*(100*abs(total-j[9]))))
                j.append(d)
                distanciat4_1.append(j)
                j=j[:-1]
                k41=j

            #T4.2
            elif (distance < 1000) and (abs(util/j[8]-1)<0.2) and (abs(total/j[9]-1)<0.4) and \
                    ((k42[5]!=j[5]) or (k42[8]!=j[8]) or (k42[9]!=j[9]) or (k42[6]!=j[6]) or (k42[7]!=j[7]) or (k42[12]!=j[12])):

                d=sqrt(distance*distance+(100*abs(util-j[8])*(100*abs(util-j[8])))+(100*abs(total-j[9])*(100*abs(total-j[9]))))
                j.append(d)
                distanciat4_2.append(j)
                j=j[:-1]
                k42=j
            #T5.1
            elif (distance < 1000) and ((k51[5]!=j[5]) or (k51[8]!=j[8]) or (k51[9]!=j[9]) or (k51[6]!=j[6]) or (k51[7]!=j[7]) or (k51[12]!=j[12])):

                d=sqrt(distance*distance+(100*abs(util-j[8])*(100*abs(util-j[8])))+(100*abs(total-j[9])*(100*abs(total-j[9]))))
                j.append(d)
                distanciat5_1.append(j)
                j=j[:-1]
                k51=j
            #T5.2
            elif (distance < 5000) and ((k52[5]!=j[5]) or (k52[8]!=j[8]) or (k52[9]!=j[9]) or (k52[6]!=j[6]) or (k52[7]!=j[7]) or (k52[12]!=j[12])):

                d=sqrt(distance*distance+(100*abs(util-j[8])*(100*abs(util-j[8])))+(100*abs(total-j[9])*(100*abs(total-j[9]))))
                j.append(d)
                distanciat5_1.append(j)
                j=j[:-1]
                k52=j
            #T5.3
            elif (distance < 10000) and ((k53[5]!=j[5]) or (k53[8]!=j[8]) or (k53[9]!=j[9]) or (k53[6]!=j[6]) or (k53[7]!=j[7]) or (k53[12]!=j[12])):

                d=sqrt(distance*distance+(100*abs(util-j[8])*(100*abs(util-j[8])))+(100*abs(total-j[9])*(100*abs(total-j[9]))))
                j.append(d)
                distanciat5_1.append(j)
                j=j[:-1]
                k53=j
            #T6
            elif ((k60[5]!=j[5]) or (k60[8]!=j[8]) or (k60[9]!=j[9]) or (k60[6]!=j[6]) or (k60[7]!=j[7]) or (k60[12]!=j[12])):

                d=sqrt(distance*distance+(100*abs(util-j[8])*(100*abs(util-j[8])))+(100*abs(total-j[9])*(100*abs(total-j[9]))))
                j.append(d)
                distanciat6_0.append(j)
                j=j[:-1]
                k60=j

    print("Tamaño de grupos:")

    print("distanciat000: "+str(len(distanciat000)))
    print("distanciat00: "+str(len(distanciat00)))
    print("distanciat0: "+str(len(distanciat0)))
    print("distanciat1: "+str(len(distanciat1)))
    print("distanciat2_1: "+str(len(distanciat2_1)))
    print("distanciat2_2: "+str(len(distanciat2_2)))
    print("distanciat3_1: "+str(len(distanciat3_1)))
    print("distanciat3_2: "+str(len(distanciat3_2)))
    print("distanciat4_1: "+str(len(distanciat4_1)))
    print("distanciat4_2: "+str(len(distanciat4_2)))
    print("distanciat5_1: "+str(len(distanciat5_1)))
    print("distanciat5_2: "+str(len(distanciat5_2)))
    print("distanciat5_3: "+str(len(distanciat5_3)))
    print("distanciat6_0: "+str(len(distanciat6_0)))



    t_actual="AA+"
    g_actual=1
    cota=10



    if len(distanciat000)>=6:
        distancia=distanciat000
    elif len(distanciat00+distanciat000)>=8:
        distancia=distanciat00+distanciat000
        t_actual="AA-"
        g_actual=1
    elif len(distanciat0+distanciat00+distanciat000)>=cota:
        distancia=distanciat0+distanciat00+distanciat000
        t_actual="A+"
        g_actual=1
    elif len(distanciat1+distanciat0+distanciat00+distanciat000)>=cota:
        distancia=distanciat1+distanciat0+distanciat00+distanciat000
        t_actual="A-"
        g_actual=2
    elif len(distanciat2_1+distanciat1+distanciat0+distanciat00+distanciat000)>=cota:
        distancia=distanciat2_1+distanciat1+distanciat0+distanciat00+distanciat000
        t_actual="B+"
        g_actual=3
    elif len(distanciat2_2+distanciat2_1+distanciat1+distanciat0+distanciat00+distanciat000)>=cota:
        distancia=distanciat2_2+distanciat2_1+distanciat1+distanciat0+distanciat00+distanciat000
        t_actual="B-"
        g_actual=4
    elif len(distanciat3_1+distanciat2_2+distanciat2_1+distanciat1+distanciat0+distanciat00+distanciat000)>=cota:
        distancia=distanciat3_1+distanciat2_2+distanciat2_1+distanciat1+distanciat0+distanciat00+distanciat000
        t_actual="C+"
        g_actual=5
    elif len(distanciat3_2+distanciat3_1+distanciat2_2+distanciat2_1+distanciat1+distanciat0+distanciat00+distanciat000)>=cota:
        distancia=distanciat3_2+distanciat3_1+distanciat2_2+distanciat2_1+distanciat1+distanciat0+distanciat00+distanciat000
        t_actual="C-"
        g_actual=6
    elif len(distanciat4_1+distanciat3_2+distanciat3_1+distanciat2_2+distanciat2_1+distanciat1+distanciat0+distanciat00+distanciat000)>=cota:
        distancia=distanciat4_1+distanciat3_2+distanciat3_1+distanciat2_2+distanciat2_1+distanciat1+distanciat0+distanciat00+distanciat000
        t_actual="D+"
        g_actual=7
    elif len(distanciat4_2+distanciat4_1+distanciat3_2+distanciat3_1+distanciat2_2+distanciat2_1+distanciat1+distanciat0+distanciat00+distanciat000)>=5:
        distancia=distanciat4_2+distanciat4_1+distanciat3_2+distanciat3_1+distanciat2_2+distanciat2_1+distanciat1+distanciat0+distanciat00+distanciat000
        t_actual="D-"
        g_actual=8
    elif len(distanciat5_1+distanciat4_2+distanciat4_1+distanciat3_2+distanciat3_1+distanciat2_2+distanciat2_1+distanciat1+distanciat0+distanciat00+distanciat000)>=5:
        distancia=distanciat5_1+distanciat4_2+distanciat4_1+distanciat3_2+distanciat3_1+distanciat2_2+distanciat2_1+distanciat1+distanciat0+distanciat00+distanciat000
        t_actual="E+"
        g_actual=9
        tasacionsimple=True
    elif len(distanciat5_2+distanciat5_1+distanciat4_2+distanciat4_1+distanciat3_2+distanciat3_1+distanciat2_2+distanciat2_1+distanciat1+distanciat0+distanciat00+distanciat000)>=5:
        distancia=distanciat5_2+distanciat5_1+distanciat4_2+distanciat4_1+distanciat3_2+distanciat3_1+distanciat2_2+distanciat2_1+distanciat1+distanciat0+distanciat00+distanciat000
        t_actual="E-"
        g_actual=10
        tasacionsimple=True
    elif len(distanciat5_3+distanciat5_2+distanciat5_1+distanciat4_2+distanciat4_1+distanciat3_2+distanciat3_1+distanciat2_2+distanciat2_1+distanciat1+distanciat0+distanciat00+distanciat000)>=5:
        distancia=distanciat5_3+distanciat5_2+distanciat5_1+distanciat4_2+distanciat4_1+distanciat3_2+distanciat3_1+distanciat2_2+distanciat2_1+distanciat1+distanciat0+distanciat00+distanciat000
        t_actual="F+"
        g_actual=11
        tasacionsimple=True
    elif len(distanciat6_0+distanciat5_3+distanciat5_2+distanciat5_1+distanciat4_2+distanciat4_1+distanciat3_2+distanciat3_1+distanciat2_2+distanciat2_1+distanciat1+distanciat0+distanciat00+distanciat000)>=5:
        distancia=distanciat6_0+distanciat5_3+distanciat5_2+distanciat5_1+distanciat4_2+distanciat4_1+distanciat3_2+distanciat3_1+distanciat2_2+distanciat2_1+distanciat1+distanciat0+distanciat00+distanciat000
        t_actual="F-"
        g_actual=12
        tasacionsimple=True

    else:
        return 0,"N",0,["No hay links para tasación inválida",""],es_venta,13

    distancias=sorted(distancia,key=lambda x:x[14])
    try:
        distancias=distancias[:20]
    except:
        distancias=distancia

    for dist in distancias:
        preciomt=dist[5]/((dist[8]+dist[9])/2)
        dist.append(preciomt)

    preciosmts=[el[15] for el in distancias]

    med=stat.median(preciosmts)
    intermin=0.4*med
    intermax=2.5*med

    arregloaux=[]

    for preciodistancia in distancias:
        if preciodistancia[15]<intermax and preciodistancia[15]>intermin:
            arregloaux.append(preciodistancia)

    print("mediana:"+str(med))
    print("intermin:"+str(intermin))
    print("intermax:"+str(intermax))
    print("Propiedades Eliminadas: "+str(len(distancias)-len(arregloaux)))
    distancias=arregloaux

    links = []
    for props in distancias:
            links.append(props[13])
    if tasacionsimple:
        preciosmts=[el[15] for el in distancias]
        prom=stat.mean(preciosmts)
        sup=(util+total)/2
        price=sup*prom
        try:
            if es_venta:
                price = int(price/ufn)
            else:
                price = int(price)

            return(price,t_actual,len(distancias),links,es_venta,g_actual)
        except:

            return (0,"N",len(distancias),["No hay links para tasación inválida",""],es_venta,13)


    y_train = []
    x_train = []

    for e in distancias:
        reg_terraza=(e[9]-e[8])
        reg_util = e[8]
        reg_dorms = e[6]
        reg_banos = e[7]
        reg_precio = e[5]
        reg_estacionamientos = e[12]
        x_train.append([reg_util,reg_terraza,reg_dorms,reg_banos,reg_estacionamientos,reg_util*reg_util,
                        reg_util*reg_terraza,reg_util*reg_dorms,reg_util*reg_banos,reg_terraza*reg_terraza,reg_terraza*reg_dorms,
                        reg_terraza*reg_banos,reg_dorms*reg_dorms,reg_dorms*reg_banos,reg_banos*reg_banos])
        y_train.append(reg_precio)

    #y2_train=[]
    #y2_train.append(y_train)
    #y_train=y2_train
    x_train=np.array(x_train)
    y_train=np.array(y_train)


    x_test = [util,(total-util),dormitorios,banos,estacionamientos,
              util*util,util*(total-util),util*dormitorios,util*banos,
              (total-util)*(total-util),(total-util)*dormitorios,(total-util)*banos,
              dormitorios*dormitorios,dormitorios*banos,banos*banos]
    x_test=np.array(x_test)
    x_test=np.transpose(x_test)
    # Make predictions using the testing set

    price,utilnegativo,terrazanegativo,estacionamientosnegativo=regresion(x_train,y_train,x_test)

    for dato in x_train:
        if utilnegativo:
            dato[0] = float(0.00000)
            dato[5] = float(0.00000)
            dato[6] = float(0.00000)
            dato[7] = float(0.00000)
            dato[8] = float(0.00000)


        if terrazanegativo:
            dato[1]=float(0.00000)
            dato[6]=float(0.00000)
            dato[9]=float(0.00000)
            dato[10]=float(0.00000)
            dato[11]=float(0.00000)


        if estacionamientosnegativo:
            dato[4]=float(0.0000)


    if utilnegativo or terrazanegativo or estacionamientosnegativo:
        price, utilnegativo, terrazanegativo, estacionamientosnegativo = regresion(x_train, y_train, x_test)

    try:
        if es_venta:
            price = int(price/ufn)
        else:
            price = int(price)
        return(price,t_actual,len(distancias),links,es_venta,g_actual)

    except:

        return (0,"N",len(distancias),["No hay links para tasación inválida",""],es_venta,13)

if __name__ == "__main__":

    operacion = "venta"
    tipo = "departamento"
    lat = -33.404904
    lon=-70.5947597
    util = 240
    total = 270
    dormitorios = 3
    banos = 3
    estacionamientos=2

    precio,confianza,nrProps,links = calcularTasacion(operacion,tipo,lat,lon,util,total,dormitorios,banos,estacionamientos)
