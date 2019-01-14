import math
import pymysql as mysql
from math import radians, sin, cos, acos, asin,pi,sqrt
from datetime import datetime, timedelta, date
past = datetime.now() - timedelta(days=120)
past=datetime.date(past)
yesterday = datetime.now() - timedelta(days=30)
yesterday=datetime.date(yesterday)
import uf

from datetime import datetime, timedelta
import pdfCreatorProyectos as pdfC
import numpy as np
from sklearn import datasets, linear_model
uf1=uf.getUf()


def mean(numbers):
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

def calcularDistancia(i,data):
    past=datetime.date(datetime.now() - timedelta(days=120))
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

        # i3=op, i4=tipo, i5=precio, i6=dorms, i7=baños, i12= estacionamientos i8=util, i9=total, i14=piso
        if (j[2]>past) and (i[3]==j[3]) and (i[4]==j[4]) and (j!=i):
            #print("ok, primera iteracion")
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
            print("no se han encontrado propiedades para comparar")
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

        # prices=[]
        # count=0
        # for d in distancias:
        #     p=d[5]
        #     if (count==1) and (q==p):
        #         continue
        #     else:
        #         prices.append(p)
        #         count=1
        #         q=p

        # i3=op, i4=tipo, i5=precio, i6=dorms, i7=baños, i12= estacionamientos i8=util, i9=total

        y_train = []
        x_train = []
        for e in distancias:
            x_train.append([e[8],e[9],e[6],e[7],e[12],e[14]])
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
        x_test = [i[8],i[9],i[6],i[7],i[12],i[17]]
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
        # cosa=mean(prices)
        # precio=cosa[0]
        # std=cosa[1]
        # preciomin=precio-std
        # preciomax=precio+std
        return price,t_actual
    except:
        print("No existen departamentos para comparar")



def from_proyectos():
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='proyectos')
    cur = mariadb_connection.cursor()
    #sql="SELECT proyectos.id, deptos.id, deptos.fechascrap, proyectos.comuna,proyectos.tipo,deptos.precio,deptos.dormitorios,deptos.banos,deptos.utiles,deptos.totales,proyectos.lat,proyectos.lon,proyectos.estacionamiento,proyectos.link FROM deptos,proyectos"
    sql="SELECT id2,deptos.id,deptos.fechascrap,proyectos.comuna,proyectos.tipo,deptos.precio,deptos.dormitorios,deptos.banos,deptos.utiles,deptos.totales,proyectos.lat,proyectos.lon,proyectos.estacionamiento,proyectos.link, deptos.piso FROM proyectos INNER JOIN deptos ON proyectos.id2 = deptos.id_proyecto"
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


def from_proyectos_select(past,yesterday,preciomin,preciomax,utilmin,utilmax,totalmin,totalmax,latmin,latmax,lonmin,lonmax,dormitoriosmin,dormitoriosmax,banosmin,banosmax,estacionamientos,tipo,operacion,region,comuna1,comuna2,comuna3,comuna4,comuna5,comuna6):
        mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='proyectos')
        cur = mariadb_connection.cursor()

        sqlselect = "SELECT id2,deptos.id,deptos.fechascrap,proyectos.comuna,proyectos.tipo,deptos.precio,deptos.dormitorios,deptos.banos,deptos.utiles,deptos.totales,proyectos.lat,proyectos.lon,proyectos.estacionamiento,proyectos.link, proyectos.entrega, proyectos.vende, proyectos.construye, deptos.piso FROM proyectos INNER JOIN deptos ON proyectos.id2 = deptos.id_proyecto WHERE "
        sql=sqlselect
        sqlwhere="deptos.fechascrap>='"+str(yesterday)+"' AND "
        sql=sql + sqlwhere

        sqlwhere="deptos.precio>="+str(preciomin)+" AND "
        sql=sql+sqlwhere

        sqlwhere="deptos.precio<="+str(preciomax)+" AND "
        sql=sql+sqlwhere

        sqlwhere="deptos.utiles>="+str(utilmin)+" AND "
        sql=sql+sqlwhere

        sqlwhere="deptos.utiles<="+str(utilmax)+" AND "
        sql=sql+sqlwhere

        sqlwhere="deptos.totales>="+str(totalmin)+" AND "
        sql=sql+sqlwhere

        sqlwhere="deptos.totales<="+str(totalmax)+" AND "
        sql=sql+sqlwhere


        sqlwhere="proyectos.lat>="+str(latmin)+" AND "
        sql=sql+sqlwhere

        sqlwhere="proyectos.lat<="+str(latmax)+" AND "
        sql=sql+sqlwhere

        sqlwhere="proyectos.lon>="+str(lonmin)+" AND "
        sql=sql+sqlwhere

        sqlwhere="proyectos.lon<="+str(lonmax)+" AND "
        sql=sql+sqlwhere

        sqlwhere="deptos.dormitorios>="+str(dormitoriosmin)+" AND "
        sql=sql+sqlwhere

        sqlwhere="deptos.dormitorios<="+str(dormitoriosmax)+" AND "
        sql=sql+sqlwhere

        sqlwhere="deptos.banos>="+str(banosmin)+" AND "
        sql=sql+sqlwhere

        sqlwhere="deptos.banos<="+str(banosmax)+" AND "
        sql=sql+sqlwhere

        sqlwhere="proyectos.estacionamiento>="+str(estacionamientos)+" AND "
        sql=sql+sqlwhere


        sqlwhere="tipo LIKE '%" + str(tipo) + "%' AND "
        sql=sql+sqlwhere

        sqlwhere="link LIKE '%"+str(region)+"%' AND "
        sql=sql+sqlwhere

        sqlwhere="(link LIKE '%" + comuna1 + "%' or link LIKE '%"+ comuna2 + "%' or link LIKE '%"+ comuna3 + "%' or link LIKE '%"+ comuna4 + "%' or link LIKE '%"+ comuna5 +"%' or link LIKE '%"+ comuna6 +"%')"
        sql=sql+sqlwhere

        #print(sql)
        cur.execute(sql)
        tupla = cur.fetchall()
        return tupla

def clientes():
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='proyectos')
    cur = mariadb_connection.cursor()
    sql = "SELECT * FROM clientesproyectos"
    cur.execute(sql)
    tupla = cur.fetchall()
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


props=from_proyectos()
print("proyectos rescatados")
data=clientes()
print("clientes rescatados")
resultado=[]
for i in data:
    #print(i[34])
    #print("cliente")
    resultado=[]
    if i[34]==0:
        continue
    elif i[34]==1:
        activo=2
        #actualizarActividad(i[0])
    else:
        past = datetime.now() - timedelta(days=1)
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
    metrodistance=(i[30])
    try:
        pisomin=float(i[34])
        pisomax=float(i[35])
    except:
        print("piso no registrado")
    estacionamientos=float(i[19])

    tipo=i[20]
    operacion=i[21]
    region=i[23]
    comuna1=i[24]
    if comuna1 is None:
        comuna1="abcdefghij"
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
    propiedades=from_proyectos_select(past,yesterday,preciomin,preciomax,utilmin,utilmax,totalmin,totalmax,latmin,latmax,lonmin,lonmax,dormitoriosmin,dormitoriosmax,banosmin,banosmax,estacionamientos,tipo,operacion,region,comuna1,comuna2,comuna3,comuna4,comuna5,comuna6)
    estaciones1=estaciones()
    for prop in propiedades:
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
        preciob=calcularDistancia(prop,props)
        try:
            subresultado=[]
            uni=str(prop[0])+"000"+str(i[0])
            uni=int(uni)
            #ID proyecto
            subresultado.append(int(prop[0]))

            #ID Depto
            #subresultado.append(int(prop[1]))
            #Comuna
            subresultado.append(prop[3])
            #tipologia
            tipologia=(str(prop[6])+"/"+str(prop[7]))
            subresultado.append(tipologia)
            #Precio
            subresultado.append(int(prop[5]))
            #SupUtil
            #subresultado.append(int(prop[8]))
            #SupTotal
            #subresultado.append(int(prop[9]))
            #Dorms
            #subresultado.append(int(prop[6]))
            #Baños
            #subresultado.append(int(prop[7]))
            #Estacionamientos
            #subresultado.append(int(prop[12]))
            #Metro
            #subresultado.append(estacioncercana[1])
            #subresultado.append(estacioncercana[0])
            #subresultado.append(estacioncercana[2])

            tasacion=calcularDistancia(prop,props)
            preciob=tasacion[0]
            confianza=tasacion[1]

            print(str(prop[0])+" tiene un nivel de confianza de "+str(confianza))

            rentab=((preciob)-prop[5])/prop[5]
            print(prop[1])
            print(rentab)
            if rentab<0.1:
                continue
            #Prediccion
            subresultado.append(preciob)
            #Rentabilidad
            subresultado.append(float(rentab))
            #Link
            subresultado.append(prop[13])
            #entrega
            entrega=prop[14]
            subresultado.append(entrega)
            #Inmobiliaria
            inmobiliaria=prop[15]
            try:
                inmobiliaria=inmobiliaria.replace("Inmobiliaria ","")
            except:
                z=0
            try:
                inmobiliaria=inmobiliaria.replace(" Inmobiliaria","")
            except:
                z=0

            try:
                inmobiliaria=inmobiliaria.replace("Constructora ","")
            except:
                z=0
            try:
                inmobiliaria=inmobiliaria.replace("Constructora","")
            except:
                z=0
            try:
                inmobiliaria=inmobiliaria[:20]
            except:
                z=0
            subresultado.append(inmobiliaria)
            #Constructora
            constructora=prop[16]
            try:
                constructora=constructora.replace("Constructora ","")
            except:
                z=0
            try:
                constructora=constructora.replace("Constructora","")
            except:
                z=0

            try:
                constructora=constructora.replace("Inmobiliaria ","")
            except:
                z=0
            try:
                constructora=constructora.replace("Inmobiliaria","")
            except:
                z=0
            try:
                constructora=constructora[:20]
            except:
                z=0

            subresultado.append(constructora)


            print("depto encontrado para "+str(i[1]))
            resultado.append(subresultado)
            print("sub appended")
        except:
            print("exception ocurred")



    print(len(resultado))
    s = sorted(resultado, key=lambda x:x[5],reverse=True)
    resultado=sorted(s, key=lambda x:x[0])
    a=""
    resultado2=[]
    for prop in resultado:
        if (a==prop[0]):
            continue
        else:
            a=prop[0]
            resultado2.append(prop)
    resultado2 = sorted(resultado2, key=lambda x:x[5],reverse=True)

    if len(resultado)>0:
        columnNames=["Id","Comuna","Tip.","P. Real","P. Predicho","Rent.","Link","Entrega","Inmobiliaria","Constructora"]

        today = datetime.today().strftime('%Y-%m-%d')
        nombreArchivo = i[1] + " proyectos " +str(tipo)+" "+ today
        pdfC.createPdfReport(i[1], "reporte " + nombreArchivo + ".pdf", resultado2, columnNames,operacion)
    else:
        print("No se han encontrado propiedades para el cliente "+i[1])
   #insertarClientes_Propiedades(subresultado)
