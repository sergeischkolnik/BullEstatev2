import math

from mysql import connector
from threading import Thread

import sql
from lxml import html
import requests
#import csvWrite as ew
import datetime
import time
import psycopg2
import mysql.connector
guardados=[]
a=0
from itertools import cycle
from time import sleep

# def get_proxies():
#     url = 'https://free-proxy-list.net/'
#     response = requests.get(url)
#     parser = html.fromstring(response.text)
#     proxies = set()
#     for i in parser.xpath('//tbody/tr'):
#         if i.xpath('.//td[7][contains(text(),"yes")]'):
#             #Grabbing IP and corresponding PORT
#             proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
#             proxies.add(proxy)
#     return proxies

def insertarProyecto(proyecto):
    sql = """INSERT INTO proyectos(id2,nombre,tipo,comuna,barrio,direccion,lat,lon,entrega,propietario,arquitecto,construye,vende,bodega,bdesde,bhasta,bprom,estacionamiento,edesde,ehasta,eprom,link,fechascrap)
             VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE fechascrap=%s"""


    mariadb_connection = mysql.connector.connect(user='root', password='sergei', host='127.0.0.1', database='proyectos')

    cur = mariadb_connection.cursor()
    try:
        cur.execute(sql, (proyecto))
        mariadb_connection.commit()
        mariadb_connection.close()
    except:
        mariadb_connection.commit()
        mariadb_connection.close()

def insertarDepto(propiedad):
    sql = """INSERT INTO deptos(id_proyecto,id3,numero,precio,dormitorios,banos,piso,orientacion,utiles,totales,terraza,fechascrap)
             VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE fechascrap=%s"""


    mariadb_connection = mysql.connector.connect(user='root', password='sergei', host='127.0.0.1', database='proyectos')

    cur = mariadb_connection.cursor()
    try:
        cur.execute(sql, (propiedad))
        mariadb_connection.commit()
        mariadb_connection.close()
    except:
        mariadb_connection.close()

def scraper(tipo,region,a,b):


    for i in range (a,b):

        fechahoy = datetime.datetime.now()
        fechascrap=str(fechahoy.year)+'-'+str(fechahoy.month)+'-'+str(fechahoy.day)
        try:
            link = "https://www.portalinmobiliario.com/venta/"+tipo+"/"+region+"?ca=1&ts=1&mn=1&or=&sf=0&sp=0&at=0&pg=" + str(i)
            page = requests.get(link, timeout=20)
        except:
            continue
            print("continue")



        for j in range (1,28):

            proyecto = []

            id=None
            nombre=None
            tipo=None
            comuna=None
            barrio=None
            direccion=None
            lat=None
            lon=None
            entrega=None
            propietario=None
            construye=None
            arquitecto=None
            propietario=None
            vende=None
            bodega=None
            bdesde=None
            bhasta=None
            bprom=None
            estacionamiento=None
            edesde=None
            ehasta=None
            eprom=None
            link2=None

            tree = html.fromstring(page.content)
            link2=tree.xpath('//*[@id="wrapper"]/section[2]/div/div/div[1]/article/div[3]/div['+str(j)+']/div[2]/div/div[1]/h4/a')
            try:
                link2=link2[0]
            except:
                continue
            link2=str(link2.attrib)
            link2=link2.split(': ')
            link2=link2[1]
            link2=str(link2)
            link2=link2[2:-2]
            link2 = "https://www.portalinmobiliario.com/" + link2

            try:
                page2 = requests.get(link2, timeout=30)
            except:
                continue
                print("continue")
            tree2 = html.fromstring(page2.content)

            bye=tree2.xpath('//*[@id="project-descr"]/div/div[3]/div/p')
            try:
                bye=bye[0]
                bye=bye.text
                if ("no" in bye):
                    if ("UF" in bye):
                        try:
                            byes=bye.split(' ')
                            byen=0
                            for i in byes:
                                if ("bodega" in i):
                                    if ("(desde" in byes[byen+1]):
                                        bdesde=byes[byen+3]
                                        if ("," in bdesde):
                                            bdesde=bdesde[:-1]
                                        if (")" in bdesde):
                                            bdesde=bdesde[:-1]
                                    else:
                                        bprom=byes[byen+2]
                                        if ("," in bprom) or ("." in bprom):
                                            bprom=bprom[:-1]
                                        if (")" in bprom):
                                            bprom=bprom[:-1]
                                    if ("hasta" in byes[byen+4]):
                                        bhasta=byes[byen+6]
                                        if ("," in bhasta) or ("." in bhasta):
                                            bhasta=bhasta[:-1]
                                        if (")" in bhasta):
                                            bhasta=bhasta[:-1]
                                if ("estacionamiento" in i):
                                    if ("(desde" in byes[byen+1]):
                                        edesde=byes[byen+3]
                                        if ("," in edesde) or ("." in edesde):
                                            edesde=edesde[:-1]
                                        if (")" in edesde):
                                            edesde=edesde[:-1]
                                    else:
                                        eprom=byes[byen+2]
                                        if ("," in eprom) or ("." in eprom):
                                            eprom=eprom[:-1]
                                        if (")" in eprom):
                                            eprom=eprom[:-1]
                                    if ("hasta" in byes[byen+4]):
                                        ehasta=byes[byen+6]
                                        if ("," in ehasta) or ("." in ehasta):
                                            ehasta=ehasta[:-1]
                                        if (")" in ehasta):
                                            ehasta=ehasta[:-1]
                                        if ")" in ehasta:
                                            ehasta.split(")")
                                            ehasta=ehasta[0]

                                byen=byen+1
                            bodega=0
                            estacionamiento=0
                        except:
                            bodega = 0
                            estacionamiento = 0
                    else:
                        bodega=0
                        estacionamiento=0
                else:
                    bodega=1
                    estacionamiento=1
                try:
                    bprom=(float(bdesde)+float(bhasta))/2
                except:
                    try:
                        bprom=float(bprom)
                    except:
                        bprom=None
                try:
                    eprom = (float(edesde) + float(ehasta)) / 2
                except:
                    eprom=None
                try:
                    bdesde=float(bdesde)
                except:
                    bdesde=None
                try:
                    bhasta=float(bhasta)
                except:
                    bhasta=None
                try:
                    edesde = float(edesde)
                except:
                    edesde=None
                try:
                    ehasta = float(ehasta)
                except:
                    ehasta=None
                try:
                    eprom = float(eprom)
                except:
                    eprom=None
                try:
                    bodega=float(bodega)
                except:
                    bodega=None
                try:
                    estacionamiento=float(estacionamiento)
                except:
                    estacionamiento=None
                byen=0
                byes = bye.split(' ')
                for j in byes:
                    if ("incluye") in j:
                        if ("no" not in byes[byen-1]) or (byen==0):
                            if ("estacionamiento" in byes[byen+1]):
                                estacionamiento=1
                                if ("y" in byes[byen+2]):
                                    if("bodega" in byes[byen+3]):
                                        bodega=1
                                    if("bodega" in byes[byen+4]):
                                        bodega=float(byes[byen+3])
                            if ("estacionamiento") in byes[byen+2]:
                                try:
                                    estacionamiento=float(byes[byen+1])
                                except:
                                    estacionamiento=0
                                if ("y" in byes[byen+3]):
                                    if("bodega" in byes[byen+4]):
                                        bodega=1
                                    if("bodega" in byes[byen+5]):
                                        try:
                                            bodega=float(byes[byen+4])
                                        except:
                                            bodega=0

                            if ("bodega" in byes[byen+1]):
                                bodega=1
                                if ("y" in byes[byen+2]):
                                    if("estacionamiento" in byes[byen+3]):
                                        estacionamiento=1
                                    if("estacionamiento" in byes[byen+4]):
                                        estacionamiento=float(byes[byen+3])
                            if ("bodega") in byes[byen+2]:
                                try:
                                    bodega=float(byes[byen+1])
                                except:
                                    bodega=0
                                if ("y" in byes[byen+3]):
                                    if("estacionamiento" in byes[byen+4]):
                                        estacionamiento=1
                                    if("estacionamiento" in byes[byen+5]):
                                        try:
                                            estacionamiento=float(byes[byen+4])
                                        except:
                                            estacionamiento=0

                    else:
                        byen=byen+1
            except:
                bodega=0
                estacionamiento=0


            try:
                bodega=int(bodega)
                bdesde=float(bdesde)
                bhasta=float(bhasta)
                bprom=float(bprom)
                estacionamiento=int(estacionamiento)
                edesde=float(edesde)
                ehasta=float(ehasta)
                eprom=float(eprom)
            except:
                alfa=None


            tester=tree2.xpath('//*[@id="project-descr"]/div/div[4]/div[2]/div/div[1]/strong')
            validator=4
            try:
                tester=tester[0].text
            except:
                validator=5
            for v in range (1,6):
                tester=tree2.xpath('//*[@id="project-descr"]/div/div['+str(validator)+']/div[2]/div/div['+str(v)+']/strong')
                try:
                    if("Fecha" in tester[0].text):
                        entrega=tree2.xpath('//*[@id="project-descr"]/div/div['+str(validator)+']/div[2]/div/div['+str(v)+']/text()')
                        entrega=entrega[0]
                        entrega=str(entrega)
                        entrega=entrega[1:]
                    if ("Propietario" in tester[0].text):
                        propietario =tree2.xpath('//*[@id="project-descr"]/div/div['+str(validator)+']/div[2]/div/div['+str(v)+']/text()')
                        propietario=propietario[0]
                        propietario=str(propietario)
                        propietario=propietario[1:]
                    if ("Arquitecto" in tester[0].text):
                        arquitecto=tree2.xpath('//*[@id="project-descr"]/div/div['+str(validator)+']/div[2]/div/div['+str(v)+']/text()')
                        arquitecto=arquitecto[0]
                        arquitecto=str(arquitecto)
                        arquitecto=arquitecto[1:]
                    if ("Construye" in tester[0].text):
                        construye=tree2.xpath('//*[@id="project-descr"]/div/div['+str(validator)+']/div[2]/div/div['+str(v)+']/text()')
                        construye=construye[0]
                        construye=str(construye)
                        construye=construye[1:]
                    if ("Vende" in tester[0].text):
                        vende=tree2.xpath('//*[@id="project-descr"]/div/div['+str(validator)+']/div[2]/div/div['+str(v)+']/text()')
                        vende=vende[0]
                        vende=str(vende)
                        vende=vende[1:]
                except:
                    continue

            texto=tree2.xpath('/html/body/script[7]/text()')
            try:
                texto=texto[0].split(',')
            except: continue
            b=0
            for t in texto:
                if ("lat") in t:
                    try:
                        lat=texto[b]
                        if ("Nombre") not in t:
                            lat=lat.split(': ')
                            lat=lat[1]
                            lat=lat.split(' ')
                            lat=lat[0]
                            lat=float(lat)

                            lon=texto[b+1]
                            lon=lon.split(' ')
                            lon=lon[2]
                            lon=float(lon)

                            id=texto[b+1]
                            id=id.split(':')
                            id=id[2]
                            id=int(id)

                            nombre=texto[b+2]
                            nombre=nombre.split(':')
                            nombre=nombre[1]
                            nombre=nombre[1:-1]

                            tipo=texto[b+3]
                            tipo=tipo.split(':')
                            tipo=tipo[1]
                            tipo=tipo[1:-1]

                            direccion=texto[b+5]
                            direccion=direccion.split(':')
                            direccion=direccion[1]
                            direccion=direccion[1:]
                            if "?" in texto[b+7]:
                                comuna=texto[b+6]
                                comuna=comuna[1:-1]
                            else:
                                comuna=texto[b+8]
                                comuna=comuna[1:-1]
                                barrio=texto[b+7]
                                barrio=barrio[1:]

                    except:
                        b=b+1
                        continue


                b=b+1

            a=0

            proyecto.append(id)
            proyecto.append(nombre)
            proyecto.append(tipo)
            proyecto.append(comuna)
            proyecto.append(barrio)
            proyecto.append(direccion)
            proyecto.append(lat)
            proyecto.append(lon)
            proyecto.append(entrega)
            proyecto.append(propietario)
            proyecto.append(arquitecto)
            proyecto.append(construye)
            proyecto.append(vende)
            proyecto.append(bodega)
            proyecto.append(bdesde)
            proyecto.append(bhasta)
            proyecto.append(bprom)
            proyecto.append(estacionamiento)
            proyecto.append(edesde)
            proyecto.append(ehasta)
            proyecto.append(eprom)
            proyecto.append(link2)
            proyecto.append(fechascrap)
            proyecto.append(fechascrap)
            print(len(proyecto))
            print(proyecto)
            insertarProyecto(proyecto)

            for t in texto:
                if ("Numero" in t):
                    try:
                        propiedad = []
                        n=str(texto[a])
                        try:
                            n=n.split(':')
                            n=str(n[1])
                            n=n[1:-1]
                        except:
                            n="nn"
                        try:
                            id3=(int(n)*100000)
                            id3=id3+id
                        except:
                            continue

                        precio=str(texto[a+1])
                        precio=precio.split(":")
                        precio=str(precio[1])
                        try:
                            precio=float(precio)
                        except:
                            precio=None

                        dormitorios=str(texto[a+3])
                        dormitorios=dormitorios.split(":")
                        dormitorios=str(dormitorios[1])
                        try:
                            dormitorios=int(dormitorios)
                        except:
                            dormitorios=None
                        banos=str(texto[a+4])
                        banos=banos.split(":")
                        banos=str(banos[1])
                        banos=int(banos)

                        piso=str(texto[a+5])
                        piso=piso.split(":")
                        piso=str(piso[1])
                        try:
                            piso=int(piso)
                        except:
                            piso=None
                        orientacion=str(texto[a+6])
                        orientacion=orientacion.split(":")
                        orientacion=str(orientacion[1])
                        orientacion=orientacion[1:-1]

                        util=str(texto[a+8])
                        util=util.split(":")
                        util=str(util[1])
                        try:
                            util=float(util)
                        except:
                            util=None
                        total=str(texto[a+9])
                        total=total.split(":")
                        total=str(total[1])
                        try:
                            total=float(total)
                        except:
                            total=None
                        terraza=str(texto[a+10])
                        terraza=terraza.split(":")
                        terraza=str(terraza[1])
                        try:
                            terraza=float(terraza)
                        except: terraza=None

                        propiedad.append(id)
                        propiedad.append(id3)
                        propiedad.append(n)
                        propiedad.append(precio)
                        propiedad.append(dormitorios)
                        propiedad.append(banos)
                        propiedad.append(piso)
                        propiedad.append(orientacion)
                        propiedad.append(util)
                        propiedad.append(total)
                        propiedad.append(terraza)
                        propiedad.append(fechascrap)

                        propiedad.append(fechascrap)
                        insertarDepto(propiedad)
                    except:
                        continue
                a=a+1
        sleep(5)
    sleep(120)
a=True
region=[]
tipo=[]

tipo.append("departamento")
tipo.append("casa")
tipo.append("oficina")

region.append("metropolitana")
region.append("valparaiso")
region.append("biobio")
while (a==True):
    for tip in tipo:
        for reg in region:
            threadlist=[]
            for i in range(0,70):
                a=i
                b=i+10
                t=Thread(target=scraper,args=(tip,reg,a,b))
                t.start()
                threadlist.append(t)
            for t in threadlist:
                t.join()
