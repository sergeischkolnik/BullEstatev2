
from datetime import datetime, timedelta, date
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


from sklearn import ensemble
from sklearn.model_selection import train_test_split


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
    full=False
    textmail=''
    ufn=uf.getUf()

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
        text='¨Propiedad no se encuentra en la base de datos.'
        return(text)

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
                savedescripcion = False
            if savedescripcion:
                descripcion.append(str(texto))

        #descripcion=descripcion[2:]
        print(descripcion)

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
