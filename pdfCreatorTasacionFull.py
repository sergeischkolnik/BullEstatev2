import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from datetime import datetime, timedelta
from reportlab import platypus
from  reportlab.lib.styles import ParagraphStyle as PS
import locale
import uf
import os
from collections import namedtuple
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import base64
import pubPortalExiste
import reportes
import botPropertyConnector
import uf

def crearPdfTasacion(client,precioV,precioA,linksVenta,linksArriendo,fileName,ufventacomuna,arriendocomuna):
    #Propiedad:
    #DatosPro: Preciov/RentV/PrecioA/RentA, o bien solo PrecioA
    headerslocalizacion=[]
    headersprecio=[]
    headerspropiedad=[]
    headerscomuna=[]

    datoslocalizacion=[]
    datosprecio=[]
    datospropiedad=[]
    datoscomuna=[]


    uf1=uf.getUf()

    region=str(client["region"])
    comuna=str(client["comuna"])
    tipo=str(client["tipo"])
    direccion=str(client["adress"])


    headerslocalizacion.append("Tipo de Prop.")
    headerslocalizacion.append("Región")
    headerslocalizacion.append("Comuna")
    headerslocalizacion.append("Dirección")


    datoslocalizacion.append(tipo.capitalize())
    datoslocalizacion.append(region.capitalize())
    datoslocalizacion.append(comuna.capitalize())
    datoslocalizacion.append(direccion.capitalize())

    metrosmin = str(int(client["metros"]))
    metrosmax = str(int(client["total"]))


    ufm2 = '{:,}'.format((int(10 * ((2 * float(precioV) / (float(metrosmin) + float(metrosmax))) / float(uf1)))) / 10).replace(
        ",", ".")
    am2 = '{:,}'.format(int(2 * float(precioA) / (float(metrosmin) + float(metrosmax)))).replace(",", ".")


    precioVuf=(int(precioV/uf1))
    precioVuf=str(format(precioVuf,','))
    precioVuf=precioVuf.replace(',','.')

    precioV=int(precioV)
    precioV=str(format(precioV,','))
    precioV=precioV.replace(',','.')



    precioAuf = (int(precioA / uf1))
    precioAuf = str(format(precioAuf, ','))
    precioAuf = precioAuf.replace(',', '.')

    precioA=int(precioA)
    precioA = str(format(precioA, ','))
    precioA = precioA.replace(',', '.')


    dormitorios=str(int(client["dormitorios"]))
    banos=str(int(client["baños"]))




    estacionamientos=str(int(client["estacionamientos"]))
    bodegas=str(int(client["bodegas"]))


    headersprecio.append("Tasación Venta UF")
    headersprecio.append("Tasación Venta $")
    headersprecio.append("Venta UF/m2")
    headersprecio.append("Tasación Arriendo $")
    headersprecio.append("Arriendo/m2")

    headerspropiedad.append("Sup. Util")
    headerspropiedad.append("Sup. Total")
    headerspropiedad.append("Dormitorios")
    headerspropiedad.append("Baños")
    headerspropiedad.append("Estacionamientos")
    headerspropiedad.append("Bodegas")

    datosprecio.append(precioVuf)
    datosprecio.append(precioV)
    datosprecio.append(ufm2)
    datosprecio.append(precioA)
    datosprecio.append(am2)

    datospropiedad.append(metrosmin)
    datospropiedad.append(metrosmax)
    datospropiedad.append(dormitorios)
    datospropiedad.append(banos)
    datospropiedad.append(estacionamientos)
    datospropiedad.append(bodegas)

    headerscomuna.append("Comuna")
    headerscomuna.append("UF/m2 Venta")
    headerscomuna.append("$/m2 Arriendo")

    datoscomuna.append(comuna.capitalize())
    datoscomuna.append(ufventacomuna)
    datoscomuna.append(arriendocomuna)



    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY,leading=16))


    doc = SimpleDocTemplate(fileName,pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)

    Story=[]

    tabla=[]
    tabla.append(headerslocalizacion)
    tabla.append(datoslocalizacion)

    t1=Table(tabla,hAlign='LEFT')
    t1.setStyle(TableStyle([
                           ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                           ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                           ('FONTSIZE', (0,0), (-1,-1), 9),
                           ('BACKGROUND',(0,0), (-1,0),colors.HexColor('#34BAAF')),
                           ('TEXTCOLOR',(0,0), (-1,0),colors.black),
                           ]))
    tabla=[]
    tabla.append(headersprecio)
    tabla.append(datosprecio)

    t2=Table(tabla,hAlign='LEFT')
    t2.setStyle(TableStyle([
                           ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                           ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                           ('FONTSIZE', (0,0), (-1,-1), 11),
                           ('BACKGROUND',(0,0), (-1,0),colors.lightgrey),
                           ('TEXTCOLOR',(0,0), (-1,0),colors.black),
                           ]))

    tabla = []
    tabla.append(headerspropiedad)
    tabla.append(datospropiedad)

    t3 = Table(tabla, hAlign='LEFT')
    t3.setStyle(TableStyle([
                            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                            ('FONTSIZE', (0, 0), (-1, -1), 11),
                            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                             ]))

    tabla = []
    tabla.append(headerscomuna)
    tabla.append(datoscomuna)

    t4 = Table(tabla, hAlign='LEFT')
    t4.setStyle(TableStyle([
                            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                            ('FONTSIZE', (0, 0), (-1, -1), 11),
                            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
    ]))

    image = Image('bull_logo2.png', hAlign='LEFT')
    image._restrictSize(2 * inch, 3 * inch)
    Story.append(image)
    Story.append(Spacer(1, 16))




    ptext = '<font size=11><b>TASACIÓN PROPIEDAD</b></font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 14))

    Story.append(t1)
    Story.append(Spacer(1, 16))
    Story.append(t2)
    Story.append(Spacer(1, 16))
    Story.append(t3)
    Story.append(Spacer(1, 16))
    Story.append(t4)
    Story.append(Spacer(1, 16))


    if len(linksVenta)>0:
        print("entro en crear tabla de links")
        print(linksVenta)
        data=[]
        n=0
        headers=["N°","UF","Precio","UF/mt2","MtsMin","MtsMax","Dorms","Baños","Link","Disponibilidad"]
        for l in linksVenta:
            if "portal" in l:
                d=[]
                n+=1
                d.append(str(n))
                avaible=pubPortalExiste.publicacionExiste(l)
                id=botPropertyConnector.obtenerIdConLink(l,"www.portalinmobiliario.com")
                id=id[0]
                prop=reportes.precio_from_portalinmobiliario(id)
                prop=prop[0]
                print("Arreglo de propiedad:")
                print(prop)
                print("1er dato de propiedad de propiedad:")
                print(prop[0])
                ufn=int(prop[0]/(uf.getUf()))
                d.append(ufn)
                d.append(prop[0])
                d.append((int(20*ufn/(prop[1]+prop[2])))/10)
                d.append(int(prop[1]))
                d.append(int(prop[2]))
                d.append(prop[5])
                d.append(prop[6])
                print(d)
                print("appendeo bien datos")
                linkHtml = '<link href="' + l + '" color="blue">' + "Link" + '</link>'
                print(linkHtml)
                linkHtml=platypus.Paragraph(linkHtml, PS('body'))
                d.append(linkHtml)
                if avaible:
                    d.append("Disponible")
                else:
                    d.append("No disponible")
                print(str(n)+" intento de agregar prop a data")
                print(d)
                data.append(d)
            else:
                pass


        data = [headers]+data
        #t=Table(data,nrCols*[0.6*inch], nrRows*[0.25*inch])
        t=Table(data)
        t.setStyle(TableStyle([
                               ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                               ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                               ('FONTSIZE', (0,0), (-1,-1), 9),
                               ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                               ]))

        Story.append(t)
        Story.append(PageBreak())

    if len(linksArriendo)>0:
        print("entro en crear tabla de links")
        print(linksArriendo)
        data=[]
        n=0
        headers=["N°","Precio","$/mt2","MtsMin","MtsMax","Dorms","Baños","Link","Disponibilidad"]
        for l in linksArriendo:
            if "portal" in l:
                d=[]
                n+=1
                d.append(str(n))
                avaible=pubPortalExiste.publicacionExiste(l)
                id=botPropertyConnector.obtenerIdConLink(l,"www.portalinmobiliario.com")
                id=id[0]
                prop=reportes.precio_from_portalinmobiliario(id)
                prop=prop[0]
                print("Arreglo de propiedad:")
                print(prop)
                print("1er dato de propiedad de propiedad:")
                print(prop[0])
                d.append(prop[0])
                d.append((int(20*prop[0]/(prop[1]+prop[2])))/10)
                d.append(int(prop[1]))
                d.append(int(prop[2]))
                d.append(prop[5])
                d.append(prop[6])
                print(d)
                print("appendeo bien datos")
                linkHtml = '<link href="' + l + '" color="blue">' + "Link" + '</link>'
                print(linkHtml)
                linkHtml=platypus.Paragraph(linkHtml, PS('body'))
                d.append(linkHtml)
                if avaible:
                    d.append("Disponible")
                else:
                    d.append("No disponible")
                print(str(n)+" intento de agregar prop a data")
                print(d)
                data.append(d)
            else:
                pass


        data = [headers]+data
        #t=Table(data,nrCols*[0.6*inch], nrRows*[0.25*inch])
        t=Table(data)
        t.setStyle(TableStyle([
                               ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                               ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                               ('FONTSIZE', (0,0), (-1,-1), 9),
                               ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                               ]))

        Story.append(t)
        Story.append(PageBreak())


    Story=list(Story)
    doc.build(Story)
    return fileName
