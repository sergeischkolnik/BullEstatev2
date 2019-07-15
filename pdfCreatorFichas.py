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

def crearPdfFicha(id,propiedad,fotos):

    nombre=str(propiedad[0])
    region=str(propiedad[1])
    operacion=str(propiedad[2])
    tipo=str(propiedad[3])
    precio=str(propiedad[4])
    dormitorios=str(propiedad[5])
    banos=str(propiedad[6])
    metrosmin=str(propiedad[7])
    metrosmax=str(propiedad[8])
    estacionamientos=str(propiedad[9])
    bodegas=str(propiedad[10])
    lat=str(propiedad[11])
    lon=str(propiedad[12])
    link=str(propiedad[13])

    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    fileName="Ficha Propiedad id:"+str(id)+" ("+str(nombre[:30]+").")

    doc = SimpleDocTemplate(fileName,pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)

    Story=[]

    ptext = '<font size=12>FICHA PROPIEDAD</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size=12>Nombre: '+str(nombre)+'.</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size=12>Operacion: '+str(operacion)+'</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size=12>Tipo: '+str(tipo)+'</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size=12>Región: '+str(region)+'</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size=12>Dormitorios/Baños: '+str(dormitorios)+'/'+str(banos)+'</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size=12>Superficies: '+str(metrosmin)+'/'+str(metrosmax)+'</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size=12>Estacionamientos/Bodegas: '+str(estacionamientos)+'/'+str(bodegas)+'</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    for x,foto in enumerate(fotos):

        pathfoto = os.path.join(os.path.expanduser('~'), 'fotos',str(x)+" foto.jpg")
        Story.append(Image(pathfoto)._restrictSize(2 * inch, 3 * inch))


    Story=list(Story)
    doc.build(Story)
