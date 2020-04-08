#EXTERNAL
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab import platypus
from  reportlab.lib.styles import ParagraphStyle as PS
import pymysql as mysql

#INTERNAL
import pubPortalExiste
import botPropertyConnector
import indicadoresV3 as indicadores

def precio_from_portalinmobiliario(id2):
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    sql = "SELECT precio,metrosmin,metrosmax,lat,lon,dormitorios,banos FROM portalinmobiliario WHERE id2='"+str(id2)+"'"
    cur.execute(sql)
    precio = cur.fetchall()

    return precio

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

    if pro=="financiera":
        pro=True
        financiera=True
    else:
        financiera=False

    uf=indicadores.getUf()
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
    precioreal=precio
    precioufreal=precio/uf
    preciouf=(int(precio/uf))
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
            precioVreal=precioV
            precioV=precioV/uf
            precioV=int(precioV)
            precioV=str(format(precioV,','))
            precioV=precioV.replace(',','.')
            precioV='UF '+precioV
            rentV = float(datospro[1])
            rentV = int(rentV*1000)
            rentV = float(rentV/10)
            rentV = str(rentV)+"%"
            precioA=datospro[2]
            precioAreal=10000*(int(precioA/10000))
            precioA=int(precioA)
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
            precioA=int(precioA[0])
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

    try:
        image = Image('bull_logo2.png', hAlign='LEFT')
        image._restrictSize(2 * inch, 3 * inch)
        Story.append(image)
        Story.append(Spacer(1, 16))
    except:
        try:
            image = Image('bull_logo.jpg', hAlign='LEFT')
            image._restrictSize(2 * inch, 3 * inch)
            Story.append(image)
            Story.append(Spacer(1, 16))
        except:
            pass



    if interna:
        ptext = '<font size=11>FICHA PROPIEDAD: '+str(id)+'</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 14))


    else:
        ptext = '<font size=11>FICHA PROPIEDAD</font>'
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

    ptext = '<font size=11>Descripción:</font>'
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
        headers=["N°","UF","Precio","UF/mt2","MtsMin","MtsMax","Dorms","Baños","Link","Disponibilidad"]
        for l in links:
            if "portal" in l:
                d=[]
                n+=1
                d.append(str(n))
                avaible=pubPortalExiste.publicacionExiste(l)
                id=botPropertyConnector.obtenerIdConLink(l,"www.portalinmobiliario.com")
                id=id[0]
                prop=precio_from_portalinmobiliario(id)
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
                               ('FONTSIZE', (0,0), (-1,-1), 11),
                               ]))

        Story.append(t)
        Story.append(PageBreak())
    print("Antes de entrar a datos financieros")
    if pro and financiera and operacion=='venta':

        print("entro datos financieros")
        tasacion=datospro[0]
        tasacionUF=(precioVreal/uf)

        ftext = '<font size=11>Propuesta de Compra Arriendo y Posterior Venta en un Período de 7 Meses, ofertando 95% Valor propiedad, Revendiendo a 95%  del valor de tasación:</font>'
        Story.append(Paragraph(ftext, styles["Justify"]))
        Story.append(Spacer(1, 14))
        rent=(1+(((0.95*tasacionUF-((0.95)*precioufreal))*0.81-((0.95)*precioufreal)*0.031)-25+precioAreal*7/uf)/((0.95)*precioufreal*1.031+25)-0.25*((((0.95*tasacionUF-((0.95)*precioufreal))*0.81-((0.95)*precioufreal)*0.031)-25+precioAreal*7/uf)/((0.95)*precioufreal*1.031+25)-0.05))**(12/7)-1
        data=[["Item","Valor"],
              ["Rent. de arriendo(1)",str(int(1000*(precioAreal*12/uf/((0.95)*precioufreal*1.031+14)))/10)+"%"],
              ["Rent. Capital (2)",str(int(1000*(((0.95*tasacionUF-((0.95)*precioufreal))*0.81-((0.95)*precioufreal)*0.031)-14)/((0.95)*precioufreal*1.031+14))/10)+"%"],
              ["Rent. Total(3)",str(int(1000*(((0.95*tasacionUF-((0.95)*precioufreal))*0.81-((0.95)*precioufreal)*0.031)-14+precioAreal*7/uf)/((0.95)*precioufreal*1.031+14))/10)+"%"],
              ["Rentabilidad Neta(4)",str(int(1000*((1+rent)**(7/12)-1))/10)+"%"],
              ["Rentabilidad Neta UF (5)",str(int(((int((0.95)*precioufreal*1.031+25))*((1+rent)**(7/12)-1))))+" UF"],
              ["Rentabilidad Anual Neta(6)",str(int(1000*rent)/10)+"%"],
              ["Costos Legales(7)","25 UF"],
              ["Costos de Corretaje(8)",str(int(0.02*0.95*precioufreal))+" UF"],
              ["IVA(9)",str(int((0.95*tasacionUF-((0.95)*precioufreal))*0.19))+" UF"],
              ["Total Inversión Inicial(10)",str(int((0.95)*precioufreal*1.031+25))+" UF"],
              ["Comisión BullEstate(11)",str(int(0.25*((((0.95*tasacionUF-((0.95)*precioufreal))*0.81-((0.95)*precioufreal)*0.031)-25+precioAreal*7/uf)-0.05*((0.95)*precioufreal*1.031+25))+0.01*0.95*precioufreal))+" UF"]]


        t=Table(data)
        table_style=(TableStyle([
                               ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                               ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                               ('BACKGROUND',(0,0), (-1,0),colors.HexColor('#34BAAF')),
                               ('TEXTCOLOR',(0,0), (-1,0),colors.black),
                               ('FONTSIZE', (0,0), (-1,-1), 9),
                               ]))
        t.setStyle(table_style)
        Story.append(t)
        Story.append(Spacer(1, 14))

        ftext = '<font size=6>(1)Rentabilidad calculada como doce veces el valor de arriendo dividido por el total de inversión.</font>'
        Story.append(Paragraph(ftext, styles["Justify"]))
        ftext = '<font size=6>(2)Rentabilidad calculada como (valor de reventa - total inversión)/total inversión.</font>'
        Story.append(Paragraph(ftext, styles["Justify"]))
        ftext = '<font size=6>(3)Rentabilidad de Arriendo + Rentabilidad de Capital, durante ciclo de inversión.</font>'
        Story.append(Paragraph(ftext, styles["Justify"]))
        ftext = '<font size=6>(4)Rentabilidad neta de un ciclo de inversión, descontando gastos.</font>'
        Story.append(Paragraph(ftext, styles["Justify"]))
        ftext = '<font size=6>(5)Rentabilidad neta en UF de un ciclo de inversión, descontando gastos.</font>'
        Story.append(Paragraph(ftext, styles["Justify"]))
        ftext = '<font size=6>(6)Rentabilidad neta anualizada</font>'
        Story.append(Paragraph(ftext, styles["Justify"]))
        ftext = '<font size=6>(7)Estudio de títulos, pago de CBR y notaría.</font>'
        Story.append(Paragraph(ftext, styles["Justify"]))
        ftext = '<font size=6>(8)Valor correspondiente al 2% de costos de corretaje, al comprar propiedad</font>'
        Story.append(Paragraph(ftext, styles["Justify"]))
        ftext = '<font size=6>(9) Valor correspondiente al 19% de la diferencia entre valor compra y valor re-venta</font>'
        Story.append(Paragraph(ftext, styles["Justify"]))
        ftext = '<font size=6>(10) Valor propiedad más corretaje, gastos legales, y comisión Fija de Bullestate</font>'
        Story.append(Paragraph(ftext, styles["Justify"]))
        ftext = '<font size=6>(11)Comisión correspondiente al 1% más un 25% de la utilidad obtenida sobre 5% por parte del Cliente.</font>'
        Story.append(Paragraph(ftext, styles["Justify"]))
        Story.append(Spacer(1, 14))
        Story.append(PageBreak())

        reventas=[0.9,0.925,0.95,0.975,1]

        for rev in reventas:
            ftext = '<font size=11>INFO FINANCIERA (Reventa al '+(str(int(1000*rev)/10)).replace('.',',')+'% - '+str(format(int(rev*tasacionUF),',')).replace(',','.')+' UF - $' +str(format(int(rev*tasacion),',')).replace(',','.')+ ':</font>'

            Story.append(Paragraph(ftext, styles["Justify"]))
            Story.append(Spacer(1, 14))
            data=[]
            headers=["Valor UF:","Valor Pesos", "% Oferta"]
            for i in range (1,16):
                headers.append(str(i))


            for n in range (0,9):
                row=[]
                row.append((str(format(int((0.8+0.025*n)*precioufreal),','))).replace(',','.'))
                row.append((str(format(int((0.8+0.025*n)*precioreal),','))).replace(',','.'))
                row.append(str(80+2.5*n)+"%")
                for i in range (1,16):
                    tasacionUF=float(tasacionUF)
                    precioufreal=float(precioufreal)
                    precioAreal=float(precioAreal)
                    uf=float(uf)
                    rev=float(rev)
                    rent=(1+(((rev*tasacionUF-((0.8+0.025*n)*precioufreal))*0.81-((0.8+0.025*n)*precioufreal)*0.031)-25+precioAreal*i/uf)/((0.8+0.025*n)*precioufreal*1.031+25)-0.25*((((rev*tasacionUF-((0.8+0.025*n)*precioufreal))*0.81-((0.8+0.025*n)*precioufreal)*0.031)-25+precioAreal*i/uf)/((0.8+0.025*n)*precioufreal*1.031+25)-0.05))**(12/i)-1
                    rent=str((int(1000*rent))/10)+"%"
                    row.append(rent)
                data.append(row)



            data = [headers]+data
            #t=Table(data,nrCols*[0.6*inch], nrRows*[0.25*inch])
            t=Table(data)
            table_style=(TableStyle([
                                   ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                                   ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                                   ('BACKGROUND',(0,0), (-1,0),colors.HexColor('#34BAAF')),
                                   ('TEXTCOLOR',(0,0), (-1,0),colors.black),
                                   ('FONTSIZE', (0,0), (-1,-1), 6.5),
                                   ]))
            t.setStyle(table_style)
            for row, values, in enumerate(data):
                for column, value in enumerate(values):
                    try:
                        print(value)
                        intvalue=float(value[:-1])
                        print(intvalue)
                        if intvalue < 0:
                            table_style.add('BACKGROUND', (column, row), (column, row), colors.red)
                        if intvalue > 0.2:
                            table_style.add('BACKGROUND', (column, row), (column, row), colors.limegreen)
                        if intvalue > 0.5:
                            table_style.add('BACKGROUND', (column, row), (column, row), colors.darkgreen)
                    except:
                        pass
            Story.append(t)
            Story.append(Spacer(1, 14))
        Story.append(PageBreak())



    for x in range(0,lenfotos):

        image = Image(str(x)+" foto.jpg", hAlign='LEFT')
        image._restrictSize(6 * inch, 9 * inch)
        Story.append(image)
        Story.append(Spacer(1, 4))

    Story=list(Story)
    doc.build(Story)
