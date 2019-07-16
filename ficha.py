import math
import pymysql as mysql
from math import radians, sin, cos, acos, asin,pi,sqrt
from datetime import datetime, timedelta, date
past = datetime.now() - timedelta(days=180)
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
from xlsxWriter import writeXlsx
import os
import bot1 as tgbot
import googleMapApi as gm
import datetime
fechahoy = datetime.datetime.now()
fechahoy=str(fechahoy.year)+'-'+str(fechahoy.month)+'-'+str(fechahoy.day)
uf1=uf.getUf()
import math
from lxml import html
import requests
import datetime
from threading import Thread
import pymysql as mysql
from itertools import cycle
import agentCreator
import time
import random
from requests_html import HTMLSession
session = HTMLSession()
from PIL import Image
from io import BytesIO
import pdfCreatorFichas

def obtenerProp(id,sitio):

    if (sitio=='portal'):
        mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
        cur = mariadb_connection.cursor()
        sql = "SELECT nombre,region,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,estacionamientos,bodegas,lat,lon,link from portalinmobiliario WHERE id2="+str(id)
    else:
        mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='yapo')
        cur = mariadb_connection.cursor()
        sql = "SELECT nombre,region,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,estacionamientos,bodegas,lat,lon,link,comuna from propiedades WHERE id2="+str(id)
    cur.execute(sql)
    propiedad = cur.fetchall()
    return propiedad[0]


def crearFicha(sitio,id,mail):

    #Chequear que sitio este bien
    sitio=sitio.lower()

    if('portal' in sitio):
        sitio='portal'
    elif('yapo' in sitio):
        sitio='yapo'
    else:
        text='Sitio ingresado es incorrecto. Favor ingresar portalinmobiliario o yapo.'
        return(text)
    #Chequear que mail este bien
    if ('@' not in mail):
        text='Email incorrecto. Favor ingresar correo válido.'
        return(text)
    if ('.' not in mail):
        text='Email incorrecto. Favor ingresar correo válido.'
        return(text)

    #sacar informacion de bbdd, y chequear que propiedad existe:
    propiedad=obtenerProp(id,sitio)
    propiedad=list(propiedad)
    if len(propiedad)<1:
        text='¨Propiedad no se encuentra en la base de datos.'
        return(text)
    else:


        nombre=str(propiedad[0])
        region=str(propiedad[1])
        operacion=str(propiedad[2])
        tipo=str(propiedad[3])
        precio=str(propiedad[4])
        dormitorios=str(propiedad[5])
        banos=str(propiedad[6])
        metrosmin=str(propiedad[7])
        metrosmax=str(propiedad[8])
        estacionamientos=str(propiedad[9])
        bodegas=str(propiedad[10])
        lat=str(propiedad[11])
        lon=str(propiedad[12])
        link=str(propiedad[13])
        if sitio=='portal':
            if operacion=='venta':
                comuna=str(link.split('/')[5])
                comuna=comuna.replace('-metropolitana','')
                comuna=comuna.replace('-',' ')
                comuna=comuna.capitalize()
            else:
                comuna=str(link.split('/')[6])
                comuna=comuna.replace('-metropolitana','')
                comuna=comuna.replace('-',' ')
                comuna=comuna.capitalize()
        else:
            comuna=str(propiedad[14])


    #Revisar si existe aun la publicacion
    if not pubPortalExiste.publicacionExiste(link):
        text='Propiedad ya no se encuentra disponible en el sitio.'
        return(text)
    #sacar informacion de la publicacion
    #sacar urls fotos portal
    if sitio=='portal':
        url=[]
        page = requests.get(link, headers={'User-Agent': agentCreator.generateAgent()})
        metatext=page.text
        metatext=metatext.split(' ')
        for meta in metatext:
            if 'https://image.portalinmobiliario.cl/Portal/Propiedades' in meta and '1200' in meta:
                meta=meta.split('"')

                url.append(str(meta[1]))
     #Sacar urls fotos yapo
    else:
        text='aun no se desarrolla Yapo'
        return (text)
    #Sacar fotos de urls
    if len(url)==0:
        print("la propiedad no cuenta con fotografias")
    else:
        for x,u in enumerate (url):
            response = requests.get(u)
            img = Image.open(BytesIO(response.content))
            img.save(str(x)+" foto.jpg")
    lenfotos=len(url)
    #Crear PDF
    nombrearchivo="Ficha Propiedad Sitio:"+str(sitio)+" Id:"+str(id)+".pdf"
    print(nombrearchivo)
    pdfCreatorFichas.crearPdfFicha(nombrearchivo,id,propiedad,lenfotos,comuna)
    print("pdf generado con exito")
    #Enviar PDF
    sendmail.sendMail(mail,"",nombrearchivo)

    #Eliminar del servidor

    if len(url)==0:
        pass
    else:
        for x,u in enumerate (url):
            os.remove(str(x)+" foto.jpg")

    os.remove(nombrearchivo)

    #Retornar exito
    text = "Ficha creada para la propiedad: "+str(id)+" obtenida del sitio: "+str(sitio)+", enviada con éxito al correo: "+str(mail)+"."
    return(text)


def main():
    texto=crearFicha('portal',4927298,'sergei.schkolnik@gmail.com')
    print(texto)

if __name__ == '__main__':
    main()