import scraperPortalML_OR
from datetime import datetime, timedelta, date
import time
import random
past = datetime.now() - timedelta(days=180)
past=datetime.date(past)
yesterday = datetime.now() - timedelta(days=10)
yesterday=datetime.date(yesterday)
import uf
import numpy as np
from sklearn import datasets, linear_model
import sendmail
import tasadorbot2 as tb2
import pubPortalExiste
import os
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
import agentCreator
from requests_html import HTMLSession
session = HTMLSession()
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import pdfCreatorFichasv2 as pdfCreatorFichas
import reportesHuberV1 as reportes
import pubYapoExiste
import json

from sklearn import ensemble
from sklearn.model_selection import train_test_split

headers = {
    'authority': 'www.portalinmobiliario.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    'sec-fetch-user': '?1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'referer': 'https://www.portalinmobiliario.com/',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'es-US,es;q=0.9,es-419;q=0.8,en;q=0.7',
    'cookie': '_d2id=2f52a2ad-2dc1-4db9-ba16-afa9d3030d06-n; _csrf=znVPWlbzP11aMD2-q_Mmr8tQ; c_home=0.20.0%7C5.3.3; pin_d2id=; pin_exp=new; _d2id=2f52a2ad-2dc1-4db9-ba16-afa9d3030d06; _pi_ga=GA1.2.346434101.1572221445; _pi_ga_gid=GA1.2.700821714.1572221445; _pi_ci=346434101.1572221445; _hjid=df262c46-fd11-46f6-9807-0d9cd4bd7878; searchbox-currentSearch=eyJvcGVyYXRpb25zIjp7ImxhYmVsIjoiVmVudGEiLCJzZWxlY3RlZCI6InZlbnRhIn0sImNhdGVnb3JpZXMiOnsibGFiZWwiOiJEZXBhcnRhbWVudG9zIiwic2VsZWN0ZWQiOiJ2ZW50YV9kZXBhcnRhbWVudG8ifSwibG9jYXRpb24iOnsidmFsdWUiOiJWYWxwYXJh7XNvIiwic2VsZWN0ZWQiOiJUVXhEVUZaQlRFODRNRFZqIn0sImZpbHRlci1uZXciOnsiY2hlY2tlZCI6ZmFsc2UsImRpc2FibGVkIjpmYWxzZX19; _mlt=6a66608b-edb2-40c7-bb49-6a89232f6276',
}
def obtainPropFromPortal(link):

    try:
        request = requests.get(link, headers=headers)
        operacion=(request.request.url.split("/")[3])
        tipo=(request.request.url.split("/")[3])
        region=(request.request.url.split("/")[5]).split("-")[1]
    except:
        time.sleep(random.randint(60,90))
        request = requests.get(link, headers=headers)
        return False

    try:
        tree = html.fromstring(request.content)
    except:
        #   print("Fallo.")
        return False

    priceSymbolPath = '//*[@id="productInfo"]/fieldset/span/span[1]'

    pricePath = '//*[@id="productInfo"]/fieldset/span/span[2]'
    namePath = '//*[@id="short-desc"]/div/header/h1'
    addressPath = '//*[@id="root-app"]/div/div/div[1]/div[3]/section/div[1]/div/h2'

    priceSymbol = tree.xpath(priceSymbolPath)
    if len(priceSymbol) == 0:
        return False
    priceSymbol = priceSymbol[0].text
    price = tree.xpath(pricePath)
    if len(price) == 0:
        return False
    price = int(price[0].text.replace(',','').replace(' ','').replace('.',''))

    if priceSymbol == 'UF':
        price = price*uf

    name = tree.xpath(namePath)
    if len(name) == 0:
        return False
    name = name[0].text.replace('\n','').replace('\t','')

    address =  tree.xpath(addressPath)
    if len(address) == 0:

        address = '-'
    else:
        address = address[0].text

    #fecha
    datePosition = request.text.find('<p class="title">Fecha de Publicación</p>')
    if datePosition == -1:

        date = "00-00-0000"
    else:
        date = request.text[datePosition+60:datePosition+70]
        dateSplit = date.split('-')
        date = dateSplit[2] + '-' + dateSplit[1] + '-' + dateSplit[0]

    #metraje, estacionamientos, bodegas
    htmlArray = request.text.split('<li class="specs-item">')
    maxMeters = 0
    minMeters = 0
    estacionamientos = 0
    bodegas = 0

    minMetersFound = maxMetersFound = estacionamientosFound = bodegasFound = False

    try:
        for j, element in enumerate(htmlArray):
            if j == len(htmlArray)-1:
                #last element, we have to split again.
                element = element.split('</ul>')[0]
            if "Superficie total" in element and not maxMetersFound:
                maxMeters = int(float(element.split('span')[1][1:-5]))
                maxMetersFound = True
            elif "Superficie útil" in element and not minMetersFound:
                minMeters = element.split('span')[1][1:-5]
                minMetersFound = True
            elif "Estacionamientos" in element and not estacionamientosFound:
                estacionamientos = int(float(element.split('span')[1].replace('<','').replace('>','').replace('/','')))
                estacionamientosFound = True
            elif "Bodegas" in element and not bodegasFound:
                bodegas = int(float(element.split('span')[1].replace('<','').replace('>','').replace('/','')))
                bodegasFound = True
    except:
        return False


    if maxMeters != 0 and minMeters == 0:
        minMeters = maxMeters
    if minMeters != 0 and maxMeters == 0:
        maxMeters = minMeters

    #baños y dormitorios
    try:
        item1xpath = '//*[@id="productInfo"]/div[1]/dl[1]/dd'
        item2xpath = '//*[@id="productInfo"]/div[1]/dl[2]/dd'
        item3xpath = '//*[@id="productInfo"]/div[1]/dl[3]/dd'
        itemUniquexpath = '//*[@id="productInfo"]/div[1]/dl/dd'

        item1 = tree.xpath(item1xpath)
        item2 = tree.xpath(item2xpath)
        item3 = tree.xpath(item3xpath)
        itemU = tree.xpath(itemUniquexpath)

        item1 = item1[0].text if len(item1) > 0 else ''
        item2 = item2[0].text if len(item2) > 0 else ''
        item3 = item3[0].text if len(item3) > 0 else ''
        itemU = itemU[0].text if len(itemU) > 0 else ''

        if "dormitorio" in item1:
            dorms = int(item1.split(' ')[0])
        elif "dormitorio" in item2:
            dorms = int(item2.split(' ')[0])
        elif "dormitorio" in item3:
            dorms = int(item3.split(' ')[0])
        elif "dormitorio" in itemU:
            dorms = int(itemU.split(' ')[0])
        elif "priva" in item1:
            dorms = int(item1.split(' ')[0])
        elif "priva" in item2:
            dorms = int(item2.split(' ')[0])
        elif "priva" in item3:
            dorms = int(item3.split(' ')[0])
        elif "priva" in itemU:
            dorms = int(itemU.split(' ')[0])
        else:
            dorms = 0

        if "baño" in item1:
            baths = int(item1.split(' ')[0])
        elif "baño" in item2:
            baths = int(item2.split(' ')[0])
        elif "baño" in item3:
            baths = int(item3.split(' ')[0])
        elif "baño" in itemU:
            baths = int(itemU.split(' ')[0])
        else:
            baths = 0
    except:
        return False


    #lat, lon
    mapPosition = request.text.find("center=")
    if mapPosition == -1:

        lat = 0
        lon = 0
    else:
        amperPosition = request.text[mapPosition:].find('&')
        mapTexts = request.text[mapPosition:mapPosition+amperPosition].replace("center=",'').split('%2C')
        lat = float(mapTexts[0])
        lon = float(mapTexts[1])

    fechascrap = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day)

    propiedad = []

    try:
        code = int(link.split('/')[6].split('-')[0])
    except Exception as err:
        try:
            code = int(link.split('/')[3].split('-')[1])
        except Exception as err2:
            return False

    #text mining para bodegas
    if bodegas == 0:
        descripcion_xpath  = '//*[@id="description-includes"]/div/p'
        descripcion_result = tree.xpath(descripcion_xpath)
        if len(descripcion_result)>0:
            bodegas = scraperPortalML_OR.obtenerBodegas(descripcion_result[0].text)

    # text mining para estacionamientos
    if estacionamientos == 0:
        descripcion_xpath = '//*[@id="description-includes"]/div/p'
        descripcion_result = tree.xpath(descripcion_xpath)
        if len(descripcion_result) > 0:
            estacionamientos = scraperPortalML_OR.obtenerBodegas(descripcion_result[0].text)

    sql = "SELECT nombre,region,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,estacionamientos,bodegas,lat,lon,link from portalinmobiliario WHERE id2="+str(id)


    propiedad.append(name)
    propiedad.append(region)
    propiedad.append(operacion)
    propiedad.append(tipo)
    propiedad.append(price)
    propiedad.append(dorms)
    propiedad.append(baths)
    propiedad.append(minMeters)
    propiedad.append(maxMeters)
    propiedad.append(estacionamientos)
    propiedad.append(bodegas)
    propiedad.append(lat)
    propiedad.append(lon)
    propiedad.append(link)

    return propiedad

def obtainPropFromYapo(link):

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

        page = requests.get(link, headers={'User-Agent': agentCreator.generateAgent()})
        tree = html.fromstring(page.content)

        url=[]
        metatext=page.text
        metatext=metatext.split(' ')
        descripcion=[]
        savedescripcion=False
        saveimg=False
        og=True
        telefono = 'NN'

        precio1=tree.xpath('//*[@id="content"]/section[1]/article/div[5]/div[1]/table/tbody/tr[1]/td/div/strong')
        precio2=tree.xpath('//*[@id="content"]/section[1]/article/div[5]/div[1]/table/tbody/tr[1]/td/div/span/span')

        '//*[@id="content"]/section[1]/article/div[5]/div[1]/table/tbody/tr[1]/td/div/strong'
        '//*[@id="content"]/section[1]/article/div[5]/div[1]/table/tbody/tr[1]/td/div/span/span'

        if len(precio1)<0:
            return False

        if len(precio2) == 0:
            print("Error al sacar el precio en " + link)
            return False

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
        aux = link.split('.')
        aux = aux[-2]
        aux = aux.split('_')
        codigo = int(aux[-1])

        utag_data = tree.xpath("/html/body/script[1]/text()")[0]
        text = str(utag_data.split('=')[1])
        text = text[:-5] + "}"

        try:
            value = json.loads(text)
        except:
            return False


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


        try:
            propiedad = []
            propiedad.append(titulo)
            propiedad.append(idregion)
            propiedad.append(operacion.lower())
            propiedad.append(tipo.lower())
            propiedad.append(preciopesos)
            propiedad.append(int(float(dormitorios)))
            propiedad.append(int(float(banos)))
            propiedad.append(int(float(metrosmin)))
            propiedad.append(int(float(metrosmax)))
            propiedad.append(int(float(estacionamientos)))
            propiedad.append(int(float(estacionamientos)))
            propiedad.append(lat)
            propiedad.append(lon)
            propiedad.append(link)
            propiedad.append(comuna)
            return propiedad
        except Exception as err:
            print("Error en propiedad:" + link + " \n " + str(err))
            return False


def obtenerProp(id,sitio):

    if 'portal' in sitio:
        mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
        cur = mariadb_connection.cursor()
        sql = "SELECT nombre,region,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,estacionamientos,bodegas,lat,lon,link from portalinmobiliario WHERE id2="+str(id)
    else:
        mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='yapo')
        cur = mariadb_connection.cursor()
        sql = "SELECT titulo,idregion,operacion,tipo,preciopesos,dormitorios,banos,metrosmin,metrosmax,estacionamientos,estacionamientos,lat,lon,link,comuna from propiedades WHERE id2="+str(id)
    print(sql)
    cur.execute(sql)
    propiedad = cur.fetchall()
    if len(propiedad)>0:
        return propiedad[0]
    else:
        return propiedad

def crearFicha(sitio,id,mail,tipoficha):
    links=[]
    text2=''
    auxPhone=0
    #Determinar tipo de informe
    pro=False
    interna=False
    financiera=False
    textmail=''
    ufn=uf.getUf()
    if tipoficha>4:
        financiera=True
        tipoficha=tipoficha-4
    if tipoficha==2:
        pro=True
    elif tipoficha==3:
        interna=True
    elif tipoficha==4:
        interna=True
        pro=True


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
    print(propiedad)

    if len(propiedad)<1:

        if sitio=='portal':
            link="https://www.portalinmobiliario.com/"+str(id)
        else:
            link="https://www.yapo.cl/region_metropolitana/"+str(id)

        if not pubPortalExiste.publicacionExiste(link) and not pubYapoExiste.publicacionExiste(link):
            text='¨Propiedad no se encuentra en la base de datos.'
            return(text)
        elif sitio=="portal":
            pass
        else:
            if obtainPropFromYapo(link) is not False:
                propiedad=obtainPropFromYapo(link)


    else:
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

        propiedad=list(propiedad)

        region=str(propiedad[1])
        regionP=region
        regionY=regYapoDict[region.lower()]
        if region=='15':
            regionP='metropolitana'
        if region=='metropolitana':
            regionY='15'
        operacion=str(propiedad[2])
        tipo=str(propiedad[3])
        precio=float(propiedad[4])
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
                comuna=comuna.replace('-'+str(regionP),'')
                comuna=comuna.replace('-',' ')
                comuna=comuna.capitalize()
                propiedad.append(comuna)

            else:
                comuna=str(link.split('/')[6])
                comuna=comuna.replace('-metropolitana','')
                comuna=comuna.replace('-',' ')
                comuna=comuna.capitalize()
                propiedad.append(comuna)
        else:
            comuna=str(propiedad[14])
    #Revisar si existe aun la publicacion
    if not pubPortalExiste.publicacionExiste(link):
        text='Propiedad ya no se encuentra disponible en el sitio.'
        return(text)
    #sacar informacion de la publicacion
    #sacar urls fotos portal
    matrixdescripcion=[]
    matrixcounter=0
    matrixdescripcion.append('')

    if sitio=='portal':
        first=True
        url=[]
        page = requests.get(link, headers={'User-Agent': agentCreator.generateAgent()})
        metatext=page.text
        metatext=metatext.split(' ')
        descripcion=[]
        savedescripcion=False
        for texto in metatext:

            if 'item-description__text' in texto:
                savedescripcion=True
            if '/div' in texto:
                if savedescripcion:
                    descripcion.append(str(texto))
                savedescripcion = False
            if savedescripcion:
                descripcion.append(str(texto))

        descripcion2=descripcion.copy()

        first=(descripcion2[0])
        first=first.split(">")
        print(first)
        first=first[2]
        descripcion[0]=first

        last=descripcion2[-1]
        last=last.split("<")
        last=last[0]
        descripcion[-1]=last

        #descripcion=descripcion[2:]
        print(descripcion)
        descripcion=list(descripcion)

        if not interna:
            for desc in descripcion:
                desc=desc.replace('   ','')
                desc=desc.replace('<br />',' ')
                desc=desc.replace('<br/>',' ')
                desc=desc.replace('<br>',' ')
                desc=desc.replace('<b/>','')
                desc=desc.replace('<b>','')
                desc=desc.replace('</b>','')
                desc=desc.replace('<br','')
                desc=desc.replace('/>','')
                desc=desc.replace('&#237;','í')
                desc=desc.replace('&#233;','é')
                desc=desc.replace('&#243;','ó')
                desc=desc.replace('&#225;','á')
                desc=desc.replace('&#250;','ú')
                desc=desc.replace('&#241;','ñ')
                desc=desc.replace('&#209;','Ñ')

                if "+56" in desc:
                    desc="**"
                if len(desc)>=6:
                    try:
                        desc.replace('\n',"")
                        int(desc)
                        desc="**"
                    except:
                        pass

                if "@" in desc:
                    desc="***"

                if ((len(matrixdescripcion[matrixcounter])+len(desc))>=78):

                    matrixcounter+=1
                    matrixdescripcion.append('')
                    if desc!= '':
                        matrixdescripcion[matrixcounter]=matrixdescripcion[matrixcounter]+str(desc)
                else:
                    if first:
                        if desc!= '':
                            matrixdescripcion[matrixcounter]=matrixdescripcion[matrixcounter]+str(desc)
                        first=False
                    else:
                        if desc!= '':
                            matrixdescripcion[matrixcounter]=matrixdescripcion[matrixcounter]+' '+str(desc)
            print(matrixdescripcion)
            for x,matrix in enumerate(matrixdescripcion):
                matrix=matrix.replace('<br />','\n')
                matrix=matrix.replace('<br/>','\n')
                matrix=matrix.replace('<br>','\n')
                matrix=matrix.replace('<b/>','')
                matrix=matrix.replace('<b>','')
                matrix=matrix.replace('</b>','')
                matrixdescripcion[x]=matrix
            descripcion='\n'.join(matrixdescripcion)
            propiedad.append(descripcion)

        else:
            descripcion=' '.join(descripcion)
            descripcion=descripcion.replace('   ','')
            descripcion=descripcion.replace('<br />','\n')
            descripcion=descripcion.replace('<br/>','\n')
            descripcion=descripcion.replace('<br>','\n')
            descripcion=descripcion.replace('<b/>','')
            descripcion=descripcion.replace('<b>','')
            descripcion=descripcion.replace('</b>','')
            descripcion=descripcion.replace('<br','')
            descripcion=descripcion.replace('/>','')
            descripcion=descripcion.replace('&#237;','í')
            descripcion=descripcion.replace('&#233;','é')
            descripcion=descripcion.replace('&#243;','ó')
            descripcion=descripcion.replace('&#225;','á')
            descripcion=descripcion.replace('&#250;','ú')
            descripcion=descripcion.replace('&#241;','ñ')
            descripcion=descripcion.replace('&#209;','Ñ')



            propiedad.append(descripcion)
            print(propiedad)

        for meta in metatext:

            if 'data-full-images' in meta:
                meta=meta.split(';')
                for met in meta:
                    if 'mlstatic' in met:
                        met=met.split('&')
                        met=met[0]
                        met=met.replace(".webp",".jpg")
                        url.append(str(met))




    #Sacar urls fotos yapo
    else:

        url=[]
        page = requests.get(link, headers={'User-Agent': agentCreator.generateAgent()})
        metatext=page.text
        metatext=metatext.split(' ')
        descripcion=[]
        savedescripcion=False
        saveimg=False
        og=True

        for texto in metatext:

            if '<h4>Descripción</h4>' in texto:
                savedescripcion=True

            if og and 'og:image' in texto:
                saveimg=True
                og=False
            if 'img/yapo' in texto:
                saveimg=False
            if savedescripcion:
                descripcion.append(str(texto))
            if '</div>' in texto:
                savedescripcion = False
            if saveimg and 'img.yapo.cl/images' in texto:
                texto=texto.replace('content="','')
                texto.replace('"','')
                url.append(texto)
            if 'phone-url' in texto:
                texto=texto.split('"')
                texto=texto[1]
                auxPhone=texto
                auxPhone='https://www.yapo.cl'+auxPhone
        descripcion=descripcion[1:]
        first=True
        print(descripcion)
        for desc in descripcion:
            desc=desc.replace('\n',' ')
            desc=desc.replace('<br />','\n')
            desc=desc.replace('</div>','\n')
            desc=desc.replace('<br>','\n')
            desc=desc.replace('<br','')
            desc=desc.replace('/>','')
            desc=desc.replace('itemprop="description">',"")
            desc=desc.replace('</p>','\n')
            desc=desc.replace("\t","")
            desc=desc.replace('<!','')
            desc=desc.replace('--','')
            desc=desc.replace('  ','')
            desc=desc.replace('\n',' ')


            if ((len(matrixdescripcion[matrixcounter])+len(desc))>=78):

                matrixcounter+=1
                matrixdescripcion.append('')
                matrixdescripcion[matrixcounter]=matrixdescripcion[matrixcounter]+str(desc)
            else:
                if first:
                    matrixdescripcion[matrixcounter]=matrixdescripcion[matrixcounter]+str(desc)
                    first=False
                else:
                    matrixdescripcion[matrixcounter]=matrixdescripcion[matrixcounter]+' '+str(desc)

        print(matrixdescripcion)
        descripcion='\n'.join(matrixdescripcion)

        propiedad.append(descripcion)


        try:
            print(auxPhone)
            response = requests.get(auxPhone, headers={'User-Agent': agentCreator.generateAgent()})
            auxphone2=auxPhone
            img = Image.open(BytesIO(response.content))
            img=img.convert('L')
            img=img.convert('1')
            img.save("auxphone.gif")
            auxPhone=1
        except:
            pass
    lenfotos=len(url)

    if len(url)==0:
        print("la propiedad no cuenta con fotografias")
    else:
        print('total fotos: '+str(len(url)))
        for x,u in enumerate (url):
            u=u.replace('"','')
            response = requests.get(u)
            img = Image.open(BytesIO(response.content))
            img.save(str(x)+" foto.jpg")

    if not interna:
        imagenDescripcion = Image.new('RGB', (456, 345), color = (255, 255, 255))

        d = ImageDraw.Draw(imagenDescripcion)
        f= ImageFont.truetype('arial.ttf',12)
        d.text((0,0), descripcion,font=f, fill=(0,0,0))

        imagenDescripcion.save('imagenDescripcion.png')

    datospro = []
    if pro:

        propsPV = reportes.from_portalinmobiliario(tipo, regionP, [comuna], "venta", True)
        propsYV = reportes.from_yapo(tipo, regionY, [comuna], True, "venta", True)
        propsV = propsPV + propsYV
        # aca deberiamos hacer el GB

        m2=reportes.m2prom(tipo,comuna,region)
        m2V=m2[0]
        m2A=m2[1]

        clfHV = ensemble.GradientBoostingRegressor(n_estimators=400, max_depth=5, min_samples_split=2,
                                                  learning_rate=0.1, loss='huber')

        #id2,fechapublicacion,fechascrap,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,lat,lon,estacionamientos,link

        preciosV = [row[5] for row in propsV]

        trainingV = propsV.copy()
        for row in trainingV:
            del row[13]
            if tipo not in ["departamento","Casa","Oficina"]:
                del row[12]
                del row[7]
                if tipo != "local":
                    del row[6]
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

        propsPA = reportes.from_portalinmobiliario(tipo, regionP, [comuna], "arriendo", True)
        propsYA = reportes.from_yapo(tipo, region, [comuna], True, "arriendo", True)
        propsA = propsPA + propsYA
        # aca deberiamos hacer el GB

        clfHA = ensemble.GradientBoostingRegressor(n_estimators=400, max_depth=5, min_samples_split=2,
                                                  learning_rate=0.1, loss='huber')

        #id2,fechapublicacion,fechascrap,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,lat,lon,estacionamientos,link

        preciosA = [row[5] for row in propsA]

        trainingA = propsA.copy()
        for row in trainingA:
            del row[13]
            if tipo not in ["departamento","Casa","Oficina"]:
                del row[12]
                del row[7]
                if tipo != "local":
                    del row[6]
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

        textmail+="Resultados comuna "+str(comuna)+":\n"+"Score Ventas: "+str((int(10000*scoreV))/100)+"%\nScore Arriendos: "+str((int(10000*scoreA))/100)+"%\nPrecio m2 Venta: UF."+str((int(10*(m2V/ufn)))/10)+"\nPrecio m2 Arriendo: $"+str((int(m2A)))+"\n\n"

        if tipo not in ["departamento", "Casa", "Oficina"]:
            prop=[banos, metrosmin, metrosmax, lat, lon]
            if tipo != "local":
                prop = [metrosmin, metrosmax, lat, lon]
        else:
            prop = [dormitorios, banos, metrosmin, metrosmax, lat, lon, estacionamientos]

        tasacionVenta = clfHV.predict([prop])
        tasacionArriendo = clfHA.predict([prop])

        precioV = tasacionVenta
        precioA = tasacionArriendo
        print("el precio tasado de venta inicial es: "+str(precioV))
        print("el precio tasado de arriendo inicial es: "+str(precioA))

        if operacion=='venta':

            if precioV is None or precioV < 0.1:
                pro=False


            try:
                rentaV = ((precioV - precio) / precio)
            except:
                pro=False
                text2='No se ha podido realizar tasación'
                print('fail 1')

            if precioA is None or precioA < 0.01:
                pro=False


            try:
                rentaA = (precioA * 12 / precio)

            except:
                pro=False
                text2='No se ha podido realizar tasación'
                print('fail 2')


            if pro:
                if rentaA > 0.2:
                    pro=False
                    print('fail 3')

                if rentaA < 0:
                    pro=False


            if pro:
                # precio venta tasado
                datospro.append(precioV)
                # rentabilidad de venta
                datospro.append(float(rentaV))

                # precio arriendo tasado
                datospro.append(precioA)
                # rentabilidad de arriendo
                datospro.append(float(rentaA))



        else:

            try:
                precioA = tasacionArriendo

            except:
                pro=False
                text2='No se ha podido realizar tasación'
                print('fail 72')

            if pro:
                if precioA is None or precioA < 0.01:
                    pro = False
                    text2='No se ha podido realizar tasación'
                    print('fail 8')


            if pro:
                # precio arriendo tasado
                datospro.append(precioA)
                # rentabilidad de arriendo

    datoscontacto = []
    if interna:

        if sitio=='portal':
            try:
                email, telefono, dueno = reportes.getDatosDueno(str(id))
            except:
                email = "NN"
                telefono = "NN"
                dueno = "NN"

        else:
            email = "NN"
            if auxPhone == 1:
                telefono=auxphone2
            else:
                telefono = "NN"
            dueno = 'NN'
        datoscontacto.append(email)
        datoscontacto.append(telefono)
        datoscontacto.append(dueno)


    #Crear PDF
    if interna:
        nombrearchivo="Ficha Propiedad Sitio:"+str(sitio)+" Id:"+str(id)+".pdf"
    else:
        nombrearchivo="Ficha Propiedad Sitio:"+str(sitio)+", "+str(operacion)+", "+str(tipo)+", "+str(region)+", "+str(comuna)+".pdf"

    print(nombrearchivo)
    links=[]
    if financiera:
        pro="financiera"
    pdfCreatorFichas.crearPdfFicha(nombrearchivo,id,propiedad,lenfotos,pro,datospro,interna,datoscontacto,regionP,links)
    print("pdf generado con exito")
    #Enviar PDF
    sendmail.sendMail(mail,"",nombrearchivo)

    #Eliminar del servidor

    if len(url)==0:
        pass
    else:
        for x,u in enumerate (url):
            os.remove(str(x)+" foto.jpg")
    try:
        os.remove("auxphone.gif")
    except:
        pass

    if not interna:
        try:
            os.remove("imagenDescripcion.png")
        except:
            pass
    os.remove(nombrearchivo)

    #Retornar exito
    text = "Ficha creada para la propiedad: "+str(id)+" obtenida del sitio: "+str(sitio)+", enviada con éxito al correo: "+str(mail)+"."
    if text2!='':
        text=text2+'. '+text
    return(text)


def main():
    texto=crearFicha('portal',5022561,'sergei.schkolnik@gmail.com',3)
    print(texto)

if __name__ == '__main__':
    main()
