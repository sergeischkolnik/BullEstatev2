import tasadorbot as tb
import math
import pymysql as mysql
import math
from math import radians, sin, cos, acos, asin,pi,sqrt
from datetime import datetime, timedelta, date
past = datetime.now() - timedelta(days=90)
past=datetime.date(past)
yesterday = datetime.now() - timedelta(days=3)
yesterday=datetime.date(yesterday)
import googleMapApi as gm
import propManager as pm



def actualizarActividad():

    sql = "UPDATE pedidos SET activo=0 WHERE activo=1"

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='railstest')

    cur = mariadb_connection.cursor()
    cur.execute(sql)
    mariadb_connection.commit()
    mariadb_connection.close()

def tasacion():
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='railstest')
    cur = mariadb_connection.cursor()
    sql = "SELECT operacion,tipo,latitud,longitud,sup_util,superficie,dorms,bano,estacionamiento,direccion,comuna FROM pedidos WHERE activo=1"

    cur.execute(sql)
    tasacion=cur.fetchall()
    return tasacion

tasacion=tasacion()
tasacion=tasacion[0]
print (tasacion)
direccion = tasacion[9] + ", " + tasacion[10] + ", Chile"

direccion=tasacion[9]
lat,lon = gm.getCoordsWithAdress(direccion)
precio,nivel,nrcomp,links=tb.calcularTasacion(tasacion[0],tasacion[1],float(lat),float(lon),float(tasacion[4]),float(tasacion[5]),int(tasacion[6]),int(tasacion[7]),int(tasacion[8]))

print("El precio tasado es UF " + str(precio)+", con un nivel de confianza: "+str(nivel)+\
                                   ", tasación realizada comparandose con "+str(nrcomp)+" propiedades.")
actualizarActividad()
