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
import ficha
import types
import telebot as tb
from telebot import types



TOKEN = "864014186:AAGrFbg92jxFplBVlYSXh9brToc2aal3RMg"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)



# TODOS LOS COMANDOS SIEMPRE SOLO MINUSCULAS
comandosIndividuales = ['hola',
                        'ficha']

comandosMultiples = ['hola',
                    'ficha']

id_chats_updates = ["485728961", "652659504", "9561926"]




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
        url += "&offset={}".format(offset)
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

            chat = update["message"]["chat"]["id"]

            markup = types.ReplyKeyboardMarkup()
            markup.row('a', 'v')
            markup.row('c', 'd', 'e')
            tb.send_message(chat,"teclado", None, None, markup)

            if len(arr) == 1:
                print("ejecutando comando simple")
                # comandos simples
                text = arr[0]

                # Hola y bienvenida
                if text == comandosIndividuales[0]:
                    text = "Hola! Los comandos son:"
                    for c in comandosIndividuales:
                        text += "\n" + c


                # ficha
                elif text == comandosIndividuales[1]:
                    text = "Para usar la emisión de ficha, escriba, separando por espacios:\nficha " \
                           "<fuente (portalinmobiliario o yapo)> <id de la Propiedad> <correo de envío> "

                # no encontrado
                else:
                    text = "Comando desconocido. Los comandos dispobibles son:"
                    for c in comandosIndividuales:
                        text += "\n" + c

            elif len(arr) > 1:
                # comandos multiples


                # Ficha

                if arr[0] == comandosMultiples[1]:
                    if (len(arr)!=4):
                        text = "Para usar la emisión de ficha, escriba, separando por espacios:\nficha " \
                           "<fuente (portalinmobiliario o yapo)> <id de la Propiedad> <correo de envío> "
                    else:
                        print("ejecutando creacion de ficha")
                        sitio=str(arr[1])
                        id=int(arr[2])
                        mail=str(arr[3])
                        text=ficha.crearFicha(sitio,id,mail)

                else:
                    text = "Comando desconocido. Los comandos dispobibles son:"
                    for c in comandosIndividuales:
                        text += "\n" + c
            else:
                text = "Comando desconocido. Los comandos dispobibles son:"
                for c in comandosIndividuales:
                    text += "\n" + c

            send_message(text, chat, URL)
        except Exception as e:
            print("[tgBotPropertyAdmin]" + str(e))


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id, urlP):
    text = urllib.parse.quote_plus(text)
    url = urlP + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)
    print("[tgBot] send to:" + str(chat_id) + " -> " + str(text))


def main():
    currentMinute = dt.datetime.now().minute
    last_update_id = None
    avisado = False
    activo=True
    print("[tgBotPropertyAdmin] Bot andando.")
    while True:

        updates = get_updates(last_update_id)
        result = updates.get("result")
        if result:
            if len(result) > 0:
                last_update_id = get_last_update_id(updates) + 1
                echo_all(updates)

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
