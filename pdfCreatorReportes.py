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

def createPdfReport(cliente, fileName, data, headers,operacion):

    doc = SimpleDocTemplate(fileName,pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)

    Story=[]


    image = Image('bull_logo2.png', hAlign='LEFT')
    image._restrictSize(2 * inch, 3 * inch)
    Story.append(image)

    Story.append(Spacer(1, 12))

    fecha_hoy = datetime.today().strftime('%d-%m-%Y')

    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    ptext = '<font size=12>%s</font>' % fecha_hoy

    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    # Create return address
    full_name = "BullEstate"
    ptext = '<font size=12>%s</font>' % full_name
    Story.append(Paragraph(ptext, styles["Normal"]))

    web = '<link href="' + 'http://www.bullestate.cl' + '" color="blue">' + 'www.bullestate.cl' + '</link>'
    Story.append(platypus.Paragraph(web, PS('body')))

    mail = '<a href="mailto:contacto@bullestate.cl" color="blue">contacto@bullestate.cl</a>'
    Story.append(platypus.Paragraph(mail, PS('body')))

    Story.append(Spacer(1, 12))
    ptext = '<font size=12>Estimada/o %s:</font>' % cliente.split()[0].strip()
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size=12>Según los requerimientos presentados por Ud, las oportunidades inmobiliarias encontradas con ' \
            'fecha %s, son las siguientes:</font>' % fecha_hoy
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    nrCols = 11
    nrRows = len(data) + 1

    data = [list(elem) for elem in data]

    #creacion de precios, porcentajes y link
    for i,prop in enumerate(data):
        #porcentaje
        rent = float(prop[9])
        rent = int(rent*1000)
        rent = float(rent/10)
        rent = str(rent)+"%"
        prop[9] = rent
        if (operacion=="venta"):
            rent = float(prop[11])
            rent = int(rent*1000)
            rent = float(rent/10)
            rent = str(rent)+"%"
            prop[11] = rent

        #arreglar precio
        precio = prop[0]
        if operacion=="venta":
            unf=uf.getUf()
            precio=precio/unf
            precio=int(precio)
            precioStr =  format(precio, ',.2f')
            precioStr = precioStr[:-3]
            precioStr = "UF "+precioStr.replace(",",".")
        else:
            precioStr = format(precio, ',.2f')
            precioStr = precioStr[:-3]
            precioStr="$ "+str(precioStr)

        prop[0] = precioStr
        ufn=uf.getUf()
        #quitar decimales a valores
        prop[1] = int(prop[1])
        prop[2] = int(prop[2])
        prop[3] = int(prop[3])
        prop[4] = int(prop[4])
        prop[5] = int(prop[5])
        prop[7] = int(prop[7])

        if (operacion=="venta"):
            prop[8] = int(prop[8]/ufn)
            prop[8] = format(prop[8], ',.2f')
            prop[8] =prop[8][:-3]
            prop[8] ="UF "+str(prop[8])
            prop[10] = int(prop[10])
            prop[10] = format(prop[10], ',.2f')
            prop[10] =prop[10][:-3]
            prop[10] ="$ "+str(prop[10])
            #link
            link = str(prop[12])
            linkHtml = '<link href="' + link + '" color="blue">' + "Link" + '</link>'
            prop[12] = platypus.Paragraph(linkHtml, PS('body'))

        else:

            prop[8] = int(prop[8])
            prop[8] = format(prop[8], ',.2f')
            prop[8] =prop[8][:-3]
            prop[8] ="$ "+str(prop[8])
            #link
            link = str(prop[10])
            linkHtml = '<link href="' + link + '" color="blue">' + "Link" + '</link>'
            prop[10] = platypus.Paragraph(linkHtml, PS('body'))

        #agregar numerador
        data[i] = [i+1] + prop

    headers = ["Nº"] + headers
    data = [headers]+data
    #t=Table(data,nrCols*[0.6*inch], nrRows*[0.25*inch])
    t=Table(data)
    t.setStyle(TableStyle([
                           ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                           ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                           ('FONTSIZE', (0,0), (-1,-1), 9),
                           ]))

    Story.append(t)
    Story.append(Spacer(2, 24))

    ptext = '<font size=12>*D=Dormitorios  B=Baños  E=Estacionamientos  P.P=Precio venta predicho  Rent.P=Rentabilidad Venta  Rent.A=Rentabilidad Arriendo </font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size=12>Si ud. esta interesada/o en visitar algunas de las propiedades señaladas, le solicitamos escribirnos a la brevedad ' \
            'para agendar una visita.</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    ptext = '<font size=12>Sin otro particular, se despide atentamente:</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))

    image = Image('firmaSergei.jpg', hAlign='LEFT')
    image._restrictSize(2 * inch, 3 * inch)
    Story.append(image)

    ptext = '<font size=12>Sergei Schkolnik</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))


    doc.build(Story)
