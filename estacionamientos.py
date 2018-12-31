import math
import sql
from lxml import html
import requests
#import csvWrite as ew
import datetime
import time
from lxml.html import fromstring
from threading import Thread
import psycopg2
import mysql.connector
estacionamientos=0
bodegas=0
link="https://www.portalinmobiliario.com/venta/departamento/santiago-metropolitana/4410322-vicuna-mackenna-con-avenida-matta-uda?tp=2&op=1&iug=305&ca=2&ts=1&mn=2&or=&sf=1&sp=0&at=0&i=282"
page=requests.get(link,)
tree=html.fromstring(page.content)
texts=[]
for p in range (1,20):
    try:
        path='//*[@id="wrapper"]/section/div/div/div[1]/article/div/div[2]/div[2]/div[3]/div/div/text()['+str(p)+']'
        texto=tree.xpath(path)
        texto=texto[0]
        texto=str(texto)

        texts.append(texto)

    except:
        continue

for texto in texts:
    if 'Estacionamientos: 1' in texto:
            estacionamientos=1
            break
    elif 'Estacionamientos: 2' in texto:
        estacionamientos=2
        break
    elif 'Estacionamientos: 3' in texto:
        estacionamientos=3
        break
    elif ('estaciomamiento' in texto) or ('Estacionamiento' in texto) or ('ESTACIONAMIENTO' in texto):
        estacionamientos=1
        if (('INCLUYE' in texto) or ('Incluye' in texto) or ('incluye' in texto)) and (('ESTACIONAMIENTO' in texto) or ('Estacionamiento' in texto) or ('estacionamiento' in texto)):
            if (('No' in texto) or ('NO' in texto) or ('no' in texto)):
                estacionamientos=0
            elif (('Ni' in texto) or ('NI' in texto) or ('ni' in texto)):
                estacionamientos=0
            else:
                 estacionamientos=1

        elif (('TIENE' in texto) or ('Tiene' in texto) or ('tiene' in texto)) and (('ESTACIONAMIENTO' in texto) or ('Estacionamiento' in texto) or ('estacionamiento' in texto)):
            if (('No' in texto) or ('NO' in texto) or ('no' in texto)):
                estacionamientos=0
            elif (('Ni' in texto) or ('NI' in texto) or ('ni' in texto)):
                estacionamientos=0
            else:
                 estacionamientos=1

        elif ('Visita' in texto) or ('visita' in texto) or ('VISITA' in texto):
             estacionamientos=0

        #elif ('' in texto) or ('' in texto) or ('' in texto) or ('' in texto) or ('' in texto) or ('' in texto):
        else:
            if (('Sin' in texto) or ('SIN' in texto) or ('sin' in texto)):
                estacionamientos=0
            #elif (('Ni' in texto) or ('NI' in texto) or ('ni' in texto)):
                #estacionamientos=0
            else:
                 estacionamientos=1

        break


print(estacionamientos)
