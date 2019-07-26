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
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import pdfCreatorFichas
import reportes
import tasadorbot2 as tb2
import io


def obtenerProp(id,sitio):

    if (sitio=='portal'):
        mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
        cur = mariadb_connection.cursor()
        sql = "SELECT nombre,region,operacion,tipo,precio,dormitorios,banos,metrosmin,metrosmax,estacionamientos,bodegas,lat,lon,link from portalinmobiliario WHERE id2="+str(id)
    else:
        mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='yapo')
        cur = mariadb_connection.cursor()
        sql = "SELECT titulo,idregion,operacion,tipo,preciopesos,dormitorios,banos,metrosmin,metrosmax,estacionamientos,estacionamientos,lat,lon,link,comuna from propiedades WHERE id2="+str(id)
    cur.execute(sql)
    propiedad = cur.fetchall()
    if len(propiedad)>0:
        return propiedad[0]
    else:
        return propiedad

def crearFicha(sitio,id,mail,tipoficha):
    text2=''
    auxPhone=0
    #Determinar tipo de informe
    pro=False
    interna=False
    full=False

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

    if len(propiedad)<1:
        text='¨Propiedad no se encuentra en la base de datos.'
        return(text)

    else:
        propiedad=list(propiedad)

        nombre=str(propiedad[0])
        region=str(propiedad[1])
        regionP=region
        regionY=region
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
                comuna=comuna.replace('-metropolitana','')
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

            if 'propiedad-descr' in texto:
                savedescripcion=True
            if '/div' in texto:
                savedescripcion = False
            if savedescripcion:
                descripcion.append(str(texto))

        descripcion=descripcion[2:]
        print(descripcion)

        if not interna:
            for desc in descripcion:
                desc=desc.replace('   ','')
                desc=desc.replace('<br />','\n')
                desc=desc.replace('<br/>','\n')
                desc=desc.replace('<br>','\n')
                desc=desc.replace('<b/>','')
                desc=desc.replace('<b>','')
                desc=desc.replace('&#237;','í')
                desc=desc.replace('&#233;','é')
                desc=desc.replace('&#243;','ó')
                desc=desc.replace('&#225;','á')
                desc=desc.replace('&#241;','ñ')
                desc=desc.replace('&#209;','Ñ')
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
            descripcion=descripcion.replace('&#237;','í')
            descripcion=descripcion.replace('&#233;','é')
            descripcion=descripcion.replace('&#243;','ó')
            descripcion=descripcion.replace('&#225;','á')
            descripcion=descripcion.replace('&#241;','ñ')
            descripcion=descripcion.replace('&#209;','Ñ')

            propiedad.append(descripcion)

        for meta in metatext:

            if 'https://image.portalinmobiliario.cl/Portal/Propiedades' in meta and '1200' in meta:
                meta=meta.split('"')

                url.append(str(meta[1]))




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

        propsP = reportes.from_portalinmobiliario(tipo, regionP, True)
        propsY = reportes.from_yapo(tipo, regionY, True, True)
        props = propsP + propsY

        if operacion=='venta':
            comunaP=(comuna.replace(' ','-')+'-metropolitana').lower()
            rentaPromedio = reportes.rentaPProm(tipo, float(dormitorios), float(banos), float(estacionamientos), comunaP)
            tasacionVenta = tb2.calcularTasacionData("venta", tipo, float(lat), float(lon), float(metrosmin),float(metrosmax),float(dormitorios),
                                                     float(banos), float(estacionamientos), props)
            tasacionArriendo = tb2.calcularTasacionData("arriendo", tipo, float(lat), float(lon), float(metrosmin),float(metrosmax),float(dormitorios),
                                                     float(banos), float(estacionamientos), props)


            precioV = tasacionVenta[0] * uf.getUf()
            precioA = tasacionArriendo[0]



            if precioV is None or precioV < 0.1:
                pro=False


            try:
                precioA = tasacionArriendo[0]
                rentaV = ((precioV - precio) / precio)
            except:
                pro=False
                text2='No se ha podido realizar tasación'
                print('fail 1')

            if precioA is None or precioA < 0.01:
                pro=False


            try:
                rentaA = (precioA * 12 / precio)
                print('succes 2.1')
                print(precioA)
                print(precioV)
                rentaPP = (precioA * 12 / precioV)
                print('succes 2.2')
            except:
                pro=False
                text2='No se ha podido realizar tasación'
                print('fail 2')


            if pro:
                if rentaA > 0.2:
                    pro=False
                    print('fail 3')


                if rentaPP < rentaPromedio:

                    try:
                        precioV = precioA * 12 / rentaPromedio
                        rentaV = ((precioV - precio) / precio)
                        rentaPP = (precioA * 12 / precioV)


                    except:
                        pro=False
                        text2='No se ha podido realizar tasación'
                        print('fail 4')

                if rentaPP > 0.15:
                    try:
                        precioV = precioA * 12 / 0.15
                        rentaV = ((precioV - precio) / precio)
                    except:
                        pro=False
                        text2='No se ha podido realizar tasación'
                        print('fail 52')

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
                tasacionArriendo = tb2.calcularTasacionData("arriendo", tipo, float(lat), float(lon), float(metrosmin),float(metrosmax),float(dormitorios),
                                                     float(banos), float(estacionamientos), props)
            except:
                pro=False
                text2='No se ha podido realizar tasación'
                print('fail 6')


            try:
                precioA = tasacionArriendo[0]
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

    pdfCreatorFichas.crearPdfFicha(nombrearchivo,id,propiedad,lenfotos,pro,datospro,interna,datoscontacto,regionP)
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
    texto=crearFicha('portal',4885411,'sergei.schkolnik@gmail.com',3)
    print(texto)

if __name__ == '__main__':
    main()
