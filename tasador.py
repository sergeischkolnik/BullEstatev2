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
        #print("Coeficiente "+str(c)+":"+str(coef)+"precio parcial: "+str(price))
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



def calcularTasacionData(operacion,tipo,lat,lon,util,total,dormitorios,banos,estacionamientos,data):
    ufn=uf.getUf()
    es_venta=operacion=="venta"
    distanciasDict={}
    confDict={0:100,1:97,2:95,3:92,4:90,5:80,6:70,7:60,8:50,9:40,10:30,11:20,12:15,13:10,14:7,15:5,16:2,17:0}


    tasacionsimple=False

    kDict={}

    drange=[50,100,200,500,1000,1000,1000,1000,1000,1000,1000,1000,1000,5000,10000,5000000]
    utilrange=[0.1,0.1,0.1,0.1,0.1,0.2,0.2,0.2,0.2,0.2,0.2,0.2,1000000,1000000,1000000,1000000]
    dormrange=[0,0,0,0,0,0,0,0,1,1,100,100,100,100,100,100]
    bathrange=[0,0,0,0,0,0,0,0,0,1,1,100,100,100,100,100]
    parkingrange=[0,0,0,0,0,0,1,100,100,100,100,100,100,100,100,100]

    auxparkingbool=False
    #Aux dictionaries for different parkings
    auxDict1={}
    auxDict2={}

    try:

        if estacionamientos==0:
            auxparking1=1
            auxparking2=2
        if estacionamientos==1:
            auxparking1=1
            auxparking2=2
        else:
            auxparking1=estacionamientos-2
            auxparking2=estacionamientos-1
        auxparkingbool=True
    except:
        pass

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
            if tipo in 'local comercial':
                    dormitorios=0
                    banos=0
                    estacionamientos=0
                    j[6]=0
                    j[7]=0
                    j[12]=0
            for x in range (0,16):

                kDict[x]=[0]*16
                if (distance < drange[x]) and (abs(util/j[8]-1)<utilrange[x]) and (abs(total/j[9]-1)<(1.5*utilrange[x])) and \
                        (abs(dormitorios-j[6])<=dormrange[x] or tipo=="comercial") and (abs(banos-j[7])<=bathrange[x]or tipo=="comercial") and \
                        ((kDict[x][5]!=j[5]) or (kDict[x][8]!=j[8]) or (kDict[x][9]!=j[9]) or (kDict[x][6]!=j[6]) or (kDict[x][7]!=j[7]) or (kDict[x][12]!=j[12])):

                    d=sqrt(distance*distance+(100*abs(util-j[8])*(100*abs(util-j[8])))+(100*abs(total-j[9])*(100*abs(total-j[9]))))
                    j.append(d)
                    if x not in distanciasDict:
                        distanciasDict[x]=[]
                        #print("creada la entrada para el valor:"+str(x))
                        if auxparkingbool:
                            auxDict1[x]=[]
                            auxDict2[x]=[]

                    if ((abs(estacionamientos-j[12])<=parkingrange[x]) or tipo=="casa" or tipo=="comercial"):
                        distanciasDict[x].append(j)
                    if x<4:
                        if (auxparkingbool and (j[12]-estacionamientos)==-1):
                            auxDict1[x].append(j)
                        if (auxparkingbool and (j[12]-estacionamientos)==1):
                            auxDict2[x].append(j)
                    kDict[x]=j

                    break





    print("Tamaño de grupos:")
    for x in range(0,16):
        if x in distanciasDict:
            print(str(x)+": "+str(len(distanciasDict[x])))
    cota=5
    distancia=[]
    distanciaaux=[]
    auxdistancia1=[]
    auxdistancia2=[]

    g_actual=0
    for x in range (0,16):
        if x==1:
            cota+=1
        if x==2:
            cota+=1
        g_actual=x
        if x>=10:
            tasacionsimple=True
        if x in distanciasDict:
            distancia+=distanciasDict[x]

            for dist in distancia:
                preciomt=dist[5]/((dist[8]+dist[9])/2)
                dist.append(preciomt)

                preciosmts=[el[15] for el in distancia]

                med=stat.median(preciosmts)
                intermin=0.5*med
                intermax=2*med

                arregloaux=[]

                for preciodistancia in distancia:
                    if preciodistancia[15]<intermax and preciodistancia[15]>intermin:
                        arregloaux.append(preciodistancia)

                print("mediana:"+str(med))
                print("intermin:"+str(intermin))
                print("intermax:"+str(intermax))
                print("Propiedades Eliminadas: "+str(len(distancia)-len(arregloaux)))
                distancia=arregloaux

            if x<4:
                auxdistancia1+=auxDict1[x]
                auxdistancia2+=auxDict2[x]
            if len(distancia)>=cota:
                distancia=sorted(distancia,key=lambda x:x[5])
                for a in range(0,len(distancia)-1):
                    if (distancia[a][5]==distancia[a+1][5] and distancia[a][6]==distancia[a+1][6] and
                            distancia[a][7]==distancia[a+1][7] and distancia[a][12]==distancia[a+1][12] and
                            abs(distancia[a][8]-distancia[a+1][8])<=2 and
                            abs(distancia[a][9]-distancia[a+1][9])<=2) and len(distancia)>1:
                        pass
                    else:
                        distanciaaux.append(distancia[a])

                distancia=distanciaaux
                #opcion de marcar repetidos, o sacarlos de la matriz y no considerarlos en la tasacion
                if len(distancia)>=cota:

                    if x < 4:

                        if len(auxdistancia1)>=cota:

                            auxdistancia1 = sorted(auxdistancia1, key=lambda x: x[5])
                            auxcota = 0
                            if len(auxdistancia1)>1:
                                for a in range(0, len(auxdistancia1) - 1):
                                    print(a)
                                    print(auxdistancia1[a])
                                    if (auxdistancia1[a][5] == auxdistancia1[a + 1][5] and auxdistancia1[a][6] == auxdistancia1[a + 1][6] and
                                        auxdistancia1[a][7] == auxdistancia1[a + 1][7] and auxdistancia1[a][12] == auxdistancia1[a + 1][12] and
                                        abs(auxdistancia1[a][8] - auxdistancia1[a + 1][8]) <= 2 and
                                        abs(auxdistancia1[a][9] - auxdistancia1[a + 1][9]) <= 2):
                                        auxcota += 1
                                if (len(auxdistancia1)-auxcota>=cota):
                                    print('Datos con un estacionamiento menos: ' + str(len(auxdistancia1)))
                                    print('precio y estacionamientos con un estacionamiento menos: '+str([el[5] for el in auxdistancia1])+'-'  + str([el[12] for el in auxdistancia1]))
                                    distancia += auxdistancia1

                        if len(auxdistancia2)>=cota:

                            auxdistancia2 = sorted(auxdistancia2, key=lambda x: x[5])
                            auxcota = 0
                            if len(auxdistancia2)>1:
                                for a in range(0, len(auxdistancia2) - 1):
                                    if (auxdistancia2[a][5] == auxdistancia2[a + 1][5] and auxdistancia2[a][6] == auxdistancia2[a + 1][6] and
                                            auxdistancia2[a][7] == auxdistancia2[a + 1][7] and auxdistancia2[a][12] == auxdistancia2[a + 1][12] and
                                            abs(auxdistancia2[a][8] - auxdistancia2[a + 1][8]) <= 2 and
                                            abs(auxdistancia2[a][9] - auxdistancia2[a + 1][9]) <= 2):
                                        auxcota += 1
                            if len(auxdistancia2) - auxcota >= cota:
                                #print('Datos con un estacionamiento mas: ' + str(len(auxdistancia2)))
                                #print('precio y estacionamientos con un estacionamiento mas: '+str([el[5] for el in auxdistancia1])+'-'  + str([el[12] for el in auxdistancia2]))
                                distancia+=auxdistancia2

                    print('grupo Resultante: '+str(x))
                    break

    if len(distancia)<cota:
        return(0,0,len(distancia),"No links to show",es_venta,17)

    distancias=sorted(distancia,key=lambda x:x[14])
    try:
        distancias=distancias[:10]
    except:
        pass

    #esto hay q hacerlo antes de sacar la cota

    print('Datos Finales: ' + str(len(distancias)))
    print('precio y estacionamientos Finales: ' + str([el[5]/ufn for el in distancias]) + '-' + str(
         [el[12] for el in distancias]))
    print('IDS Finales: ' + str(sorted([el[0] for el in distancias])))

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

            return(price,confDict[g_actual],len(distancias),links,es_venta,g_actual)
        except:
            print("Entro al except 1")
            return (0,0,len(distancias),["No hay links para tasación inválida",""],es_venta,17)


    y_train = []
    x_train = []

    for e in distancias:
        reg_terraza=(e[9]-e[8])
        reg_util = e[8]
        reg_dorms = e[6]
        reg_banos = e[7]
        reg_precio = e[5]
        reg_estacionamientos = e[12]
        # x_train.append([reg_util,reg_terraza,reg_dorms,reg_banos,reg_estacionamientos,reg_util*reg_util,
        #                 reg_util*reg_terraza,reg_util*reg_dorms,reg_util*reg_banos,reg_terraza*reg_terraza,reg_terraza*reg_dorms,
        #                 reg_terraza*reg_banos,reg_dorms*reg_dorms,reg_dorms*reg_banos,reg_banos*reg_banos])
        x_train.append([reg_util, reg_terraza, reg_dorms, reg_banos, reg_estacionamientos,
                        reg_util*reg_dorms,reg_util*reg_banos,reg_dorms*reg_dorms,reg_dorms*reg_banos,reg_banos*reg_banos])
        y_train.append(reg_precio)

    #y2_train=[]
    #y2_train.append(y_train)
    #y_train=y2_train
    x_train=np.array(x_train)
    y_train=np.array(y_train)


    # x_test = [util,(total-util),dormitorios,banos,estacionamientos,
    #           util*util,util*(total-util),util*dormitorios,util*banos,
    #           (total-util)*(total-util),(total-util)*dormitorios,(total-util)*banos,
    #           dormitorios*dormitorios,dormitorios*banos,banos*banos]
    x_test = [util, (total - util), dormitorios, banos, estacionamientos,
              util * dormitorios, util * banos,
              dormitorios * dormitorios, dormitorios * banos, banos * banos]
    x_test=np.array(x_test)
    x_test=np.transpose(x_test)
    # Make predictions using the testing set

    price,utilnegativo,terrazanegativo,estacionamientosnegativo=regresion(x_train,y_train,x_test)

    for dato in x_train:
        if utilnegativo:
            dato[0] = float(0.00000)
            # dato[5] = float(0.00000)
            # dato[6] = float(0.00000)
            # dato[7] = float(0.00000)
            # dato[8] = float(0.00000)


        if terrazanegativo:
            dato[1]=float(0.00000)
            # dato[6]=float(0.00000)
            # dato[9]=float(0.00000)
            # dato[10]=float(0.00000)
            # dato[11]=float(0.00000)


        if estacionamientosnegativo:
            dato[4]=float(0.0000)


    if utilnegativo or terrazanegativo or estacionamientosnegativo:
        price, utilnegativo, terrazanegativo, estacionamientosnegativo = regresion(x_train, y_train, x_test)
    try:
        if es_venta:
            price = int(price/ufn)

        else:
            price = int(price)
        if price>0:
            print("Check")
            print(price)
            return(price,confDict[g_actual],len(distancias),links,es_venta,g_actual)
        else:
            return (0, "N", len(distancias), ["No hay links para tasación inválida", ""], es_venta, 13)

    except:
        print("Entro al except 2")
        print(price)
        return (0,"N",len(distancias),["No hay links para tasación inválida",""],es_venta,13)

if __name__ == "__main__":

    results=[]
    parkings=[0,1,2,3]
    ops=['venta','arriendo']
    for op in ops:
        for park in parkings:
            operacion = op
            tipo = "departamento"
            lat = -33.402253
            lon=-70.560878
            util = 90
            total = 100
            dormitorios = 3
            banos = 3
            estacionamientos=park
            region="valparaiso"
            regionYapo="6"
            propsP=reportes.from_portalinmobiliario(tipo,region,True)
            propsY=reportes.from_yapo(tipo,regionYapo,True,True)
            props=propsP+propsY
            print("Propiedades Check")
            result = calcularTasacionData(operacion,tipo,lat,lon,util,total,dormitorios,banos,estacionamientos,props)
            result2=[]
            for k in range(0,6):
                if k!=3:
                    result2.append(result[k])
            results.append(result2)
    print(results)
