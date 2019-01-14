import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from datetime import datetime, timedelta
from reportlab import platypus
from  reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import PageBreak
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
        rent = float(prop[12])
        rent = int(rent*1000)
        rent = float(rent/10)
        rent = str(rent)+"%"
        prop[12] = rent

        #arreglar precio
        precio = prop[3]
        if operacion=="venta":
            precio=int(precio)
            precioStr =  format(precio, ',.2f')
            precioStr = precioStr[:-3]
            precioStr = "UF "+precioStr.replace(",",".")
        else:
            precioStr = format(precio, ',.2f')
            precioStr = precioStr[:-3]
            precioStr="$ "+str(precioStr)

        prop[3] = precioStr

        #quitar decimales a valores
        prop[4] = int(prop[4])
        prop[5] = int(prop[5])
        prop[6] = int(prop[6])
        prop[7] = int(prop[7])
        prop[8] = int(prop[8])
        prop[11] = int(prop[11])

        #link
        link = str(prop[13])
        linkHtml = '<link href="' + link + '" color="blue">' + "Link" + '</link>'
        prop[13] = platypus.Paragraph(linkHtml, PS('body'))

        #agregar numerador
        data[i] = [i+1] + prop

    headers = ["Nº"] + headers

    #t=Table(data,nrCols*[0.6*inch], nrRows*[0.25*inch])
    a=0
    data2=[]
    for i in data:
        if (i[1]==a):
            data2.append(i)
        else:
            if (a!=0):

                t=Table(data2)
                t.setStyle(TableStyle([
                                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                                       ('FONTSIZE', (0,0), (-1,-1), 9),
                                       ]))

                Story.append(t)
                Story.append(PageBreak())
            data2=[]
            data2 = [headers]+data2
            data2.append(i)
            a=i[1]


    Story.append(Spacer(2, 24))

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
