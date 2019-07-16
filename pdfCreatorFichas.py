import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from datetime import datetime, timedelta
from reportlab import platypus
from  reportlab.lib.styles import ParagraphStyle as PS
import locale
import uf
import os


def crearPdfFicha(fileName,id,propiedad,lenfotos,comuna):

    print(propiedad)
    uf1=uf.getUf()
    for x,p in enumerate (propiedad):
        if p is None:
            propiedad[x]=0
    print(propiedad)
    nombre=str(propiedad[0])
    region=str(propiedad[1])
    operacion=str(propiedad[2])
    tipo=str(propiedad[3])

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



    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))


    doc = SimpleDocTemplate(fileName,pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)

    Story=[]

    image = Image('bull_logo2.png', hAlign='LEFT')
    image._restrictSize(2 * inch, 3 * inch)
    Story.append(image)
    Story.append(Spacer(1, 14))

    ptext = '<font size=14>FICHA PROPIEDAD:'+str(id)+'</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 16))

    ptext = '<font size=12>Nombre: '+str(nombre)+'.</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size=12>Operacion: '+str(operacion.capitalize())+'</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size=12>Tipo: '+str(tipo.capitalize())+'</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    if operacion=='venta':
        ptext = '<font size=12>Precio: UF '+str(preciouf)+'</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))

    ptext = '<font size=12>Precio: $ '+str(precio)+'</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size=12>Región: '+str(region.capitalize())+'</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size=12>Comuna: '+str(comuna)+'</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size=12>Dormitorios: '+str(dormitorios)+'</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size=12>Baños: '+str(banos)+'</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size=12>Superficies: '+str(metrosmin)+'mts2/'+str(metrosmax)+'mts2</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size=12>Estacionamientos: '+str(estacionamientos)+'</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size=12>Bodegas: '+str(bodegas)+'</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(3, 36))

    for x in range(0,lenfotos):

        image = Image(str(x)+" foto.jpg", hAlign='LEFT')
        image._restrictSize(6 * inch, 9 * inch)
        Story.append(image)

    Story=list(Story)
    doc.build(Story)
