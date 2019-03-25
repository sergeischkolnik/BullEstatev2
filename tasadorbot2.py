import math
import pymysql as mysql
import math
from math import radians, sin, cos, acos, asin,pi,sqrt
from datetime import datetime, timedelta, date
past = datetime.now() - timedelta(days=90)
past=datetime.date(past)
yesterday = datetime.now() - timedelta(days=3)
yesterday=datetime.date(yesterday)
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import uf

uf1=uf.getUf()



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

def precio_from_portalinmobiliario(id2):
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT precio,metrosmin,metrosmax,lat,lon,dormitorios,banos FROM portalinmobiliario WHERE id2='"+str(id2)+"'"
    cur.execute(sql)
    precio = cur.fetchall()

    return precio


def calcularTasacion(operacion,tipo,lat,lon,util,total,dormitorios,banos,estacionamientos):


    data = from_portalinmobiliario()
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
        print("no se han encontrado propiedades para comparar")
        return 0,"E",len(distanciat4_2),[]

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
        x_train.append([e[8],e[9],e[6],e[7],e[12],e[8]*e[8],e[8]*e[9],e[8]*e[6],e[8]*e[7],e[9]*e[9],e[9]*e[6],e[9]*e[7]],e[6]*e[7])
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
    x_test = [util,total,dormitorios,banos,estacionamientos,util*util,util*total,util*dormitorios,util*banos,total*dormitorios,total*banos,dormitorios*banos]
    x_test=np.array(x_test)
    x_test=np.transpose(x_test)
    # Make predictions using the testing set

    price=regr.intercept_
    c=0
    for coef in regr.coef_:
        print("\n")
        print (coef)

        price=price+coef*x_test[c]
        c=c+1


    #print(price)
    cota=len(distancias)+1
#print("y_pred = " + str(y_pred))
# The coefficients
#print('Coefficients: \n', regr.coef_)

    try:
        price = int(price/uf.getUf())
        return(price,t_actual,len(distancias),links,coef)

    except:

        return -1,"ERROR",-1,[]

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
    print("Precio:" + str(precio))
    print("confianza:" + str(confianza))
    print("comparado con:" + str(nrProps))
    for link in links:
            print(link)
