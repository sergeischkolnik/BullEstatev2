
import math
import pymysql as mysql
from math import radians, sin, cos, acos, asin,pi,sqrt
from datetime import datetime, timedelta, date
past = datetime.now() - timedelta(days=180)
past=datetime.date(past)
yesterday = datetime.now() - timedelta(days=20)
yesterday=datetime.date(yesterday)
from threading import Thread
from time import sleep
from datetime import datetime, timedelta
import pdfCreatorReportes as pdfC
import uf
import numpy as np
from sklearn import datasets, linear_model
import sendmail
#import tasador as tb2
import tasadorbot2 as tb2
import sendMailOportunidad

import pubPortalExiste
import math
import csv
from csvWriter import writeCsv
from csvWriter import writeCsvCanje

from xlsxWriterv2 import writeXlsx
import os
import bot1 as tgbot
import googleMapApi as gm
import datetime

import reportesHuberV1 as reportes

from sklearn import ensemble
from sklearn.model_selection import train_test_split


def obtenerPropiedades():
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT nombre,region,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,estacionamientos,bodegas,lat,lon,link from portalinmobiliario inner join duenos " \
          "WHERE portalinmobiliario.id2=duenos.idProp AND portalinmobiliario.fechascrap>='"+str(yesterday)+"' AND (duenos.mail='contacto@vendetudepto.cl' or duenos.mail='carolina@vendetudepto.cl' or duenos.mail='daniela@vendetudepto.cl' or duenos.mail='pablo@vendetudepto.cl')"
    cur.execute(sql)
    propiedad = cur.fetchall()
    if len(propiedad)>0:
        return propiedad[0]
    else:
        return propiedad


def tasador(prop):
    propsPV = reportes.from_portalinmobiliario(client["tipo"].lower(),client["region"].lower(),listacomunas,"venta",True)
    propsYV = reportes.from_yapo(client["tipo"].lower(),regionYapo,listacomunas,True,"venta",True)
    propsV = propsPV + propsYV
    # aca deberiamos hacer el GB

    m2=reportes.m2prom(client["tipo"].lower(),comuna,client["region"].lower())
    m2V=m2[0]
    m2A=m2[1]

    clfHV = ensemble.GradientBoostingRegressor(n_estimators=400, max_depth=5, min_samples_split=2,
                                              learning_rate=0.1, loss='huber')

    #id2,fechapublicacion,fechascrap,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,lat,lon,estacionamientos,link

    preciosV = [row[5] for row in propsV]

    trainingV = propsV.copy()
    for row in trainingV:
        del row[13]
        del row[5]
        del row[4]
        del row[3]
        del row[2]
        del row[1]
        del row[0]

    x_train , x_test , y_train , y_test = train_test_split(trainingV , preciosV , test_size = 0.10,random_state = 2)

    #obtain scores venta:
    clfHV.fit(x_train, y_train)
    print("-----------")
    print("Score Huber:")
    print(clfHV.score(x_test,y_test))
    scoreV=clfHV.score(x_test,y_test)

    clfHV.fit(trainingV, preciosV)

    propsPA = reportes.from_portalinmobiliario(client["tipo"].lower(),client["region"].lower(),listacomunas,"arriendo",True)
    propsYA = reportes.from_yapo(client["tipo"].lower(),regionYapo,listacomunas,True,"arriendo",True)
    propsA = propsPA + propsYA
    # aca deberiamos hacer el GB

    clfHA = ensemble.GradientBoostingRegressor(n_estimators=400, max_depth=5, min_samples_split=2,
                                              learning_rate=0.1, loss='huber')

    #id2,fechapublicacion,fechascrap,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,lat,lon,estacionamientos,link

    preciosA = [row[5] for row in propsA]

    trainingA = propsA.copy()
    for row in trainingA:
        del row[13]
        del row[5]
        del row[4]
        del row[3]
        del row[2]
        del row[1]
        del row[0]

    x_train , x_test , y_train , y_test = train_test_split(trainingA , preciosA , test_size = 0.10,random_state = 2)

    #obtain scores arriendo:
    clfHA.fit(x_train, y_train)
    print("-----------")
    print("Score Huber:")
    print(clfHA.score(x_test,y_test))
    scoreA=clfHA.score(x_test,y_test)

    clfHA.fit(trainingA, preciosA)

    textmail+="Resultados comuna "+str(comuna)+":\n"+"Score Ventas: "+str((int(10000*scoreV))/100)+"%\nScore Arriendos: "+str((int(10000*scoreA))/100)+"%\nPrecio m2 Venta: UF "+'{:,}'.format((int(10*(m2V/ufn)))/10).replace(",",".")+"\nPrecio m2 Arriendo: $ "+'{:,}'.format(int(m2A)).replace(",",".")+"\n\n"
    tasacionVenta = clfHV.predict([[int(client["dormitorios"]),int(client["baños"]), int(client["metros"]),int(client["total"]), client["lat"],client["lon"], int(client["estacionamientos"])]])
    tasacionArriendo = clfHA.predict([[int(client["dormitorios"]),int(client["baños"]), int(client["metros"]),int(client["total"]), client["lat"],client["lon"], int(client["estacionamientos"])]])

    precioV = tasacionVenta
    precioA = tasacionArriendo

def main():
    propiedades=obtenerPropiedades()
    print(propiedades)
    # for prop in propiedades:
    #     tasador(prop)

if __name__ == '__main__':
    main()
