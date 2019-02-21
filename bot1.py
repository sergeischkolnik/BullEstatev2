import json
import requests
import time
import urllib
import pymysql as mysql
import datetime as dt
import propManager as pm
import googleMapApi as gm
import tasadorbot as tb

TOKEN = "633816057:AAE30k3FguvhUq5faEbtvsLWP_J6s2sqL5M"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


TOKEN2 = "789420054:AAFEYW1c0pgN9d3Mo3L2DFEEEGUAY8QCJ-4"
URL2 = "https://api.telegram.org/bot{}/".format(TOKEN2)

comandosIndividuales = ['hola','portal','goplaceit','reporte','tasador','tasadorlinks']
comandosMultiples = ['reporte','tasador','tasadorlinks','banear']
id_chats_updates = ["485728961","652659504"]

def insertarBanned(mail):
    sql="INSERT INTO baneados(mail) VALUES(%s)"
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sql, (mail))
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
                    text="Propiedades de portal scrapeadas:" + str(pm.selectorPortal())
              
                #propiedades gp
                elif text==comandosIndividuales[2]:
                    text="Propiedades de GP scrapeadas:" + str(pm.selectorGP())
              
                #reportes
                elif text==comandosIndividuales[3]:
                    text = "Para usar reporte, escriba, separando por espacios:\nreporte <region> <comuna> <operacion> <tipo> <estado> <dormitorios> <baños>"

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

                #no encontrado
                else:
                    text = "Comando desconocido. Los comandos dispobibles son:"
                    for c in comandosIndividuales:
                        text+="\n" + c
            
            elif len(arr)>1:
                #comandos multiples

                #reportes
                if arr[0] == comandosMultiples[0]:
                    if len(arr)!=8:
                        text = "Para usar reporte, escriba, separando por espacios:\nreporte <region <comuna> " \
                               "<operacion> <tipo> <estado> <dormitorios> <baños>"
                    else:
                        region = arr[1]
                        comuna = arr[2]
                        operacion = arr[3]
                        tipo = arr[4]
                        estado = arr[5]
                        dormitorios = arr[6]
                        banos = arr[7]
                        text = "Generando reporte para:"
                        text += "\nRegion:" + region
                        text += "\nComuna:" + comuna
                        text += "\nOperacion:" + operacion
                        text += "\nTipo:" + tipo
                        text += "\nEstado:" + estado
                        text += "\nDormitorios:" + dormitorios
                        text += "\nBaños:" + banos
                        #Agregar codigo aca para generar reporte

                #tasador
                elif arr[0] == comandosMultiples[1]:
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

                            precio,nivel,nrcomp,links = tb.calcularTasacion(operacion=operacion,tipo=tipo,lat=float(lat),lon=float(lon),util=float(mtUtiles),
                                                         total=float(mtTotales),dormitorios=int(dormitorios),banos=int(banos),
                                                         estacionamientos=int(nrEstacionamientos))
                            text = "El precio tasado es UF " + str(precio)+", con un nivel de confianza: "+str(nivel)+\
                                   ", tasación realizada comparandose con "+str(nrcomp)+" propiedades."
                        else:
                            text = "Error de ingreso de datos."

                #tasador con links
                elif arr[0] == comandosMultiples[2]:
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

                            precio,nivel,nrcomp,links = tb.calcularTasacion(operacion=operacion,tipo=tipo,lat=float(lat),lon=float(lon),util=float(mtUtiles),
                                                         total=float(mtTotales),dormitorios=int(dormitorios),banos=int(banos),
                                                         estacionamientos=int(nrEstacionamientos))
                            text = "El precio tasado es UF " + str(precio)+", con un nivel de confianza: "+str(nivel)+\
                                   ", tasación realizada comparandose con "+str(nrcomp)+" propiedades.\nLinks:"
                            for link in links:
                                text += "\n\n" + str(link)
                        else:
                            text = "Error de ingreso de datos."

                #Banear corredores
                elif arr[0] == comandosMultiples[3]:
                    if len(arr)!=2:
                        text="Para usar baneador, ingrese 'banear mail'"
                    else:
                        insertarBanned(arr[1])
                        text=str(arr[1])+" agregado a la lista de Baneados."
                else:
                    text = "Comando desconocido. Los comandos dispobibles son:"
                    for c in comandosIndividuales:
                        text+="\n" + c
            else:
                text = "Comando desconocido. Los comandos dispobibles son:"
                for c in comandosIndividuales:
                    text+="\n" + c

            chat = update["message"]["chat"]["id"]
            send_message(text, chat,URL)
        except Exception as e:
            print(e)


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
    print("send to:" + str(chat_id) + " -> " + str(text))


def main():
    currentMinute= dt.datetime.now().minute
    currentPropsPortal = pm.selectorPortal()
    currentPropsGP = pm.selectorGP()
    hasChecked = False
    last_update_id = None
    avisado = False
    print("Bot andando.")

    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        if dt.datetime.now().minute != currentMinute:
            currentMinute = dt.datetime.now().minute
            lastScrap = pm.getLastScrap()
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
