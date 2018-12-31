import math
import mysql.connector
from math import radians, sin, cos, acos, asin,pi,sqrt
from datetime import datetime, timedelta, date
past = datetime.now() - timedelta(days=30)
past=datetime.date(past)
yesterday = datetime.now() - timedelta(days=3)
yesterday=datetime.date(yesterday)
from threading import Thread
from time import sleep
import psycopg2
from datetime import datetime, timedelta
import pdfCreatorTest as pdfC

def estaciones():
    mariadb_connection = mysql.connector.connect(user='root', password='sergei', host='127.0.0.1', database='metro')
    cur = mariadb_connection.cursor()
    sql = "SELECT * FROM estaciones"
    cur.execute(sql)
    tupla = cur.fetchall()
    return tupla

def rentabilidad(prop):
    mariadb_connection = mysql.connector.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT rentabilidad FROM rentabilidades_portalinmobiliario WHERE prop="+str(prop)
    cur.execute(sql)
    rent = cur.fetchall()
    rent=rent[0]
    rent=rent[0]
    return rent


def from_portalinmobiliario_select(past,yesterday,preciomin,preciomax,utilmin,utilmax,totalmin,totalmax,latmin,latmax,lonmin,lonmax,dormitoriosmin,dormitoriosmax,banosmin,banosmax,estacionamientos,tipo,operacion,region,comuna1,comuna2,comuna3,comuna4,comuna5,comuna6):
        mariadb_connection = mysql.connector.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
        cur = mariadb_connection.cursor()

        sqlselect = "SELECT * FROM portalinmobiliario WHERE "

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

        print(sql)
        cur.execute(sql)
        tupla = cur.fetchall()
        return tupla

def clientes():
    mariadb_connection = mysql.connector.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT * FROM clientes"
    cur.execute(sql)
    tupla = cur.fetchall()
    return tupla

def insertarClientes_Propiedades(resultado):
    sql = """INSERT INTO clientes_propiedades(uni,cliente,prop)
             VALUES(%s,%s,%s) ON DUPLICATE KEY UPDATE prop=%s"""

    mariadb_connection = mysql.connector.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')

    cur = mariadb_connection.cursor()
    cur.execute(sql, (resultado))
    mariadb_connection.commit()
    mariadb_connection.close()

def actualizarActividad(cliente):

    sql = "UPDATE clientes SET activo=2 WHERE id="+str(cliente)

    mariadb_connection = mysql.connector.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')

    cur = mariadb_connection.cursor()
    cur.execute(sql)
    mariadb_connection.commit()
    mariadb_connection.close()



data=clientes()
resultado=[]
for i in data:
    print(i[34])
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
    propiedades=from_portalinmobiliario_select(past,yesterday,preciomin,preciomax,utilmin,utilmax,totalmin,totalmax,latmin,latmax,lonmin,lonmax,dormitoriosmin,dormitoriosmax,banosmin,banosmax,estacionamientos,tipo,operacion,region,comuna1,comuna2,comuna3,comuna4,comuna5,comuna6)
    estaciones1=estaciones()
    for prop in propiedades:
        estaciones2=[]
        for e in estaciones1:
            subestacion=[]
            late=e[3]
            lone=e[4]
            lat1=prop[15]
            long1=prop[16]
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

        try:
            subresultado=[]
            uni=str(prop[1])+"000"+str(i[0])
            uni=int(uni)
            subresultado.append(int(prop[9]))
            subresultado.append(int(prop[12]))
            subresultado.append(int(prop[13]))
            subresultado.append(int(prop[10]))
            subresultado.append(int(prop[11]))
            subresultado.append(int(prop[14]))
            subresultado.append(estacioncercana[1])
            subresultado.append(estacioncercana[0])
            subresultado.append(estacioncercana[2])
            rentab=rentabilidad(prop[1])
            if rentab<0.1:
                continue
            subresultado.append(float(rentab))
            subresultado.append(prop[17])

            print("depto encontrado para "+str(i[1]))
            resultado.append(subresultado)
            print("sub appended")
        except:
            print("exception ocurred")

    if len(resultado)>0:
        resultado=sorted(resultado, key=lambda x:x[9],reverse=True)
        columnNames=["Precio","Útil","Total","Dorms","Baños","Estacion.","Metro","Linea","Dist-est.","Rent.","Link"]

        today = datetime.today().strftime('%Y-%m-%d')
        nombreArchivo = i[1] + " propiedades usadas " +str(tipo)+" "+ today
        pdfC.createPdfReport(i[1], "reporte " + nombreArchivo + ".pdf", resultado, columnNames,operacion)
    else:
        print("No se han encontrado propiedades para el cliente "+i[1])
   #insertarClientes_Propiedades(subresultado)
