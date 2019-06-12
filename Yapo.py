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
import json

def insertarPropiedad(propiedad):
    #Inserta una propiedad en una base de datos

    sql = """INSERT INTO propiedades(id2,idregion,comuna,tipo,titulo,operacion,preciouf,preciopesos,fechapublicacion,
    fechascrap,metrosmin,metrosmax,dormitorios,banos,estacioanmieINSERT INTO propiedades(id2,idregion,comuna,tipo,titulo,operacion,preciouf,preciopesos,fechapublicacion,
    fechascrap,metrosmin,metrosmax,dormitorios,banos,estacionamientos,descripcion,lat,lon,anoconstruccion,ggcc,link)
             VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE idregion=%s,
             comuna=%s,tipo=%s,titulo=%s,operacion=%s,preciouf=%s,preciopesos=%s,fechapublicacion=%s,fechascrap=%s,
             metrosmin=%s,metrosmax=%s,dormitorios=%s,banos=%s,estacionamientos=%s,descripcion=%s,lat=%s, lon=%s, 
             anoconstruccion=%s, ggcc=%s, link=%s"""

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='yapo')

    cur = mariadb_connection.cursor()
    cur.execute(sql, (propiedad))

    mariadb_connection.commit()
    mariadb_connection.close()
    print("[scraperYapo] insertada propiedad:" + str(propiedad[0]))


def main():

    link='https://www.yapo.cl/region_metropolitana/comprar?ca=15_s&ret=1&cg=1220&o=1'
    page = requests.get(link, headers={'User-Agent': agentCreator.generateAgent()})
    tree = html.fromstring(page.content)
    last=tree.xpath('//*[@id="tabnav"]/li[2]/h2/span[2]')
    last=last[0].text
    last=last.split(' ')
    last=last[5]
    last=last.replace('.','')
    last=int(last)
    last=int(last/50)+1



    for i in range(1,last):

        link2='https://www.yapo.cl/region_metropolitana/comprar?ca=15_s&ret=1&cg=1220&o='+str(i)
        session = HTMLSession()
        r = session.get(link2)
        links3 = []

        for a in r.html.find('.title'):
            links3.append(a.links.pop())

        for link3 in links3:

            codigo = -1
            idregion = -1
            comuna = ""
            tipo = ""
            titulo = ""
            operacion=""
            preciouf = -1
            preciopesos= -1
            fechapublicacion = ""
            fechahoy = datetime.datetime.now()
            fechascrap=str(fechahoy.year)+'-'+str(fechahoy.month)+'-'+str(fechahoy.day)
            metrosmin = -1
            metrosmax = -1
            dormitorios = -1
            banos = -1
            descripcion = ""
            lat = -999
            lon = -999
            anoconstruccion = -1
            ggcc = -1
            estacionamientos = -1


            page = requests.get(link3, headers={'User-Agent': agentCreator.generateAgent()})
            tree = html.fromstring(page.content)
            precio1=tree.xpath('//*[@id="content"]/section[1]/article/div[5]/div[1]/table/tbody/tr[1]/td/div/strong')
            precio2=tree.xpath('//*[@id="content"]/section[1]/article/div[5]/div[1]/table/tbody/tr[1]/td/div/span/span')
            if ('$') in precio2[0].text:
                preciopesos=precio2[0].text
                preciouf=precio1[0].text
            else:
                preciopesos=precio1[0].text
                preciouf=precio2[0].text

            preciopesos=preciopesos.replace('.','')
            preciopesos=preciopesos.replace('$','')
            preciopesos=preciopesos.replace(' ','')
            preciopesos=preciopesos.replace(')','')
            preciopesos=preciopesos.replace('(','')
            preciopesos=preciopesos.replace('*','')
            preciopesos=int(preciopesos)

            preciouf=preciouf.replace('.','')
            preciouf=preciouf.replace('$','')
            preciouf=preciouf.replace(' ','')
            preciouf=preciouf.replace(')','')
            preciouf=preciouf.replace('(','')
            preciouf=preciouf.replace('*','')
            preciouf=preciouf.replace('UF','')
            preciouf=preciouf.replace(',','.')
            preciouf=float(preciouf)

            #extraccion codigo
            aux = link3.split('.')
            aux = aux[-2]
            aux = aux.split('_')
            codigo = int(aux[-1])
            print("codigo:" + str(codigo) + "-> " + str(link3))

            utag_data = tree.xpath("/html/body/script[1]/text()")[0]
            text = str(utag_data.split('=')[1])
            text = text[:-5] + "}"

            value = json.loads(text)


            try:
                idregion = value["region_level2_id"].lower()
            except:
                pass
            try:
                comuna = value["region_level3"].lower()
            except:
                pass
            try:
                titulo = value["ad_title"].lower()
            except:
                pass
            try:
                if value["category_level2"]=="Vendo":
                    operacion = "venta"
                elif value["category_level2"]=="Arriendo":
                    operacion = "arriendo"
                elif value["category_level2"]=="Arriendo de temporada":
                    operacion = "temporada"
            except:
                pass
            try:
                fechapublicacion = value["publish_date"].split(' ')[0]
            except:
                pass
            try:
                dormitorios = int(value["roms"])
            except:
                pass
            try:
                descripcion = value["description"]
            except:
                pass

            try:
                if int(value["geoposition_is_precise"]) == 1:
                    pos = value["geoposition"].split(',')
                    lat = float(pos[0])
                    lon = float(pos[1])
            except:
                pass

            tabla = tree.xpath("""//*[@id="content"]/section[1]/article/div[5]/div[1]/table/tbody/tr""")
            tabla.pop(0)

            for row in tabla:
                rowname = row.find("th").text
                if rowname == "Tipo de inmueble":
                    tipo = row.find("td").text
                elif rowname == "Superficie total":
                    metrosmax = row.find("td").text.replace('\n','').replace('\t','').split(' ')[0]
                elif rowname == "Superficie útil" or rowname == "Superficie construida":
                    metrosmin = row.find("td").text.replace('\n','').replace('\t','').split(' ')[0]
                elif rowname == "Baños":
                    banos = row.find("td").text
                    banos = int(str(banos.split(' ')[0]))
                elif rowname == "Estacionamiento":
                    estacionamientos = row.find("td").text
                elif rowname == "Año de construcción":
                    anoconstruccion = row.find("td").text
                elif rowname == "Gastos comunes":
                    ggcc = row.find("td")[2:]
                    ggcc.replace('.',' ')
                    ggcc = float(ggcc)

            propiedad = []
            propiedad.append(codigo)
            propiedad.append(idregion)
            propiedad.append(comuna)
            propiedad.append(tipo)
            propiedad.append(titulo)
            propiedad.append(operacion)
            propiedad.append(preciouf)
            propiedad.append(preciopesos)
            propiedad.append(fechapublicacion)
            propiedad.append(fechascrap)
            propiedad.append(metrosmin)
            propiedad.append(metrosmax)
            propiedad.append(dormitorios)
            propiedad.append(banos)
            propiedad.append(estacionamientos)
            propiedad.append(descripcion)
            propiedad.append(lat)
            propiedad.append(lon)
            propiedad.append(anoconstruccion)
            propiedad.append(ggcc)
            propiedad.append(link)
            propiedad.append(idregion)
            propiedad.append(comuna)
            propiedad.append(tipo)
            propiedad.append(titulo)
            propiedad.append(operacion)
            propiedad.append(preciouf)
            propiedad.append(preciopesos)
            propiedad.append(fechapublicacion)
            propiedad.append(fechascrap)
            propiedad.append(metrosmin)
            propiedad.append(metrosmax)
            propiedad.append(dormitorios)
            propiedad.append(banos)
            propiedad.append(estacionamientos)
            propiedad.append(descripcion)
            propiedad.append(lat)
            propiedad.append(lon)
            propiedad.append(anoconstruccion)
            propiedad.append(ggcc)
            propiedad.append(link)

            insertarPropiedad(propiedad)
            time.sleep(random.uniform(1, 1.5))



if __name__=="__main__":
    main()