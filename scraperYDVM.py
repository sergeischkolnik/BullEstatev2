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
from yapo_ocr import yapo_ocr
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import os


def actualizar_checker(operacion,tipo,region,pagina):
    d=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sql = "UPDATE checker SET lastscrap='"+str(d)+"',operacion='" + operacion + "',tipo='"+ tipo +"',region='"+ region +"',pagina="+str(pagina)+" WHERE nombrescraper='sydvm'"
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')

    cur = mariadb_connection.cursor()

    try:
        cur.execute(sql)
        mariadb_connection.commit()
    except:
        pass

    mariadb_connection.close()

def insertarPropiedad(propiedad):
    #Inserta una propiedad en una base de datos

    sql = """INSERT INTO propiedades(id2,idregion,comuna,tipo,titulo,operacion,preciouf,preciopesos,fechapublicacion,
             fechascrap,metrosmin,metrosmax,dormitorios,banos,estacionamientos,descripcion,lat,lon,anoconstruccion,ggcc,link,esdueno,telefono)
             VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE idregion=%s,
             comuna=%s,tipo=%s,titulo=%s,operacion=%s,preciouf=%s,preciopesos=%s,fechapublicacion=%s,fechascrap=%s,
             metrosmin=%s,metrosmax=%s,dormitorios=%s,banos=%s,estacionamientos=%s,descripcion=%s,lat=%s, lon=%s, 
             anoconstruccion=%s, ggcc=%s, link=%s, esDueno=%s, telefono=%s"""

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='yapo')

    cur = mariadb_connection.cursor()
    cur.execute(sql, (propiedad))

    mariadb_connection.commit()
    mariadb_connection.close()


def main(tipoRec="departamento",operacionRec="venta", regionRec="metropolitana",pagRec=1,isRecovery=False,ocr=None):



    while(True):
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

        if isRecovery:
            isRecovery = False
            ran = range(pagRec,last)
        else:
            ran = range(1,last)

        for i in ran:


            link2='https://www.yapo.cl/region_metropolitana/comprar?ca=15_s&ret=1&cg=1220&o='+str(i)
            session = HTMLSession()
            r = session.get(link2)
            links3 = []
            duenos = []

            for a in r.html.find('.title'):
                list = []
                links3.append(a.links.pop())

            for piece in r.html.find('.clean_links'):
                company_ad = piece.find('.company_ad')
                duenos.append(len(company_ad) == 0)

            props = zip(links3,duenos)

            for link3,dueno in props:

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
                estacionamientos = 0

                esdueno = 0

                if dueno:
                    esdueno = 1


                page = requests.get(link3, headers={'User-Agent': agentCreator.generateAgent()})
                tree = html.fromstring(page.content)

                url=[]
                metatext=page.text
                metatext=metatext.split(' ')
                descripcion=[]
                savedescripcion=False
                saveimg=False
                og=True

                for texto in metatext:


                    if og and 'og:image' in texto:
                        saveimg=True
                        og=False
                    if 'img/yapo' in texto:
                        saveimg=False

                    if saveimg and 'img.yapo.cl/images' in texto:
                        texto=texto.replace('content="','')
                        texto.replace('"','')
                        url.append(texto)
                    if 'phone-url' in texto:
                        texto=texto.split('"')
                        texto=texto[1]
                        auxPhone=texto
                        auxPhone='https://www.yapo.cl'+auxPhone

                # try:
                #     response = requests.get(auxPhone, headers={'User-Agent': agentCreator.generateAgent()})
                #     img = Image.open(BytesIO(response.content))
                #     img.save("auxphone.gif")
                #     telefono=ocr("auxphone.gif")
                # except:
                #     telefono='NN'

                telefono = 'NN'

                precio1=tree.xpath('//*[@id="content"]/section[1]/article/div[5]/div[1]/table/tbody/tr[1]/td/div/strong')
                precio2=tree.xpath('//*[@id="content"]/section[1]/article/div[5]/div[1]/table/tbody/tr[1]/td/div/span/span')

                if len(precio1) < 0:
                    continue

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

                utag_data = tree.xpath("/html/body/script[1]/text()")[0]
                text = str(utag_data.split('=')[1])
                text = text[:-5] + "}"

                try:
                    value = json.loads(text)
                except:
                    continue


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
                    dormitorios = int(value["rooms"])
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
                        ggcc = row.find("td").text[2:]
                        ggcc = ggcc.replace('.','')
                        ggcc = float(ggcc)


                propiedad = []
                propiedad.append(codigo)
                propiedad.append(idregion)
                propiedad.append(comuna)
                propiedad.append(tipo.lower())
                propiedad.append(titulo)
                propiedad.append(operacion.lower())
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
                propiedad.append(link3)
                propiedad.append(esdueno)
                propiedad.append(telefono)

                propiedad.append(idregion)
                propiedad.append(comuna)
                propiedad.append(tipo.lower())
                propiedad.append(titulo)
                propiedad.append(operacion.lower())
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
                propiedad.append(link3)
                propiedad.append(esdueno)
                propiedad.append(telefono)

                insertarPropiedad(propiedad)
                try:
                    os.remove("auxphone.gif")
                except:
                    pass
                print("[SYDVM] insertada propiedad id:" + str(propiedad[0]) + " " +str(i) + "/" + str(last))

                time.sleep(random.uniform(1, 1.5))

            actualizar_checker(operacion='venta',tipo='departamento',region='15',pagina=i)



if __name__=="__main__":
    #ocr=yapo_ocr()
    main(tipoRec="departamento",operacionRec="venta", regionRec="metropolitana",pagRec=1,isRecovery=False)
