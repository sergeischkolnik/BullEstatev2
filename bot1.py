import json
import requests
import time
import urllib
import pymysql as mysql
import datetime as dt
import propManager as pm
import googleMapApi as gm
import tasadorbot2 as tb2
import reportes as rp
import threading
import mailBotClientesArriendoFrancisca
import mailBotClientesVentaFernanda

thrFran = -1
thrFer = -1
thrReportes = -1

TOKEN = "633816057:AAE30k3FguvhUq5faEbtvsLWP_J6s2sqL5M"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


TOKEN2 = "789420054:AAFEYW1c0pgN9d3Mo3L2DFEEEGUAY8QCJ-4"
URL2 = "https://api.telegram.org/bot{}/".format(TOKEN2)

#TODOS LOS COMANDOS SIEMPRE SOLO MINUSCULAS
comandosIndividuales = ['hola',
                        'portal',
                        'goplaceit',
                        'reporte',
                        'tasador',
                        'tasadorlinks',
                        'clientesmailer',
                        'clientesmailerlinks',
                        'actualizarestadodueno',
                        'actualizarcomentariodueno',
                        'lastscrapportal',
                        'gofernanda',
                        'stopfernanda',
                        'gofrancisca',
                        'stopfrancisca']

comandosMultiples = ['reporte',
                     'reporteinterno'
                     'tasador',
                     'tasadorlinks',
                     'banear',
                     'actualizarestadodueno',
                     'actualizarcomentariodueno',]

id_chats_updates = ["485728961","652659504","9561926"]


def estadoScrapper(chatId):

    #Añadir regiones a arreglo
    region = ["metropolitana","valparaiso","biobio"]

    #Añadir operaciones a arreglo
    operacion = ["venta", "arriendo"]

    #Añadir tipo a arreglo
    tipo = ["departamento", "casa", "oficina","sitio", "comercial", "estacionamiento"]

    text = ""

    for reg in region:
        for tip in tipo:
            for op in operacion:
                sql = "SELECT MAX(fechascrap) from portalinmobiliario where region='"+reg+"' and tipo='"+tip+"' and operacion='"+op+"'"

                mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1',
                                                   database='bullestate')
                cur = mariadb_connection.cursor()
                cur.execute(sql)
                lista = cur.fetchall()
                mariadb_connection.close()
                fecha = lista[0]
                fecha = str(fecha[0])
                split = fecha.split('-')
                dia = split[2]
                mes = split[1]
                anio = split[0]
                text = reg + " - " + tip + " - " + op +" :" + str(dia) + "/" + str(mes) + "/" + str(anio)
                send_message(text,chatId,URL)

def actualizarestadodueno(mail, nuevoEstado):
    sql = "SELECT * from duenos WHERE mail='"+str(mail)+"'"
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    lista = cur.fetchall()
    mariadb_connection.close()
    if len(lista)>0:
        if nuevoEstado!="null":
            sql = "UPDATE duenos SET estado='"+str(nuevoEstado)+"' WHERE mail='"+str(mail)+"'"
            mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
            cur = mariadb_connection.cursor()
            cur.execute(sql)
            mariadb_connection.commit()
            mariadb_connection.close()
            text = "Actualizado el estado de " + str(mail) + " a " + str(nuevoEstado)
        else:
            mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
            cur = mariadb_connection.cursor()
            value = None
            cur.execute("UPDATE duenos SET estado=%s WHERE mail=%s", (value,mail))
            mariadb_connection.commit()
            mariadb_connection.close()
            text = "Actualizado el estado de " + str(mail) + " a null"
    else:
        text = "Mail equivocado."

    return text

def actualizarcomentariodueno(mail, nuevoComentario):
    sql = "SELECT * from duenos WHERE mail='" + str(mail) + "'"
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    lista = cur.fetchall()
    mariadb_connection.close()
    if len(lista)>0:
        sql = "UPDATE duenos SET comentario='"+str(nuevoComentario)+"' WHERE mail='"+str(mail)+"'"
        mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
        cur = mariadb_connection.cursor()
        cur.execute(sql)
        mariadb_connection.commit()
        mariadb_connection.close()
        text = "Actualizado el comentario de " + str(mail) + " a " + str(nuevoComentario)
    else:
        text = "Mail equivocado."

    return text

def getClientesMailer(chatId):
    sql="SELECT duenos.mail,duenos.comision,duenos.exclusividad,duenos.estado,portalinmobiliario.precio," \
        "portalinmobiliario.tipo,portalinmobiliario.fechapublicacion,duenos.comentario from " \
        "duenos inner join portalinmobiliario where " \
        "duenos.idProp=portalinmobiliario.id2 and estado IS NOT NULL"
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    lista = cur.fetchall()
    mariadb_connection.close()
    totalClients = len(lista)

    for elem in lista:
        text = ""
        text += "Mail: " + str(elem[0]) + "\n"
        text += "Comision: " + str(elem[1]) + "%\n"
        text += "Exclusividad: " + str(elem[2]) + "\n"
        text += "Estado: " + str(elem[3]) + "\n"
        text += "Precio Propiedad: $" + str('{:20,.0f}'.format((int(elem[4]))).replace(',','.').replace(' ','')) + " pesos\n"
        text += "Tipo: " + str(elem[5]) + "\n"
        text += "Fecha publicacion: " + str(elem[6]) + "\n"
        text += "Comentario:" + str(elem[7]) + "\n"
        text += "\n"
        send_message(text,chatId,URL)

    ret = "Clientes activos del mailer: " + str(totalClients) + "\n"

    return ret

def getClientesMailerLinks(chatId):
    sql="SELECT duenos.mail,duenos.comision,duenos.exclusividad,duenos.estado,portalinmobiliario.precio," \
        "portalinmobiliario.fechapublicacion,portalinmobiliario.link,duenos.comentario from duenos inner join portalinmobiliario where " \
        "duenos.idProp=portalinmobiliario.id2 and estado IS NOT NULL"
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    lista = cur.fetchall()
    mariadb_connection.close()
    totalClients = len(lista)

    for elem in lista:
        text = ""
        text += "Mail: " + str(elem[0]) + "\n"
        text += "Comision: " + str(elem[1]) + "%\n"
        text += "Exclusividad: " + str(elem[2]) + "\n"
        text += "Estado: " + str(elem[3]) + "\n"
        text += "Precio Propiedad: $" + str('{:20,.0f}'.format((int(elem[4]))).replace(',','.').replace(' ','')) + " pesos\n"
        text += "Fecha publicacion: " + str(elem[5]) + "\n"
        text += "Link: " + str(elem[6]) + "\n"
        text += "Comentario:" + str(elem[7]) + "\n"
        text += "\n"
        send_message(text,chatId,URL)

    ret = "Clientes activos del mailer: " + str(totalClients) + "\n"

    return ret

def insertarBanned(mail):
    sql="INSERT INTO baneados(mail) VALUES('"+str(mail)+"') ON DUPLICATE KEY UPDATE mail='"+str(mail)+"'"
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    mariadb_connection.commit()
    mariadb_connection.close()
    quitarDueno(mail)

def quitarDueno(mail):

    sql = "UPDATE duenos SET esDueno='no' WHERE mail='"+str(mail)+"'"

    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')

    cur = mariadb_connection.cursor()
    cur.execute(sql)
    mariadb_connection.commit()
    mariadb_connection.close()

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url+="&offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def echo_all(updates):
    global thrFran
    global thrFer
    global thrReportes
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            text = text.strip(' ')
            text = text.lower()

            arr = text.split(' ')

            if len(arr)==1:
                #comandos simples
                text = arr[0]
                
                #Hola y bienvenida
                if text==comandosIndividuales[0]:
                    text="Hola! Los comandos son:"
                    for c in comandosIndividuales:
                        text+="\n" + c
               
                #propiedades portal
                elif text==comandosIndividuales[1]:
                    sp = pm.selectorPortal()
                    if sp != -1:
                        text="Propiedades de portal scrapeadas:" + str(sp)
                    else:
                        text="Hubo un error de base de datos."
              
                #propiedades gp
                elif text==comandosIndividuales[2]:
                    gp = pm.selectorGP()
                    if gp != -1:
                        text="Propiedades de GP scrapeadas:" + str(gp)
                    else:
                        text="Error de base de datos."
              
                #reportes
                elif text==comandosIndividuales[3]:
                    text = "Para usar reporte, escriba, separando por espacios:\nreporte " \
                           "<precioMin> <precioMax> <utilMin> <utilMax> <totalMin> <totalMax> " \
                           "<latMin> <latMax> <lonMin> <lonMax> <dormitoriosMin> <dormitoriosMax>" \
                           "<banosMin> <banosMax> <estacionamientos> <tipo> <operacion> <estado>" \
                           "<region> <comuna> <distanciaMetro> <rentMin> <prioridad (venta, arriendo, nada>" \
                           "<confianzaMinima (1-8)> <mail> <nombre>"
                #tasador
                elif text==comandosIndividuales[4]:
                    text = "Para usar tasador, escriba, separando por espacios:\ntasador <region> <comuna> " \
                               "<operacion> <tipo> <estado> <dormitorios> <baños> <mtUtiles> <mtTotales> " \
                               "<nrEstacionamientos> <año> <piso> <orientacion> <nombreCalle> <numeroDireccion>"

                #tasadorlinks
                elif text==comandosIndividuales[5]:
                    text = "Para usar tasador con links, escriba, separando por espacios:\ntasadorlinks <region> <comuna> " \
                               "<operacion> <tipo> <estado> <dormitorios> <baños> <mtUtiles> <mtTotales> " \
                               "<nrEstacionamientos> <año> <piso> <orientacion> <nombreCalle> <numeroDireccion>"

                #clientesmailer
                elif text==comandosIndividuales[6]:
                    chatId = update["message"]["chat"]["id"]
                    text = getClientesMailer(chatId)

                # clientesmailerLinks
                elif text==comandosIndividuales[7]:
                    chatId = update["message"]["chat"]["id"]
                    text = getClientesMailerLinks(chatId)

                #actualizar estado dueño
                elif text == comandosIndividuales[8]:
                    text = "Para actualizar el estado de un dueño escriba:\nactualizarestadodueno <mail> <nuevo Estado>"

                # actualizar comentario dueño
                elif text == comandosIndividuales[9]:
                    text = "Para actualizar un cliente escriba:\nactualizarcomentariodueno <mail> <nuevo comentario>"

                # estado de ultimos scrapeos portal
                elif text == comandosIndividuales[10]:
                    text = "\n"
                    chatId = update["message"]["chat"]["id"]
                    estadoScrapper(chatId)

                #go Fernanda - venta
                elif text == comandosIndividuales[11]:
                    if thrFer == -1 or not thrFer.isAlive():
                        thrFer = threading.Thread(target=mailBotClientesVentaFernanda.threadSendMails, args=())
                        thrFer.setDaemon(True)
                        thrFer.start()
                        text = "Partiendo Fernanda (captadora de ventas)"
                    else:
                        text = "Fernanda (captadora de ventas.) ya esta andando."

                #stop Fernanda  venta
                elif text == comandosIndividuales[12]:
                    if thrFer != -1 and thrFer.isAlive():
                        thrFer.do_run = False
                        text = "Parando Fernanda (captadora de ventas)"
                    else:
                        text = "Fernanda (captadora de ventas) ya esta detenida."

                # go Francisca - arriendo
                elif text == comandosIndividuales[13]:
                    if thrFran == -1 or not thrFran.isAlive():
                        thrFran = threading.Thread(target=mailBotClientesArriendoFrancisca.threadSendMails, args=())
                        thrFran.setDaemon(True)
                        thrFran.start()
                        text = "Partiendo Francisca (captadora de arriendos)."
                    else:
                        text="Francisca (captadora de arriendos) ya esta andando."

                # stop Francisca  arriendo
                elif text == comandosIndividuales[14]:
                    if thrFran != -1 and thrFran.isAlive():
                        thrFran.do_run = False
                        text = "Parando Francisca (captadora de arriendos)."
                    else:
                        text = "Francisca (captadora de arriendos) ya esta detenida."

                #no encontrado
                else:
                    text = "Comando desconocido. Los comandos dispobibles son:"
                    for c in comandosIndividuales:
                        text+="\n" + c
            
            elif len(arr)>1:
                #comandos multiples

                #reportes
                if arr[0] == comandosMultiples[0]:
                    if len(arr)!=26:
                        text = "Para usar reporte, escriba, separando por espacios:\nreporte " \
                               "<precioMin> <precioMax> <utilMin> <utilMax> <totalMin> <totalMax> " \
                               "<latMin> <latMax> <lonMin> <lonMax> <dormitoriosMin> <dormitoriosMax>" \
                               "<banosMin> <banosMax> <estacionamientos> <tipo> <operacion>" \
                               "<region> <comuna> <distanciaMetro> <rentMin> <prioridad (venta, arriendo, nada>" \
                               "<confianzaMinima (1-8)> <mail> <nombre>"
                    else:

                        if thrReportes!= -1 and thrReportes.isAlive():
                            text = "Ya se está generando un reporte. Espere a que termine antes de generar otro para " \
                                   "no colapsar nuestros servidores."

                        else:
                            preciomin = arr[1]
                            preciomax = arr[2]
                            utilmin = arr[3]
                            utilmax = arr[4]
                            totalmin = arr[5]
                            totalmax = arr[6]
                            latmin = arr[7]
                            latmax = arr[8]
                            lonmin = arr[9]
                            lonmax = arr[10]
                            dormitoriosmin = arr[11]
                            dormitoriosmax = arr[12]
                            banosmin = arr[13]
                            banosmax = arr[14]
                            estacionamientos = arr[15]
                            tipo = arr[16]
                            operacion = arr[17]
                            region = arr[18]
                            comuna = arr[19]
                            distanciaMetro = arr[20]
                            rentMin = arr[21]
                            prioridad = arr[22]
                            confianzaMinima = arr[23]
                            mail = arr[24]
                            nombre = arr[25]



                            thrReportes = threading.Thread(target=rp.generarReporte, args=(preciomin, preciomax,
                                                                                           utilmin,utilmax, totalmin,
                                                                                           totalmax, latmin, latmax,
                                                                                           lonmin, lonmax,dormitoriosmin,
                                                                                           dormitoriosmax, banosmin,
                                                                                           banosmax, confianzaMinima,
                                                                                           rentMin, estacionamientos,
                                                                                           distanciaMetro, tipo,
                                                                                           operacion, region, comuna,
                                                                                           "abcdefgh", "abcdefgh",
                                                                                           "abcdefgh","abcdefgh",
                                                                                           "abcdefgh", prioridad, 1,
                                                                                           mail, nombre,False,))

                            thrReportes.setDaemon(True)
                            thrReportes.start()

                            # rp.generarReporte(preciomin, preciomax, utilmin, utilmax, totalmin, totalmax, latmin, latmax,
                            #               lonmin, lonmax,dormitoriosmin,dormitoriosmax, banosmin, banosmax, confianzaMinima,
                            #               rentMin, estacionamientos, distanciaMetro, tipo, operacion, region, comuna1=comuna,
                            #               comuna2="abcdefgh", comuna3="abcdefgh", comuna4="abcdefgh", comuna5="abcdefgh",
                            #               comuna6="abcdefgh", prioridad=prioridad, flagMail=1, mail=mail, nombreCliente=nombre)


                            text = "Generando reporte para:" + nombre
                            text += "\n\n"
                            text += "preciomin:" + preciomin + "\n"
                            text += "preciomax:" +  preciomax+ "\n"
                            text += "utilmin:" + utilmin+ "\n"
                            text += "utilmax:" + utilmax+ "\n"
                            text += "totalmin:" + totalmin+ "\n"
                            text += "totalmax:" + totalmax+ "\n"
                            text += "latmin:" + latmin+ "\n"
                            text += "latmax:" + latmax+ "\n"
                            text += "lonmin:" + lonmin+ "\n"
                            text += "lonmax:" + lonmax+ "\n"
                            text += "dormitoriosmin:" + dormitoriosmin+ "\n"
                            text += "dormitoriosmax:" + dormitoriosmax+ "\n"
                            text += "banosmin:" + banosmin+ "\n"
                            text += "banosmax:" + banosmax+ "\n"
                            text += "estacionamientos:" + estacionamientos+ "\n"
                            text += "tipo:" + tipo+ "\n"
                            text += "operacion:" + operacion+ "\n"
                            text += "region:" + region+ "\n"
                            text += "comuna:" + comuna+ "\n"
                            text += "distanciaMetro:" + distanciaMetro+ "\n"
                            text += "rentMin:" + rentMin+ "\n"
                            text += "prioridad:" + prioridad+ "\n"
                            text += "confianzaMinima:" + confianzaMinima+ "\n"
                            text += "mail:" + mail + "\n"
                            text += "nombre:" + nombre+ "\n"

                #reporte interno
                elif arr[0] == comandosMultiples[1]:
                    if len(arr)!=26:
                        text = "Para usar reporte, escriba, separando por espacios:\nreporte " \
                               "<precioMin> <precioMax> <utilMin> <utilMax> <totalMin> <totalMax> " \
                               "<latMin> <latMax> <lonMin> <lonMax> <dormitoriosMin> <dormitoriosMax>" \
                               "<banosMin> <banosMax> <estacionamientos> <tipo> <operacion>" \
                               "<region> <comuna> <distanciaMetro> <rentMin> <prioridad (venta, arriendo, nada>" \
                               "<confianzaMinima (1-8)> <mail> <nombre>"
                    else:

                        if thrReportes!= -1 and thrReportes.isAlive():
                            text = "Ya se está generando un reporte. Espere a que termine antes de generar otro para " \
                                   "no colapsar nuestros servidores."

                        else:
                            preciomin = arr[1]
                            preciomax = arr[2]
                            utilmin = arr[3]
                            utilmax = arr[4]
                            totalmin = arr[5]
                            totalmax = arr[6]
                            latmin = arr[7]
                            latmax = arr[8]
                            lonmin = arr[9]
                            lonmax = arr[10]
                            dormitoriosmin = arr[11]
                            dormitoriosmax = arr[12]
                            banosmin = arr[13]
                            banosmax = arr[14]
                            estacionamientos = arr[15]
                            tipo = arr[16]
                            operacion = arr[17]
                            region = arr[18]
                            comuna = arr[19]
                            distanciaMetro = arr[20]
                            rentMin = arr[21]
                            prioridad = arr[22]
                            confianzaMinima = arr[23]
                            mail = arr[24]
                            nombre = arr[25]



                            thrReportes = threading.Thread(target=rp.generarReporte, args=(preciomin, preciomax,
                                                                                           utilmin,utilmax, totalmin,
                                                                                           totalmax, latmin, latmax,
                                                                                           lonmin, lonmax,dormitoriosmin,
                                                                                           dormitoriosmax, banosmin,
                                                                                           banosmax, confianzaMinima,
                                                                                           rentMin, estacionamientos,
                                                                                           distanciaMetro, tipo,
                                                                                           operacion, region, comuna,
                                                                                           "abcdefgh", "abcdefgh",
                                                                                           "abcdefgh","abcdefgh",
                                                                                           "abcdefgh", prioridad, 2,
                                                                                           mail, nombre,False,))

                            thrReportes.setDaemon(True)
                            thrReportes.start()

                            # rp.generarReporte(preciomin, preciomax, utilmin, utilmax, totalmin, totalmax, latmin, latmax,
                            #               lonmin, lonmax,dormitoriosmin,dormitoriosmax, banosmin, banosmax, confianzaMinima,
                            #               rentMin, estacionamientos, distanciaMetro, tipo, operacion, region, comuna1=comuna,
                            #               comuna2="abcdefgh", comuna3="abcdefgh", comuna4="abcdefgh", comuna5="abcdefgh",
                            #               comuna6="abcdefgh", prioridad=prioridad, flagMail=1, mail=mail, nombreCliente=nombre)


                            text = "Generando reporte para:" + nombre
                            text += "\n\n"
                            text += "preciomin:" + preciomin + "\n"
                            text += "preciomax:" +  preciomax+ "\n"
                            text += "utilmin:" + utilmin+ "\n"
                            text += "utilmax:" + utilmax+ "\n"
                            text += "totalmin:" + totalmin+ "\n"
                            text += "totalmax:" + totalmax+ "\n"
                            text += "latmin:" + latmin+ "\n"
                            text += "latmax:" + latmax+ "\n"
                            text += "lonmin:" + lonmin+ "\n"
                            text += "lonmax:" + lonmax+ "\n"
                            text += "dormitoriosmin:" + dormitoriosmin+ "\n"
                            text += "dormitoriosmax:" + dormitoriosmax+ "\n"
                            text += "banosmin:" + banosmin+ "\n"
                            text += "banosmax:" + banosmax+ "\n"
                            text += "estacionamientos:" + estacionamientos+ "\n"
                            text += "tipo:" + tipo+ "\n"
                            text += "operacion:" + operacion+ "\n"
                            text += "region:" + region+ "\n"
                            text += "comuna:" + comuna+ "\n"
                            text += "distanciaMetro:" + distanciaMetro+ "\n"
                            text += "rentMin:" + rentMin+ "\n"
                            text += "prioridad:" + prioridad+ "\n"
                            text += "confianzaMinima:" + confianzaMinima+ "\n"
                            text += "mail:" + mail + "\n"
                            text += "nombre:" + nombre+ "\n"

                #tasador
                elif arr[0] == comandosMultiples[2]:
                    if len(arr)< 16:
                        text = "Para usar tasador, escriba, separando por espacios:\ntasador <region> <comuna> " \
                               "<operacion> <tipo> <estado> <dormitorios> <baños> <mtUtiles> <mtTotales> " \
                               "<nrEstacionamientos> <año> <piso> <orientacion> <nombreCalle> <numeroDireccion>"
                    else:
                        region = arr[1]
                        comuna = arr[2]

                        if arr[3]=="venta" or arr[3]=="arriendo": #1 palabra
                            n=0
                        elif arr[4]=="venta" or arr[4]=="arriendo": #2 palabras
                            n=1
                            comuna+=" "+arr[3]
                        elif arr[5]=="venta" or arr[5]=="arriendo": #3 palabras
                            n=2
                            comuna+=" "+arr[3]+" "+arr[4]
                        elif arr[6]=="venta" or arr[6]=="arriendo": #4 palabras
                            n=2
                            comuna+=" "+arr[3]+" "+arr[4]+" "+arr[5]
                        else:
                            n=-1

                        if n>=0:
                            operacion = arr[3+n]
                            tipo = arr[4+n]
                            estado = arr[5+n]
                            dormitorios = arr[6+n]
                            banos = arr[7+n]
                            mtUtiles = arr[8+n]
                            mtTotales = arr[9+n]
                            nrEstacionamientos = arr[10+n]
                            ano = arr[11+n]
                            piso = arr[12+n]
                            orientacion = arr[13+n]

                            calle = ""
                            for c in range(14+n,len(arr)-1):
                                calle += arr[c]
                                calle += " "

                            nrCalle = arr[len(arr)-1]
                            direccion = str(calle) + str(nrCalle) + ", " + str(comuna) + ", Chile"
                            lat,lon = gm.getCoordsWithAdress(direccion)

                            precio,nivel,nrcomp,links,es_venta = tb2.calcularTasacion(operacion=operacion,tipo=tipo,lat=float(lat),lon=float(lon),util=float(mtUtiles),
                                                         total=float(mtTotales),dormitorios=int(dormitorios),banos=int(banos),
                                                         estacionamientos=int(nrEstacionamientos))
                            if es_venta:
                                text = "El precio tasado es UF " + str(precio)+", con un nivel de confianza: "+str(nivel)+\
                                   ", tasación realizada comparandose con "+str(nrcomp)+" propiedades."
                            else:
                                text = "El precio tasado es $" + str(precio)+", con un nivel de confianza: "+str(nivel)+\
                                   ", tasación realizada comparandose con "+str(nrcomp)+" propiedades."

                        else:
                            text = "Error de ingreso de datos."

                #tasador con links
                elif arr[0] == comandosMultiples[3]:
                    if len(arr)< 16:
                        text = "Para usar tasador con links, escriba, separando por espacios:\ntasadorlinks <region> <comuna> " \
                               "<operacion> <tipo> <estado> <dormitorios> <baños> <mtUtiles> <mtTotales> " \
                               "<nrEstacionamientos> <año> <piso> <orientacion> <nombreCalle> <numeroDireccion>"
                    else:
                        region = arr[1]
                        comuna = arr[2]

                        if arr[3]=="venta" or arr[3]=="arriendo": #1 palabra
                            n=0
                        elif arr[4]=="venta" or arr[4]=="arriendo": #2 palabras
                            n=1
                            comuna+=" "+arr[3]
                        elif arr[5]=="venta" or arr[5]=="arriendo": #3 palabras
                            n=2
                            comuna+=" "+arr[3]+" "+arr[4]
                        elif arr[6]=="venta" or arr[6]=="arriendo": #4 palabras
                            n=2
                            comuna+=" "+arr[3]+" "+arr[4]+" "+arr[5]
                        else:
                            n=-1

                        if n>=0:
                            operacion = arr[3+n]
                            tipo = arr[4+n]
                            estado = arr[5+n]
                            dormitorios = arr[6+n]
                            banos = arr[7+n]
                            mtUtiles = arr[8+n]
                            mtTotales = arr[9+n]
                            nrEstacionamientos = arr[10+n]
                            ano = arr[11+n]
                            piso = arr[12+n]
                            orientacion = arr[13+n]

                            calle = ""
                            for c in range(14+n,len(arr)-1):
                                calle += arr[c]
                                calle += " "

                            nrCalle = arr[len(arr)-1]
                            direccion = str(calle) + str(nrCalle) + ", " + str(comuna) + ", Chile"
                            lat,lon = gm.getCoordsWithAdress(direccion)

                            precio,nivel,nrcomp,links,es_venta = tb2.calcularTasacion(operacion=operacion,tipo=tipo,lat=float(lat),lon=float(lon),util=float(mtUtiles),
                                                         total=float(mtTotales),dormitorios=int(dormitorios),banos=int(banos),
                                                         estacionamientos=int(nrEstacionamientos))
                            text = "El precio tasado es UF " + str(precio)+", con un nivel de confianza: "+str(nivel)+\
                                   ", tasación realizada comparandose con "+str(nrcomp)+" propiedades.\nLinks:"
                            for link in links:
                                text += "\n\n" + str(link)
                            text=text[:4000]
                        else:
                            text = "Error de ingreso de datos."

                #Banear corredores
                elif arr[0] == comandosMultiples[4]:
                    if len(arr)!=2:
                        text="Para usar baneador, ingrese 'banear mail'"
                    else:
                        insertarBanned(arr[1])
                        text=str(arr[1])+" agregado a la lista de Baneados."

                #actualizar estado cliente
                elif arr[0] == comandosMultiples[5]:
                    nuevoEstado = ""
                    for a in arr[2:]:
                        nuevoEstado += a + " "
                    nuevoEstado = nuevoEstado[:-1]
                    text = actualizarestadodueno(mail=arr[1], nuevoEstado=nuevoEstado)

                # actualizar comentario cliente
                elif arr[0] == comandosMultiples[6]:
                    nuevoComentario = ""
                    for a in arr[2:]:
                        nuevoComentario += a + " "

                    nuevoComentario = nuevoComentario[:-1]
                    text = actualizarcomentariodueno(mail=arr[1], nuevoComentario=nuevoComentario)

                else:
                    text = "Comando desconocido. Los comandos dispobibles son:"
                    for c in comandosIndividuales:
                        text+="\n" + c
            else:
                text = "Comando desconocido. Los comandos dispobibles son:"
                for c in comandosIndividuales:
                    text+="\n" + c

            chat = update["message"]["chat"]["id"]
            send_message(text, chat, URL)
        except Exception as e:
            print("[tgBot]" + str(e))

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)

def send_message(text, chat_id,urlP):
    text = urllib.parse.quote_plus(text)
    url = urlP + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)
    print("[tgBot] send to:" + str(chat_id) + " -> " + str(text))

def main():
    currentMinute= dt.datetime.now().minute
    last_update_id = None
    avisado = False
    print("[tgBot] Bot andando.")

    while True:
        updates = get_updates(last_update_id)
        result = updates.get("result")
        if result:
            if len(result) > 0:
                last_update_id = get_last_update_id(updates) + 1
                echo_all(updates)

        if dt.datetime.now().minute != currentMinute:
            currentMinute = dt.datetime.now().minute
            lastScrap = pm.getLastScrap()
            if lastScrap != -1:
                if dt.datetime.now()-dt.timedelta(minutes=10) > lastScrap:
                    if not avisado:
                        for idchat in id_chats_updates:
                            send_message("Falla en portal", idchat,URL2)
                        avisado = True
                else:
                    avisado = False
        time.sleep(5)

def selectorPortal():
    sql = "SELECT COUNT(id) from portalinmobiliario"
    conn = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = conn.cursor()
    cur.execute(sql)
    tupla = cur.fetchall()
    num = int(tupla[0][0])
    return num

if __name__ == '__main__':
    main()
