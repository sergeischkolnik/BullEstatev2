import time
from reportlab.lib.enums import TA_JUSTIFY
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


def crearPdfFicha(fileName,id,propiedad,lenfotos,pro,datospro,interna,datosinterna):

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
    headerslocalizacion.append("Tipo de Propiedad")
    headerslocalizacion.append("Región")
    headerslocalizacion.append("Comuna")

    datoslocalizacion.append(operacion)
    datoslocalizacion.append(tipo)
    datoslocalizacion.append(region)
    datoslocalizacion.append(comuna)

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
            precioV=str(format(precioV,','))
            precioV=precioV.replace(',','.')
            precioV='UF '+precioV
            rentV = float(datospro[1])
            rentV = int(rentV*1000)
            rentV = float(rentV/10)
            rentV = str(rentV)+"%"
            confV=datospro[2]
            precioA=datospro[3]
            precioA=str(format(precioA,','))
            precioA=precioA.replace(',','.')
            precioA='$ '+precioA
            rentA = float(datospro[4])
            rentA = int(rentA*1000)
            rentA = float(rentA/10)
            rentA = str(rentA)+"%"
            confA=datospro[5]

            headersrentabilidad.append("Precio Tasado")
            headersrentabilidad.append("Rentabilidad Venta")
            headersrentabilidad.append("Confianza Venta")
            headersrentabilidad.append("Tasacion Arriendo")
            headersrentabilidad.append("Rentabilidad Arriendo")

            datosrentabilidad.append(precioV)
            datosrentabilidad.append(rentV)
            datosrentabilidad.append(confV)
            datosrentabilidad.append(precioA)
            datosrentabilidad.append(rentA)

        else:
            precioA =datospro[0]
            precioA=str(format(precioA,','))
            precioA=precioA.replace(',','.')
            precioA='$ '+precioA
            confA =datospro[1]
            headersrentabilidad.append("Precio Arriendo")
            datosrentabilidad.append(precioA)


        headersrentabilidad.append("Confianza Arriendo")
        datosrentabilidad.append(confA)

    if interna:
        mail=datosinterna[0]
        headerscontacto.append("Mail")
        datoscontacto.append(mail)

        telefono=datosinterna[1]
        headerscontacto.append("Telefono")
        datoscontacto.append(telefono)

        dueno=datosinterna[2]
        headerscontacto.append("Dueño")
        datoscontacto.append(dueno)




    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))


    doc = SimpleDocTemplate(fileName,pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)

    Story=[]

    t1=Table(headerslocalizacion+datoslocalizacion)
    t1.setStyle(TableStyle([
                           ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                           ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                           ('FONTSIZE', (0,0), (-1,-1), 9),
                           ]))

    t2=Table(headerspropiedad+datospropiedad)
    t2.setStyle(TableStyle([
                           ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                           ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                           ('FONTSIZE', (0,0), (-1,-1), 9),
                           ]))

    t3=Table(headersrentabilidad+datospropiedad)
    t3.setStyle(TableStyle([
                           ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                           ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                           ('FONTSIZE', (0,0), (-1,-1), 9),
                           ]))

    t4=Table(headerscontacto+datoscontacto)
    t4.setStyle(TableStyle([
                           ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                           ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                           ('FONTSIZE', (0,0), (-1,-1), 9),
                           ]))

    image = Image('bull_logo2.png', hAlign='LEFT')
    image._restrictSize(2 * inch, 3 * inch)
    Story.append(image)
    Story.append(Spacer(1, 14))

    if interna:
        ptext = '<font size=14>FICHA PROPIEDAD: '+str(id)+'</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 16))

        ptext = '<font size=12>Nombre: '+str(nombre)+'.</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
    else:
        ptext = '<font size=14>FICHA PROPIEDAD</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 16))

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

    ptext = '<font size=14>DESCRIPCIÓN:</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size=12>' + str(descripcion) + '</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(PageBreak())

    for x in range(0,lenfotos):

        image = Image(str(x)+" foto.jpg", hAlign='LEFT')
        image._restrictSize(6 * inch, 9 * inch)
        Story.append(image)
        Story.append(Spacer(1, 4))

    Story=list(Story)
    doc.build(Story)
