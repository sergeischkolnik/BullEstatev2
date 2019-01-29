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

comandosIndividuales = ['hola','portal','goplaceit','reporte','tasador']
comandosMultiples = ['reporte','tasador']
id_chats_updates = ["485728961","652659504"]

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
                        operacion = arr[3]
                        tipo = arr[4]
                        estado = arr[5]
                        dormitorios = arr[6]
                        banos = arr[7]
                        mtUtiles = arr[8]
                        mtTotales = arr[9]
                        nrEstacionamientos = arr[10]
                        ano = arr[11]
                        piso = arr[12]
                        orientacion = arr[13]

                        calle = ""
                        for c in range(14,len(arr)-1):
                            calle += c
                            calle += " "

                        nrCalle = arr[len(arr)-1]
                        direccion = str(calle) + str(nrCalle) + ", " + str(comuna) + ", Chile"
                        lat,lon = gm.getCoordsWithAdress(direccion)

                        precio = tb.calcularTasacion(operacion=operacion,tipo=tipo,lat=float(lat),lon=float(lon),util=float(mtUtiles),
                                                     total=float(mtTotales),dormitorios=int(dormitorios),banos=int(banos),
                                                     estacionamientos=int(nrEstacionamientos))
                        text = "El precio tasado es UF " + str(precio)

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
