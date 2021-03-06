
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
ufn=uf.getUf()

def obtenerPropiedades():
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT nombre,region,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,estacionamientos,bodegas,lat,lon,link,id2 from portalinmobiliario inner join duenos " \
          "WHERE portalinmobiliario.id2=duenos.idProp AND portalinmobiliario.fechascrap>='"+str(yesterday)+"' AND (duenos.mail='contacto@vendetudepto.cl' or duenos.mail='carolina@vendetudepto.cl' or duenos.mail='daniela@vendetudepto.cl' or duenos.mail='pablo@vendetudepto.cl') and portalinmobiliario.operacion='venta' and portalinmobiliario.tipo='departamento'"
    cur.execute(sql)
    propiedad = cur.fetchall()
    if len(propiedad)>0:
        return propiedad
    else:
        return 0


def tasador(propiedad):
    regYapoDict={
        "metropolitana":"15",
        "valparaiso":"6",
        "Valparaíso":"6",
        "arica":"1",
        "iquique":"2",
        "antofagasta":"3",
        "atacama":"4",
        "coquimbo":"5",
        "ohiggins":"7",
        "maule":"8",
        "ñuble":"16",
        "biobio":"9",
        "araucania":"10",
        "los Rios":"11",
        "los Lagos":"12",
        "aysen":"13",
        "magallanes":"14",

        }
    region=str(propiedad[1])
    regionP=region
    regionY=regYapoDict[region.lower()]

    operacion=str(propiedad[2])
    tipo=str(propiedad[3])
    precio=float(propiedad[4])
    dormitorios=(propiedad[5])
    banos=(propiedad[6])
    metrosmin=(propiedad[7])
    metrosmax=(propiedad[8])
    estacionamientos=(propiedad[9])
    bodegas=str(propiedad[10])
    lat=(propiedad[11])
    lon=(propiedad[12])
    link=str(propiedad[13])
    id=str(propiedad[14])

    if operacion=='venta':
        comuna=str(link.split('/')[5])
        comuna=comuna.replace('-'+str(regionP),'')
        comuna=comuna.replace('-',' ')
        comuna=comuna.capitalize()

    else:
        comuna=str(link.split('/')[6])
        comuna=comuna.replace('-metropolitana','')
        comuna=comuna.replace('-',' ')
        comuna=comuna.capitalize()

    #Revisar si existe aun la publicacion
    if not pubPortalExiste.publicacionExiste(link):
        text='Propiedad ya no se encuentra disponible en el sitio.'
        return(text)

    propsPV = reportes.from_portalinmobiliario(tipo,region,[comuna],"venta",True)
    propsYV = reportes.from_yapo(tipo,regionY,[comuna],True,"venta",True)
    propsV = propsPV + propsYV
    # aca deberiamos hacer el GB

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


    clfHV.fit(trainingV, preciosV)

    propsPA = reportes.from_portalinmobiliario(tipo,region,[comuna],"arriendo",True)
    propsYA = reportes.from_yapo(tipo,regionY,[comuna],True,"arriendo",True)
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


    clfHA.fit(trainingA, preciosA)

    tasacionVenta = clfHV.predict([[int(dormitorios),int(banos), int(metrosmin),int(metrosmax), lat,lon, int(estacionamientos)]])
    tasacionArriendo = clfHA.predict([[int(dormitorios),int(banos), int(metrosmin),int(metrosmax), lat,lon, int(estacionamientos)]])

    precioV = tasacionVenta
    precioA = tasacionArriendo
    try:

        return(precioV,precioA)
    except Exception as e:
        return e,e

def main():
    propiedades=obtenerPropiedades()
    textprint=""
    c=0
    for prop in propiedades:
        c+=1
        print(str(c)+"/"+str(len(propiedades)))
        if prop[3]=='departamento' and prop[2]=='venta':
            try:
                tasacion=tasador(prop)
                textprint+="\nId Prop: "+str(prop[14])+" Precio: "+str(int(prop[4]/ufn))+" Tasacion: "+str(int(tasacion[0]/ufn))
                if tasacion[0]>prop[4]:
                    rent=(tasacion[0]-prop[4])/tasacion[0]
                    rent=rent*100
                    rent=int(rent)
                    textprint+="\nLa propiedad está un "+str(rent)+"% BAJO precio de mercado."
                elif tasacion[0]<prop[4]:
                    rent=(-tasacion[0]+prop[4])/tasacion[0]
                    rent=rent*100
                    rent=int(rent)
                    textprint+="\nLa propiedad está un "+str(rent)+"% SOBRE precio de mercado."
                else:
                    pass
                    textprint+="\nLa propiedad está a precio de mercado."
            except Exception as e:
                pass
    sendmail.sendMailText("sergei.schkolnik@gmail.com","Sergei",textprint)
if __name__ == '__main__':
    main()
