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







def crearPdfFicha(fileName,id,propiedad,lenfotos,pro,datospro,interna,datosinterna,regionP,links):
    #Propiedad:
    #DatosPro: Preciov/RentV/PrecioA/RentA, o bien solo PrecioA
    headerslocalizacion=[]
    headerspropiedad=[]
    headersrentabilidad=[]
    headerscontacto=[]
    datoslocalizacion=[]
    datospropiedad=[]
    datosrentabilidad=[]
    datoscontacto=[]

    uf1=uf.getUf()
    for x,p in enumerate (propiedad):
        if p is None:
            propiedad[x]=0
    nombre=str(propiedad[0])
    region=str(propiedad[1])
    comuna=str(propiedad[14])
    operacion=str(propiedad[2])
    tipo=str(propiedad[3])

    headerslocalizacion.append("Operación")
    headerslocalizacion.append("Tipo de Prop.")
    headerslocalizacion.append("Región")
    headerslocalizacion.append("Comuna")

    datoslocalizacion.append(operacion.capitalize())
    datoslocalizacion.append(tipo.capitalize())
    datoslocalizacion.append(regionP.capitalize())
    datoslocalizacion.append(comuna.capitalize())

    precio=int(propiedad[4])

    preciouf=(int(precio/uf1))
    preciouf=str(format(preciouf,','))
    preciouf=preciouf.replace(',','.')

    precio=str(format(precio,','))
    precio=precio.replace(',','.')


    dormitorios=str(int(propiedad[5]))
    banos=str(int(propiedad[6]))

    metrosmin=str(int(propiedad[7]))
    metrosmax=str(int(propiedad[8]))

    estacionamientos=str(int(propiedad[9]))
    bodegas=str(int(propiedad[10]))

    lat=str(propiedad[11])
    lon=str(propiedad[12])
    link=str(propiedad[13])

    headerspropiedad.append("Precio $")
    if operacion=='venta':
        headerspropiedad.append("Precio UF")
    headerspropiedad.append("Sup. Util")
    headerspropiedad.append("Sup. Total")
    headerspropiedad.append("Dormitorios")
    headerspropiedad.append("Baños")
    headerspropiedad.append("Estacionamientos")
    headerspropiedad.append("Bodegas")

    datospropiedad.append(precio)
    if operacion=='venta':
        datospropiedad.append(preciouf)
    datospropiedad.append(metrosmin)
    datospropiedad.append(metrosmax)
    datospropiedad.append(dormitorios)
    datospropiedad.append(banos)
    datospropiedad.append(estacionamientos)
    datospropiedad.append(bodegas)

    descripcion=propiedad[15]

    if pro:
        if operacion=='venta':
            precioV=datospro[0]
            precioV=precioV/uf1
            precioV=int(precioV)
            precioV=str(format(precioV,','))
            precioV=precioV.replace(',','.')
            precioV='UF '+precioV
            rentV = float(datospro[1])
            rentV = int(rentV*1000)
            rentV = float(rentV/10)
            rentV = str(rentV)+"%"
            precioA=datospro[2]
            precioA=str(format(precioA,','))
            precioA=precioA.replace(',','.')
            precioA='$ '+precioA
            rentA = float(datospro[3])
            rentA = int(rentA*1000)
            rentA = float(rentA/10)
            rentA = str(rentA)+"%"

            headersrentabilidad.append("Tasación Venta")
            headersrentabilidad.append("Rent. Venta")

            headersrentabilidad.append("Tasación Arriendo")
            headersrentabilidad.append("Rent. Arriendo")

            datosrentabilidad.append(precioV)
            datosrentabilidad.append(rentV)

            datosrentabilidad.append(precioA)
            datosrentabilidad.append(rentA)

        else:
            precioA =datospro[0]
            precioA=str(format(precioA,','))
            precioA=precioA.replace(',','.')
            precioA='$ '+precioA
            headersrentabilidad.append("Tasación Arriendo")
            datosrentabilidad.append(precioA)


    if interna:
        mail=datosinterna[0]
        headerscontacto.append("Mail")
        datoscontacto.append(mail)

        telefono=datosinterna[1]
        headerscontacto.append("Telefono")
        if 'yapo' in link and telefono!='NN':
            try:
                image = Image("auxphone.gif")
                image._restrictSize(1.2 * inch, 1.7 * inch)
                datoscontacto.append(image)
            except:
                datoscontacto.append('NN')
        else:
            datoscontacto.append(telefono)

        dueno=datosinterna[2]
        headerscontacto.append("Dueño")
        datoscontacto.append(dueno.capitalize())




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
    tabla.append(headerspropiedad)
    tabla.append(datospropiedad)

    t2=Table(tabla,hAlign='LEFT')
    t2.setStyle(TableStyle([
                           ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                           ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                           ('FONTSIZE', (0,0), (-1,-1), 11),
                           ('BACKGROUND',(0,0), (-1,0),colors.lightgrey),
                           ('TEXTCOLOR',(0,0), (-1,0),colors.black),
                           ]))
    if pro:
        tabla=[]
        tabla.append(headersrentabilidad)
        tabla.append(datosrentabilidad)

        t3=Table(tabla,hAlign='LEFT')
        t3.setStyle(TableStyle([
                               ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                               ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                               ('BACKGROUND',(0,0), (-1,0),colors.lightgrey),
                               ('TEXTCOLOR',(0,0), (-1,0),colors.black),
                               ('FONTSIZE', (0,0), (-1,-1), 11),
                               ]))
    if interna:
        tabla=[]
        tabla.append(headerscontacto)
        tabla.append(datoscontacto)

        t4=Table(tabla,hAlign='LEFT')
        t4.setStyle(TableStyle([
                               ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                               ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                               ('BACKGROUND',(0,0), (-1,0),colors.lightgrey),
                               ('TEXTCOLOR',(0,0), (-1,0),colors.black),
                               ('FONTSIZE', (0,0), (-1,-1), 11),
                               ]))

    image = Image('bull_logo2.png', hAlign='LEFT')
    image._restrictSize(2 * inch, 3 * inch)
    Story.append(image)
    Story.append(Spacer(1, 16))

    if interna:
        ptext = '<font size=11><b>FICHA PROPIEDAD</b>: '+str(id)+'</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 14))


    else:
        ptext = '<font size=11><b>FICHA PROPIEDAD</b></font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 14))

    Story.append(t1)
    Story.append(Spacer(1, 16))
    Story.append(t2)
    Story.append(Spacer(1, 16))
    if pro:
        Story.append(t3)
        Story.append(Spacer(1, 16))
    if interna:
        Story.append(t4)
        Story.append(Spacer(1, 16))

    ptext = '<font size=11><b>Descripción:</b></font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    if not interna:
        imagenDescripcion=Image('imagenDescripcion.png')
        Story.append(imagenDescripcion)
        Story.append(PageBreak())
    else:
        ptext = '<font size=11>' + str(descripcion) + '</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(PageBreak())

    if len(links)>0 and interna:
        print("entro en crear tabla de links")
        print(links)
        data=[]
        n=0
        headers=["N°","Precio","MtsMin","MtsMax","Dorms","Baños","Link","Disponibilidad"]
        for l in links:
            d=[]
            n+=1
            d.append(str(n))
            avaible=pubPortalExiste.publicacionExiste(l)
            id=botPropertyConnector.obtenerIdConLink(link,"www.portalinmobiliario.com")
            id=id[0]
            prop=reportes.precio_from_portalinmobiliario(id)
            prop=prop[0]
            d.append(prop[1])
            d.append(prop[2])
            d.append(prop[3])
            d.append(prop[6])
            d.append(prop[7])
            print(d)
            print("appendeo bien datos")
            linkHtml = '<link href="' + l + '" color="blue">' + "Link"+'</link>'
            print(linkHtml)
            d.append(linkHtml)
            if avaible:
                d.append("Disponible")
            else:
                d.append("No disponible")
            print(str(n)+" intento de agregar prop a data")
            print(d)
            data.append(d)


        data = [headers]+data
        #t=Table(data,nrCols*[0.6*inch], nrRows*[0.25*inch])
        t=Table(data)
        t.setStyle(TableStyle([
                               ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                               ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                               ('FONTSIZE', (0,0), (-1,-1), 9),
                               ]))

        Story.append(t)
        Story.append(PageBreak())


    for x in range(0,lenfotos):

        image = Image(str(x)+" foto.jpg", hAlign='LEFT')
        image._restrictSize(6 * inch, 9 * inch)
        Story.append(image)
        Story.append(Spacer(1, 4))

    Story=list(Story)
    doc.build(Story)
