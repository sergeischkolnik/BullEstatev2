from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler
from telegram.ext import ConversationHandler, CallbackQueryHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import logging
import botPropertyMain as pm
import botPropertySelect as select
import botPropertyDataBase as db
import botPropertyConnector as connector



clientsDict = dict()

### FUNCIONES GLOBALES


def start(bot, update):



    global STATE

    print(bot)
    print('...')
    print(update)
    print('...')
    print(update['message']['chat']['id'])
    """
    Start function. Displayed whenever the /start command is called.
    This function sets the language of the bot.
    """

    user = update.message.from_user

    if user.id not in clientsDict:
        client = {}
        clientsDict[user.id] = client


    if db.registered(update.message.from_user.id):
        print("usuario ya registrado")
        select.signedup(bot,update,user.id)
        return pm.SIGNEDUP
    else:
        print("usuario no registrado")
        select.first(bot, update)
        return pm.FIRST


def signedup(bot,update):

    global STATE
    client = clientsDict[update.message.from_user.id]

    data=db.registered_data(update.message.from_user.id)

    if update.message.text == "Si":
        client["id"] = update.message.from_user.id
        client["mail"] = data[1]
        client["pass"] = data[2]
        client["firstname"] = data[3]
        client["lastname"] = data[4]
        select.menu(bot, update)
        return pm.MENU
    elif update.message.text == "No":
        client.clear()
        print(client)
        select.first(bot, update)
        return pm.FIRST
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton (Si/No).")
        select.signedup(bot, update,update.message.from_user.id)
        return pm.MENU

def first(bot,update):

    global STATE

    client = clientsDict[update.message.from_user.id]

    if update.message.text == "Iniciar Sesión":
        select.login(bot, update,client)
        return pm.LOGIN
    elif update.message.text == "Registrarse":
        select.signup(bot, update,client)
        return pm.SIGNUP
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton (Iniciar Sesión/Registrarse.")
        select.first(bot, update)
        return pm.FIRST


def signup(bot,update):

        # Set state:

    global STATE
    client = clientsDict[update.message.from_user.id]

    client["id"] = update.message.chat_id
    if "mail" not in client and '@' in update.message.text and '.' in update.message.text:
        if db.isregistered(update.message.text):
            bot.send_message(chat_id=update.message.chat_id, text="Correo ya registrado, favor ingresar su contraseña")
            client["mail"]=update.message.text
            select.login(bot,update,client)
            return pm.LOGIN
        else:
            client["mail"]=update.message.text
            select.signup(bot, update,client)
            return pm.SIGNUP
    elif "mail" not in client and ('@' not in update.message.text or '.' not in update.message.text):
        bot.send_message(chat_id=update.message.chat_id, text="Correo incorrecto. Favor ingresar correo valido")
        select.signup(bot, update, client)
        return pm.SIGNUP
    elif "pass" not in client:
        client["pass"] = update.message.text
        select.signup(bot, update,client)
        return pm.SIGNUP
    elif "firstname" not in client:
        client["firstname"] = update.message.text
        select.signup(bot, update,client)
        return pm.SIGNUP
    else:
        client["lastname"] = update.message.text
        bot.send_message(chat_id=update.message.chat_id, text="Registrando como cliente")
        db.registerclient(client)
        bot.send_message(chat_id=update.message.chat_id, text="Felicidades "+client["firstname"]+", Te has registrado exitosamente")
        select.menu(bot, update)
        return pm.MENU


def login(bot,update):
    # Set state:
    global STATE
    client = clientsDict[update.message.from_user.id]
    print("Cliente inicial:")
    print(client)
    client["id"] = update.message.chat_id
    if "countfail" not in client:
        client["countfail"]=4
    if "mail" not in client and '@' in update.message.text and '.' in update.message.text:
        if db.isregistered(update.message.text):
            client["mail"]=update.message.text
            select.login(bot, update,client)
            return pm.LOGIN
        else:
            bot.send_message(chat_id=update.message.chat_id, text="El correo indicado no esta registrado. Favor Registrarse, o iniciar sesión con correo registrado.")
            select.first(bot, update)
            return pm.FIRST

    elif "mail" not in client and ('@' not in update.message.text or '.' not in update.message.text):
        bot.send_message(chat_id=update.message.chat_id, text="Correo incorrecto. Favor ingresar correo valido")
        select.login(bot, update, client)
        return pm.LOGIN
    else:
        if db.passvalidation(client["mail"],update.message.text):
            bot.send_message(chat_id=update.message.chat_id, text="Clave Correcta. Bienvenido")
            select.menu(bot, update)
            return pm.MENU
        else:
            if client["countfails"]>=0:
                client["countfails"]=client["countfails"]-1
                bot.send_message(chat_id=update.message.chat_id, text="Clave Inorrecta. Re-intente por favor")
                bot.send_message(chat_id=update.message.chat_id, text="Le quedan "+str(client["countfails"])+" intentos")
                select.login(bot, update,client)
                return pm.LOGIN
            else:
                bot.send_message(chat_id=update.message.chat_id, text="Se Han Agotado los intentos")
                select.first(bot,update)
                return pm.FIRST




def menu(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE

    #set client
    client = clientsDict[update.message.from_user.id]

    client["product"] = update.message.text
    print(client)

    if update.message.text == "Reporte":
        select.operacion(bot, update)
        return pm.SELECT_OP
    elif update.message.text == "Ficha":
        select.site(bot, update)
        return pm.SELECT_SITE
    elif update.message.text == "Ayuda":
        select.menu(bot, update)
        return pm.MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        client.pop("product")
        select.menu(bot, update)
        return pm.MENU


###FUNCIONES REPORTES


def operacion(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE

    # set client
    client = clientsDict[update.message.from_user.id]
    client["operacion"] = update.message.text
    print(client)

    if update.message.text == "Comprar":
        select.region(bot,update)
        return pm.SELECT_REGION
    elif update.message.text == "Arrendar":
        select.region(bot, update)
        return pm.SELECT_REGION
    elif update.message.text == "Atrás":
        select.menu(bot, update)
        return pm.MENU
    elif update.message.text == "Salir":
        select.menu(bot, update)
        return pm.MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        select.operacion(bot, update)
        return pm.SELECT_OP


def region(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE

    # set client
    client = clientsDict[update.message.from_user.id]
    client["region"] = update.message.text
    print(client)

    if update.message.text == "Metropolitana":
        select.comuna(bot,update,client["region"])
        return pm.SELECT_COMUNA
    elif update.message.text == "Valparaíso":
        select.comuna(bot, update,client["region"])
        return pm.SELECT_COMUNA
    elif update.message.text == "Atrás":
        select.operacion(bot, update)
        return pm.SELECT_OP
    elif update.message.text == "Salir":
        select.menu(bot, update)
        return pm.MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        select.region(bot, update)
        return pm.SELECT_REGION


def comuna(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE

    # set client
    client = clientsDict[update.message.from_user.id]
    client["comuna"] = update.message.text
    print(client)

    #Agregar validacion viendo si es parte de una lista
    if update.message.text == "Atrás":
        select.region(bot, update)
        return pm.SELECT_REGION
    elif update.message.text == "Salir":
        select.menu(bot, update)
        return pm.MENU
    else:
        select.tipo(bot, update)
        return pm.SELECT_TIPO


def tipo(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE

    # set client
    client = clientsDict[update.message.from_user.id]
    client["tipo"] = update.message.text
    print(client)

    if update.message.text == "Departamento":
        select.dorms(bot,update)
        return pm.SELECT_DORMS
    elif update.message.text == "Casa":
        select.dorms(bot, update)
        return pm.SELECT_DORMS
    elif update.message.text == "Atrás":
        select.comuna(bot, update,client["region"])
        return pm.SELECT_COMUNA
    elif update.message.text == "Salir":
        select.menu(bot, update)
        return pm.MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        select.tipo(bot, update)
        return pm.SELECT_TIPO


def dorms(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE

    # set client
    client = clientsDict[update.message.from_user.id]
    client["dormitorios"] = update.message.text
    print(client)

    if update.message.text == "1" or update.message.text == "2" or update.message.text == "3" or update.message.text == "4+":
        select.baths(bot,update)
        return pm.SELECT_BATHS
    elif update.message.text == "Atrás":
        select.tipo(bot, update)
        return pm.SELECT_TIPO
    elif update.message.text == "Salir":
        select.menu(bot, update)
        return pm.MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        select.dorms(bot, update)
        return pm.SELECT_DORMS


def baths(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE

    # set client
    client = clientsDict[update.message.from_user.id]
    client["baños"] = update.message.text
    print(client)

    if update.message.text == "1" or update.message.text == "2" or update.message.text == "3" or update.message.text == "4+":
        select.price_range(bot,update,"moneda")
        return pm.SELECT_PRICE_RANGE
    elif update.message.text == "Atrás":
        select.dorms(bot, update)
        return pm.SELECT_DORMS
    elif update.message.text == "Salir":
        select.menu(bot, update)
        return pm.MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        select.baths(bot, update)
        return pm.SELECT_BATHS


def price_range(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE

    # set client
    client = clientsDict[update.message.from_user.id]
    if "moneda" not in client:
        client["moneda"] = update.message.text
        if update.message.text == "UF":
            select.price_range(bot, update, "preciomin")
            return pm.SELECT_PRICE_RANGE
        elif update.message.text == "Pesos":
            select.price_range(bot, update, "preciomin")
            return pm.SELECT_PRICE_RANGE
        elif update.message.text == "Atrás":
            select.tipo(bot, update)
            return pm.SELECT_TIPO
        elif update.message.text == "Salir":
            select.menu(bot, update)
            return pm.MENU

    elif "preciomin" not in client:
        try:
            client["preciomin"]=int(update.message.text)
            select.price_range(bot, update, "preciomax")
            print(client)
            return pm.SELECT_PRICE_RANGE
        except:
            bot.send_message(chat_id=update.message.chat_id, text="Favor ingresar número entero")
            select.price_range(bot, update, "preciomin")
            return pm.SELECT_PRICE_RANGE

    else:
        try:
            client["preciomax"] = int(update.message.text)
            select.area_range(bot, update, "metrosmin",client["tipo"])
            print(client)
            return pm.SELECT_AREA_RANGE
        except:
            bot.send_message(chat_id=update.message.chat_id, text="Favor ingresar número entero")
            select.price_range(bot, update, "preciomax")
            return pm.SELECT_PRICE_RANGE


def area_range(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE

    # set client
    client = clientsDict[update.message.from_user.id]
    if "metrosmin" not in client:
        try:
            client["metrosmin"] = int(update.message.text)
            select.area_range(bot, update, "metrosmax",client["tipo"])
            print(client)
            return pm.SELECT_AREA_RANGE
        except:
            bot.send_message(chat_id=update.message.chat_id, text="Favor ingresar número entero")
            select.area_range(bot, update, "metrosmin",client["tipo"])
            return pm.SELECT_AREA_RANGE

    elif "metrosmax" not in client:
        try:
            client["metrosmax"] = int(update.message.text)
            if client["tipo"]=="Departamento" or client["tipo"]=="Casa":
                select.area_range(bot, update, "totalmin", client["tipo"])
                return pm.SELECT_AREA_RANGE
            else:
                select.confirm_report(bot, update, client)
                print(client)
                return pm.CONFIRM_REPORT
        except:
            bot.send_message(chat_id=update.message.chat_id, text="Favor ingresar número entero")
            select.area_range(bot, update, "metrosmax",client["tipo"])
            return pm.SELECT_AREA_RANGE

    elif "totalmin" not in client:
        try:
            client["totalmin"] = int(update.message.text)
            select.area_range(bot, update, "totalmax",client["tipo"])
            print(client)
            return pm.SELECT_AREA_RANGE
        except:
            bot.send_message(chat_id=update.message.chat_id, text="Favor ingresar número entero")
            select.area_range(bot, update, "totalmin",client["tipo"])
            return pm.SELECT_AREA_RANGE

    else:
        try:
            client["totalmax"] = int(update.message.text)

            select.confirm_report(bot, update, client)
            print(client)
            return pm.CONFIRM_REPORT
        except:
            bot.send_message(chat_id=update.message.chat_id, text="Favor ingresar número entero")
            select.area_range(bot, update, "metrosmax",client["tipo"])
            return pm.SELECT_AREA_RANGE


def confirm_report(bot,update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE

    # set client
    client = clientsDict[update.message.from_user.id]

    if update.message.text == "SI":
        #generar reporte para cliente, enviar al correo correspondiente
        bot.send_message(chat_id=update.message.chat_id, text="Reporte generado y enviado exitosamente al correo: "+(client["mail"])+".")
        select.menu(bot, update)
        return pm.MENU
    elif update.message.text == "Modificar":
        bot.send_message(chat_id=update.message.chat_id, text="Lo sentimos, por ahora no se puede modificar. Si lo deseas, presiona 'Salir' para volver a generar un reporte, o volver atrás")
        select.confirm_report(bot, update, client)
        return pm.CONFIRM_REPORT

    elif update.message.text == "Atrás":
        client.pop("metrosmin")
        client.pop("metrosmax")
        client.pop("moneda")
        client.pop("preciomin")
        client.pop("preciomax")
        if "totalmin" in client:
            client.pop("totalmin")
        if "totalmax" in client:
            client.pop("totalmax")

        select.price_range(bot, update, "moneda")
        return pm.SELECT_PRICE_RANGE
    elif update.message.text == "Salir":
        select.menu(bot, update)
        return pm.MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        select.confirm_report(bot, update, client)
        return pm.CONFIRM_REPORT


### FUNCIONES FICHA


def site(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE

    # set client
    client = clientsDict[update.message.from_user.id]
    client["sitio"] = update.message.text
    print(client)

    user = update.message.from_user
    if update.message.text == "www.portalinmobiliario.com":
        select.id_prop(bot,update)
        return pm.SELECT_ID
    if update.message.text == "www.yapo.cl":
        select.id_prop(bot, update)
        return pm.SELECT_ID
    elif update.message.text == "Atrás":
        select.menu(bot, update)
        return pm.MENU
    elif update.message.text == "Salir":
        select.menu(bot, update)
        return pm.MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        select.site(bot, update)
        return pm.SELECT_SITE


def id_prop(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    print("entro a set idprop")

    client = clientsDict[update.message.from_user.id]

    try:
        client["id_prop"] = int(update.message.text)
        print("paso test de int")
        print(client)
        select.confirm_file(bot, update,client)
        print("paso test de select confirm")
        print(client)
        return pm.CONFIRM_FILE
    except:
        bot.send_message(chat_id=update.message.chat_id, text="Favor ingresar número entero")
        select.id_prop(bot, update)
        return pm.SELECT_ID


def confirm_file(bot, update):


    global STATE

    # set client
    client = clientsDict[update.message.from_user.id]

    if update.message.text == "SI":

        bot.send_message(chat_id=update.message.chat_id, text="Generando Ficha")
        text=connector.connectorFicha(client)
        bot.send_message(chat_id=update.message.chat_id, text=text)
        select.menu(bot, update)
        return pm.MENU
    elif update.message.text == "Modificar":
        bot.send_message(chat_id=update.message.chat_id, text="Lo sentimos, por ahora no se puede modificar. Si lo deseas, presiona 'Salir' para volver a generar un reporte, o volver atrás")
        select.confirm_report(bot, update, client)
        return pm.CONFIRM_REPORT

    elif update.message.text == "Atrás":

        select.id_prop(bot, update)
        return pm.SELECT_ID
    elif update.message.text == "Salir":
        select.menu(bot, update)
        return pm.MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        select.confirm_file(bot, update, client)
        return pm.CONFIRM_FILE
