from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler
from telegram.ext import ConversationHandler, CallbackQueryHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import logging
import botPropertyMain as pm
import botPropertySelect as select
import botPropertyDataBase as db
import botPropertyConnector as connector
import googleMapApi as gm
import threading


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
    global lastoperations
    lastoperations={}
    lastoperations["Reporte"]=[]
    lastoperations["Tasador"]=[]
    lastoperations["Ficha"]=[]
    lastoperations["CRM"]=[]


    if update.message.text == "Si":
        data = db.registered_data(update.message.from_user.id)
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
        return pm.SIGNEDUP

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
        client["countfail"]=3
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
            data = db.registered_data(update.message.from_user.id)
            client["id"] = update.message.from_user.id
            client["mail"] = data[1]
            client["pass"] = data[2]
            client["firstname"] = data[3]
            client["lastname"] = data[4]
            select.menu(bot, update)
            return pm.MENU
        else:
            if client["countfail"]>0:

                bot.send_message(chat_id=update.message.chat_id, text="Clave Inorrecta. Re-intente por favor")
                bot.send_message(chat_id=update.message.chat_id, text="Le quedan "+str(client["countfail"])+" intentos")
                client["countfail"] = client["countfail"] - 1
                select.login(bot, update,client)
                return pm.LOGIN
            else:
                bot.send_message(chat_id=update.message.chat_id, text="Se Han Agotado los intentos")
                client.clear()
                select.first(bot,update)
                return pm.FIRST

def menu(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE

    #Reset client
    client = clientsDict[update.message.from_user.id]
    auxid=client["id"]
    auxmail=client["mail"]
    auxfirstname=client["firstname"]
    auxlastname=client["lastname"]
    if "product" in client and client["product"]!="Historial" and 'success' in client:
        client.pop("success")
        lastproduct=client["product"]
        auxclient=client.copy()

        #Save last operations
        lastoperations[lastproduct].insert(0,auxclient)
        if len(lastoperations[lastproduct])>5:
            lastoperations[lastproduct]=lastoperations[lastproduct][0:4]
        print(str(lastproduct)+" realizados: "+str(len(lastoperations[lastproduct])))


    hadThr = False
    if "reporteThread" in client.keys():
        thr = client["reporteThread"]
        hadThr = True

    client.clear()
    client["id"]=auxid
    client["mail"]=auxmail
    client["firstname"]=auxfirstname
    client["lastname"]=auxlastname
    client["product"] = update.message.text

    if hadThr:
        client["reporteThread"] = thr

    print(client)

    if client["id"]==940873510:
        bot.send_message(chat_id=update.message.chat_id, text="Bot en Mantención")
        select.menu(bot,update)
        return pm.MENU

    if update.message.text == "Reporte":
        if "reporteThread" in client.keys() and client["reporteThread"].isAlive():
            bot.send_message(chat_id=update.message.chat_id, text="Ya se está generando un reporte. Por favor espere que"
                                                                  " éste termine antes de comenzar otro. Si ha pasado "
                                                                  "sobre una hora y el problema persiste, por favor "
                                                                  "contacte a soporte.")
            select.menu(bot, update)
            return pm.MENU
        else:
            select.operacion(bot, update,client)
            return pm.SELECT_OP
    elif update.message.text == "Tasador":
        select.operacion(bot, update,client)
        return pm.SELECT_OP
    elif update.message.text == "Ficha":
        select.id_prop(bot, update)
        return pm.SELECT_ID
    elif update.message.text == "Historial":
        select.last(bot, update)
        return pm.SELECT_LAST
    elif update.message.text == "ASDF" or update.message.text == "Props. Cerca" or update.message.text == "CRM":
        select.crm(bot, update)
        return pm.CRM
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        client.pop("product")
        select.menu(bot, update)
        return pm.MENU

def last(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE

    # set client
    client = clientsDict[update.message.from_user.id]
    client["historial"]=True
    print(client)

    hadThr = False
    if "reporteThread" in client.keys():
        thr = client["reporteThread"]
        hadThr = True

    if hadThr:
        client["reporteThread"] = thr

    print(client)

    if update.message.text == "Reporte" and len(lastoperations[update.message.text])>0:
        if "reporteThread" in client.keys() and client["reporteThread"].isAlive():
            bot.send_message(chat_id=update.message.chat_id, text="Ya se está generando un reporte. Por favor espere que"
                                                                  " éste termine antes de comenzar otro. Si ha pasado "
                                                                  "sobre una hora y el problema persiste, por favor "
                                                                  "contacte a soporte.")
            select.menu(bot, update)
            return pm.MENU
        else:
            client["last"] = update.message.text
            client=lastoperations[update.message.text][0]

            select.confirm_report(bot, update,client)
            return pm.CONFIRM_REPORT
    elif update.message.text == "Tasador" and len(lastoperations[update.message.text])>0:
        client=lastoperations[update.message.text][0]
        select.confirm_tasacion(bot, update,client)
        return pm.CONFIRM_TASACION
    elif update.message.text == "Ficha" and len(lastoperations[update.message.text])>0:
        client=lastoperations[update.message.text][0]
        select.confirm_file(bot, update,client,False,False)
        return pm.CONFIRM_FILE
    elif update.message.text == "Atrás":
        select.menu(bot, update)
        return pm.MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="No posee historial en "+str(update.message.text)+", o bien es un comando invalido. Presione algun boton.")
        client.pop("product")
        select.menu(bot, update)
        return pm.MENU

def callback(bot,update):
    client = clientsDict[update.message.from_user.id]
    print("entro al set.callback...")
    client.pop("modify")
    print(client)

    if client["product"]=="Reporte":
        select.confirm_report(bot,update,client)
        return pm.CONFIRM_REPORT
    elif client["product"]=="Tasador":
        select.confirm_tasacion(bot,update,client)
        return pm.CONFIRM_TASACION
    elif client["product"]=="CRM" and client["crm"]=="Buscar":
        select.confirm_report(bot,update,client)
        return pm.CONFIRM_REPORT
    elif client["product"]=="CRM" and client["crm"]=="Nueva":
        select.confirm_tasacion(bot,update,client)
        return pm.CONFIRM_TASACION
    elif client["product"]=="CRM" and client["crm"]=="Lista Completa":
        select.crm_feature(bot,update,client)
        return pm.CRM_FEATURE
    else:
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
    if client["product"]=="CRM" and client["crm"]=="Buscar":
        client["operacion"] = update.message.text
    elif client["product"]=="Reporte":
        client["operacion"] = update.message.text
    else:
        client["tipotasacion"] = update.message.text
    print(client)

    if update.message.text == "Comprar":
        if "modify" in client:
            return callback(bot,update)
        else:
            select.region(bot,update,client)
            return pm.SELECT_REGION
    elif update.message.text == "Arrendar":
        if "modify" in client:
            return callback(bot,update)
        else:
            select.region(bot,update,client)
            return pm.SELECT_REGION
    elif update.message.text == "Simple":
        if "modify" in client:
            callback(bot,update)
        else:
            select.region(bot,update,client)
            return pm.SELECT_REGION
    elif update.message.text == "Full":
        if "modify" in client:
            callback(bot,update)
        else:
            select.region(bot,update,client)
            return pm.SELECT_REGION
    elif update.message.text == "Venta":
        if "modify" in client:
            callback(bot,update)
        else:
            select.region(bot,update,client)
            return pm.SELECT_REGION
    elif update.message.text == "Arriendo":
        if "modify" in client:
            callback(bot,update)
        else:
            select.region(bot,update,client)
            return pm.SELECT_REGION
    elif update.message.text == "Atrás":
        if client["product"]=="CRM":
            client.pop("tipotasacion")
            select.crm(bot, update)
            return pm.CRM
        elif client["product"] == "Reporte":
            client.pop("operacion")
        else:
            client.pop("tipotasacion")
        select.menu(bot, update)
        return pm.MENU
    elif update.message.text == "Salir":
        select.menu(bot, update)
        return pm.MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        select.operacion(bot, update,client)
        return pm.SELECT_OP

def region(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    # set client
    client = clientsDict[update.message.from_user.id]
    client["region"] = update.message.text
    print(client)

    if update.message.text == "Metropolitana":
        if "modify" in client:
            return callback(bot,update)
        else:
            select.comuna(bot,update,client)
            return pm.SELECT_COMUNA
    elif update.message.text == "Valparaiso":
        if "modify" in client:
            return callback(bot,update)
        else:
            select.comuna(bot, update,client)
            return pm.SELECT_COMUNA
    elif update.message.text == "Biobio":
        if "modify" in client:
            return callback(bot,update)
        else:
            select.comuna(bot, update,client)
            return pm.SELECT_COMUNA
    elif update.message.text == "Coquimbo":
        if "modify" in client:
            return callback(bot,update)
        else:
            select.comuna(bot, update,client)
            return pm.SELECT_COMUNA
    elif update.message.text == "Antofagasta":
        if "modify" in client:
            return callback(bot,update)
        else:
            select.comuna(bot, update,client)
            return pm.SELECT_COMUNA
    elif str(update.message.text).lower() in ["arica","iquique","atacama","ohiggins","maule","ñuble","araucanía","los ríos","los lagos","aysen","magallanes"]:
        if "modify" in client:
            return callback(bot,update)
        else:
            select.comuna(bot, update,client)
            return pm.SELECT_COMUNA
    elif update.message.text == "Otra":
        select.region(bot, update,client)
        return pm.SELECT_REGION
    elif update.message.text == "Atrás":
        client.pop("region")
        select.operacion(bot,update,client)
        return pm.SELECT_OP
    elif update.message.text == "Salir":
        select.menu(bot, update)
        return pm.MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        select.region(bot,update,client)
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
        client.pop("region")
        client.pop("comuna")
        select.region(bot, update,client)
        return pm.SELECT_REGION
    if update.message.text == "Otra":
        select.comuna(bot, update,client)
        return pm.SELECT_COMUNA
    elif update.message.text == "Salir":
        select.menu(bot, update)
        return pm.MENU
    else:
        if "modify" in client:
            return callback(bot,update)
        else:
            select.tipo(bot, update,client)
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
    if client["product"]=="CRM" and client["crm"]=="Lista Completa":
        if "modify" in client:
            return callback(bot,update)
        else:
            select.crm_feature(bot,update,client)
            return pm.CRM_FEATURE
    elif update.message.text == "Departamento":
        if "modify" in client:
            return callback(bot,update)
        else:
            select.dorms(bot,update,client)
            return pm.SELECT_DORMS
    elif update.message.text == "Casa":
        if "modify" in client:
            return callback(bot,update)
        else:
            select.dorms(bot, update,client)
            return pm.SELECT_DORMS
    elif update.message.text == "Oficina":
        if "modify" in client:
            return callback(bot,update)
        else:
            select.dorms(bot, update,client)
            return pm.SELECT_DORMS
    elif update.message.text == "Comercial":
        if "modify" in client:
            return callback(bot,update)
        else:
            select.baths(bot, update,client)
            return pm.SELECT_BATHS

    elif update.message.text == "Atrás":
        client.pop("tipo")
        client.pop("comuna")
        client.pop("region")
        select.region(bot, update,client)
        return pm.SELECT_REGION
    elif update.message.text == "Salir":
        select.menu(bot, update)
        return pm.MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        select.tipo(bot, update,client)
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
    admited=["1","2","3","4","4+","5","6","7","8","9","10",]
    if update.message.text in admited:
        if "modify" in client:
            return callback(bot,update)
        else:
            select.baths(bot,update,client)
            return pm.SELECT_BATHS
    elif update.message.text == "Atrás":
        client.pop("dormitorios")
        select.tipo(bot, update,client)
        return pm.SELECT_TIPO
    elif update.message.text == "Salir":
        select.menu(bot, update)
        return pm.MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        select.dorms(bot, update,client)
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
    admited=["1","2","3","4","4+","5","6","7","8","9","10",]

    if update.message.text in admited:


        if client["product"]=="Reporte":
            if "modify" in client:
                return callback(bot,update)
            else:
                select.price_range(bot,update,client)
                return pm.SELECT_PRICE_RANGE
        elif client["product"]=="CRM" and client["crm"]=="Buscar":
            if "modify" in client:
                return callback(bot,update)
            else:
                select.price_range(bot,update,client)
                return pm.SELECT_PRICE_RANGE
        else:
            if client["tipo"]=="Comercial":
                if "modify" in client:
                    return callback(bot,update)
                else:
                    select.area(bot,update,client)
                    return pm.SELECT_AREA

            else:
                if "modify" in client:
                    return callback(bot,update)
                else:
                    select.feature(bot,update,client)
                    return pm.SELECT_FEATURE
    elif update.message.text == "Atrás":
        client.pop("baños")
        select.dorms(bot, update,client)
        return pm.SELECT_DORMS
    elif update.message.text == "Salir":
        select.menu(bot, update)
        return pm.MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        select.baths(bot, update,client)
        return pm.SELECT_BATHS

def price_range(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE
    # set client
    client = clientsDict[update.message.from_user.id]

    if update.message.text == "Atrás":
        if "preciomax" in client:
            client.pop("preciomax")
            select.price_range(bot,update,client)
            return pm.SELECT_PRICE_RANGE
        elif "preciomin" in client:
            client.pop("preciomin")
            select.price_range(bot,update,client)
            return pm.SELECT_PRICE_RANGE
        elif "moneda" in client:
            client.pop("moneda")
            select.price_range(bot,update,client)
            return pm.SELECT_PRICE_RANGE
        else:
            select.baths(bot, update,client)
            return pm.SELECT_BATHS
    elif update.message.text == "Salir":
            select.menu(bot, update)
            return pm.MENU
    elif update.message.text == "Otro":
        if "preciomin" not in client or client["preciomin"]=="Otro":
            client["preciomin"] = update.message.text
        else:
            client["preciomax"] = update.message.text
        select.price_range(bot, update,client)
        return pm.SELECT_PRICE_RANGE

    elif update.message.text == "Default":

        client["preciomin"] = None
        client["preciomax"] = None

        if "modify" in client:
            return callback(bot,update)
        else:
            select.area_range(bot, update, client)
            print(client)
            return pm.SELECT_AREA_RANGE

    elif "moneda" not in client:
        client["moneda"] = update.message.text
        if update.message.text == "UF":
            select.price_range(bot, update,client)
            return pm.SELECT_PRICE_RANGE
        elif update.message.text == "Pesos":
            select.price_range(bot, update,client)
            return pm.SELECT_PRICE_RANGE



    elif "preciomin" not in client or client["preciomin"]=="Otro":
        try:
            client["preciomin"]=int(update.message.text.replace('.',''))
            if client["product"]=="CRM" and client["crm"]=="Nueva":
                if "modify" in client:
                    return callback(bot,update)
                else:
                    select.crm_feature(bot, update,client)
                    print(client)
                    return pm.CRM_FEATURE
            else:
                select.price_range(bot, update,client)
                print(client)
                return pm.SELECT_PRICE_RANGE
        except:
            bot.send_message(chat_id=update.message.chat_id, text="Favor ingresar número entero")
            select.price_range(bot, update, client)
            return pm.SELECT_PRICE_RANGE

    else:
        try:
            client["preciomax"] = int(update.message.text.replace('.',''))
            select.area_range(bot, update, client)
            if "modify" in client:
                return callback(bot,update)
            else:
                print(client)
                return pm.SELECT_AREA_RANGE
        except:
            bot.send_message(chat_id=update.message.chat_id, text="Favor ingresar número entero")
            select.price_range(bot, update, client)
            return pm.SELECT_PRICE_RANGE

def area_range(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE

    # set client
    client = clientsDict[update.message.from_user.id]

    if update.message.text == "Atrás":
            if "totalmax" in client:
                client.pop("totalmax")
                select.area_range(bot,update,client)
                return pm.SELECT_AREA_RANGE
            elif "totalmin" in client:
                client.pop("totalmin")
                select.area_range(bot,update,client)
                return pm.SELECT_AREA_RANGE
            elif "metrosmax" in client:
                client.pop("metrosmax")
                select.area_range(bot,update,client)
                return pm.SELECT_AREA_RANGE
            elif "metrosmin" in client:
                client.pop("metrosmin")
                select.area_range(bot,update,client)
                return pm.SELECT_AREA_RANGE
            else:
                client.pop("preciomax")
                select.price_range(bot, update,client)
                return pm.SELECT_PRICE_RANGE

    elif update.message.text == "Salir":
            select.menu(bot, update)
            return pm.MENU

    elif update.message.text == "Otra":
        if "metrosmin" not in client or client["metrosmin"]=="Otra":
            client["metrosmin"]=update.message.text
        elif "metrosmax" not in client or client["metrosmax"]=="Otra":
            client["metrosmax"]=update.message.text
        elif "totalmin" not in client or client["totalmin"]=="Otra":
            client["totalmin"]=update.message.text
        else:
            client["totalmax"]=update.message.text
        select.area_range(bot, update, client)
        return pm.SELECT_AREA_RANGE

    elif update.message.text == "Default":
        client["metrosmin"]=None
        client["metrosmax"]=None
        client["totalmin"]=None
        client["totalmax"]=None
        client["reportepro"]=False
        client["reporteinterno"] = False
        client["reportemetro"] = False
        select.confirm_report(bot, update, client)
        return pm.CONFIRM_REPORT


    elif "metrosmin" not in client or client["metrosmin"]=="Otra":
        try:
            client["metrosmin"] = int(update.message.text)
            select.area_range(bot, update, client)
            print(client)
            return pm.SELECT_AREA_RANGE
        except:
            bot.send_message(chat_id=update.message.chat_id, text="Favor ingresar número entero")
            select.area_range(bot, update, client)
            return pm.SELECT_AREA_RANGE

    elif "metrosmax" not in client or client["metrosmax"]=="Otra":
        try:
            client["metrosmax"] = int(update.message.text)
            if client["tipo"]=="Departamento" or client["tipo"]=="Casa" or client["tipo"]=="Oficina":
                select.area_range(bot, update, client)
                return pm.SELECT_AREA_RANGE
            else:
                client["reportepro"] = False
                client["reporteinterno"] = False
                client["reportemetro"] = False
                print("tipo de reporte seteado")
                select.confirm_report(bot, update, client)
                print(client)
                return pm.CONFIRM_REPORT
        except Exception as e:
            print(e)
            bot.send_message(chat_id=update.message.chat_id, text="Favor ingresar número entero")
            select.area_range(bot, update, client)
            return pm.SELECT_AREA_RANGE

    elif "totalmin" not in client or client["totalmin"]=="Otra":
        try:
            client["totalmin"] = int(update.message.text)
            select.area_range(bot, update, client)
            print(client)
            return pm.SELECT_AREA_RANGE
        except:
            bot.send_message(chat_id=update.message.chat_id, text="Favor ingresar número entero")
            select.area_range(bot, update,client)
            return pm.SELECT_AREA_RANGE

    else:
        try:
            client["totalmax"] = int(update.message.text)
            client["reportepro"]=False
            client["reporteinterno"] = False
            client["reportemetro"] = False
            select.confirm_report(bot, update, client)
            return pm.CONFIRM_REPORT
        except:
            bot.send_message(chat_id=update.message.chat_id, text="Favor ingresar número entero")
            select.area_range(bot, update, client)
            return pm.SELECT_AREA_RANGE

def confirm_report(bot,update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE

    # set client
    client = clientsDict[update.message.from_user.id]

    if update.message.text == "SI" and client["product"]=="Reporte":

        if "reporteThread" in client.keys() and client["reporteThread"].isAlive():
            bot.send_message(chat_id=update.message.chat_id, text="Ya se está generando un reporte. Por favor espere que"
                                                                  " éste termine antes de comenzar otro. Si ha pasado "
                                                                  "sobre una hora y el problema persiste, por favor "
                                                                  "contacte a soporte.")

        else:
            #generar reporte para cliente, enviar al correo correspondiente

            bot.send_message(chat_id=update.message.chat_id, text="Se está generando el reporte")
            if "historial" in client:
                client = lastoperations["Reporte"][0]
            reply = "Reporte generado y enviado exitosamente al correo: "+(client["mail"])+"."
            client["reporteThread"] = threading.Thread(target=connector.generarreporte, args=(client,bot.send_message,update.message.chat_id,reply))
            client["reporteThread"].setDaemon(True)
            client["reporteThread"].start()
            client["success"]="check"

        #bot.send_message(chat_id=update.message.chat_id, text=reply)

        select.menu(bot, update)
        return pm.MENU
    elif update.message.text == "SI" and client["product"]=="CRM":
        bot.send_message(chat_id=update.message.chat_id, text="Busqueda exitosa. Falta construir conector")
        text=connector.buscar(client)
        bot.send_message(chat_id=update.message.chat_id, text=text)
        select.menu(bot,update)
        return pm.MENU
    elif update.message.text == "Modificar":
        select.modify(bot, update, client)
        return pm.MODIFY
    elif update.message.text == "Avanzado":
        client["DormRange"] = False
        client["BathRange"] = False
        client["Adress"] = False
        client["OtraComuna"] = False
        select.advance(bot, update, client)
        return pm.ADVANCE
    elif update.message.text == "Agregar Tasación":
        client["reportepro"] = True
        select.confirm_report(bot, update, client)
        return pm.CONFIRM_REPORT
    elif update.message.text == "Agregar Contacto Publicación":
        client["reporteinterno"] = True
        select.confirm_report(bot, update, client)
        return pm.CONFIRM_REPORT
    elif update.message.text == "Agregar Distancia al metro":
        client["reportemetro"] = True
        select.confirm_report(bot, update, client)
        return pm.CONFIRM_REPORT
    elif update.message.text == "Quitar Tasación":
        client["reportepro"] = False
        select.confirm_report(bot, update, client)
        return pm.CONFIRM_REPORT
    elif update.message.text == "Quitar Contacto Publicación":
        client["reporteinterno"] = False
        select.confirm_report(bot, update, client)
        return pm.CONFIRM_REPORT
    elif update.message.text == "Quitar Distancia al metro":
        client["reportemetro"] = False
        select.confirm_report(bot, update, client)
        return pm.CONFIRM_REPORT

    elif update.message.text == "Atrás":
        try:
            client.pop("totalmax")
        except:
            pass
        select.area_range(bot, update, client)
        return pm.SELECT_AREA_RANGE
    elif update.message.text == "Salir":
        select.menu(bot, update)
        return pm.MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        select.confirm_report(bot, update, client)
        return pm.CONFIRM_REPORT

def advance(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE

    # set client
    client = clientsDict[update.message.from_user.id]
    print(client)

    if client["DormRange"] is True:
        if "DormMin" not in client:
            try:
                client["DormMin"] = int(update.message.text)
            except:
                bot.send_message(chat_id=update.message.chat_id, text="Favor ingresar número entero")
            select.advance(bot, update, client)
            return pm.ADVANCE

        else:
            try:
                client["DormMax"] = int(update.message.text)
                client["DormRange"] = False
            except:
                bot.send_message(chat_id=update.message.chat_id, text="Favor ingresar número entero")
            select.advance(bot, update, client)
            return pm.ADVANCE

    elif client["BathRange"] is True:
        if "BathMin" not in client:
            try:
                client["BathMin"] = int(update.message.text)
            except:
                bot.send_message(chat_id=update.message.chat_id, text="Favor ingresar número entero")
            select.advance(bot, update, client)
            return pm.ADVANCE

        else:
            try:
                client["BathMax"] = int(update.message.text)
                client["BathRange"] = False
            except:
                bot.send_message(chat_id=update.message.chat_id, text="Favor ingresar número entero")
            select.advance(bot, update, client)
            return pm.ADVANCE

    elif client["Adress"] is True:
        if "Center" not in client:
            client["Center"] = update.message.text
            select.advance(bot, update, client)
            return pm.ADVANCE

        else:
            try:
                client["Radius"] = int(update.message.text)
                client["Adress"] = False
            except:
                bot.send_message(chat_id=update.message.chat_id, text="Favor ingresar número entero")

            select.advance(bot, update, client)
            return pm.ADVANCE

    elif client["OtraComuna"] is True:
        listaComunas=[]
        if type(client["comuna"]) is not list:
            listaComunas.append(client["comuna"])
            listaComunas.append(update.message.text)
            client["comuna"]=listaComunas
        else:
            client["comuna"].append(update.message.text)
        client["OtraComuna"] = False
        select.advance(bot, update, client)
        return pm.ADVANCE

    elif update.message.text =="Rango Dormitorios":
        client["DormRange"] = True
        try:
            client.pop("DormMin")
            client.pop("DormMax")
        except:
            pass
        select.advance(bot,update,client)
        return pm.ADVANCE

    elif update.message.text =="Rango Baños":
        client["BathRange"] = True
        try:
            client.pop("BathMin")
            client.pop("BathMax")
        except:
            pass
        select.advance(bot, update, client)
        return pm.ADVANCE

    elif update.message.text =="Buscar por dirección":
        client["Adress"] = True
        try:
            client.pop("Center")
            client.pop("Radius")
        except:
            pass
        select.advance(bot, update, client)
        return pm.ADVANCE

    elif update.message.text =="Agregar Comuna":
        client["OtraComuna"] = True
        select.advance(bot, update, client)
        return pm.ADVANCE

    elif update.message.text =="Atrás":
        client["DormRange"] = False
        client["BathRange"] = False
        client["AdressRange"] = False
        client["OtraComuna"] = False
        try:
            client.pop("DormMin")
            client.pop("DormMax")
        except:
            pass
        try:
            client.pop("BathMin")
            client.pop("BathMax")
        except:
            pass
        try:
            client.pop("Center")
            client.pop("Radius")
        except:
            pass
        try:
            comunaOriginal=client["comuna"][0]
            client["comuna"]=comunaOriginal
        except:
            pass

        select.confirm_report(bot,update,client)
        return pm.CONFIRM_REPORT
    elif update.message.text == "Confirmar":
        client["DormRange"] = False
        client["BathRange"] = False
        client["AdressRange"] = False
        client["OtraComuna"] = False
        select.confirm_report(bot, update, client)
        return pm.CONFIRM_REPORT
    elif update.message.text == "Salir":
        select.menu(bot, update)
        return pm.MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        select.advance(bot, update, client)
        return pm.ADVANCE

def modify(bot, update):
    # Set state:
    global STATE

    # set client
    client = clientsDict[update.message.from_user.id]
    client["modify"]=False
    if update.message.text == "Salir":

        bot.send_message(chat_id=update.message.chat_id, text="Vovliendo al menu principal")
        select.menu(bot, update)
        return pm.MENU

    elif client["product"]=="Reporte":
        if update.message.text == "Operacion":
            client.pop("operacion")
            select.operacion(bot,update,client)
            return pm.SELECT_OP
        elif update.message.text == "Tipo":
            client.pop("tipo")
            select.tipo(bot,update,client)
            return pm.SELECT_TIPO
        elif update.message.text == "Región":
            client.pop("region")
            select.region(bot,update,client)
            return pm.SELECT_REGION
        elif update.message.text == "Comuna":
            client.pop("comuna")
            select.comuna(bot,update,client)
            return pm.SELECT_COMUNA
        elif update.message.text == "Dormitorios":
            client.pop("dormitorios")
            select.dorms(bot,update,client)
            return pm.SELECT_DORMS
        elif update.message.text == "Baños":
            client.pop("banos")
            select.baths(bot,update,client)
            return pm.SELECT_BATHS
        elif update.message.text == "Precio":
            client.pop("preciomin")
            client.pop("preciomax")
            client.pop("moneda")
            select.price_range(bot,update,client)
            return pm.SELECT_PRICE_RANGE
        elif update.message.text == "Superficie":
            client.pop("metrosmin")
            client.pop("metrosmax")
            client.pop("totalmin")
            client.pop("totalmax")
            select.area_range(bot,update,client)
            return pm.SELECT_AREA_RANGE
        elif update.message.text == "Atrás":
            select.confirm_report(bot, update, client)
            return pm.CONFIRM_REPORT
        else:
            bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
            select.modify(bot, update, client)
            return pm.MODIFY

    elif client["product"]=="Tasador":
        if update.message.text == "Tipo Tasacion":
            client.pop("tipotasacion")
            select.operacion(bot,update,client)
            return pm.SELECT_OP
        elif update.message.text == "Tipo Propiedad":
            client.pop("tipo")
            select.tipo(bot,update,client)
            return pm.SELECT_TIPO
        elif update.message.text == "Región":
            client.pop("region")
            select.region(bot,update,client)
            return pm.SELECT_REGION
        elif update.message.text == "Comuna":
            client.pop("comuna")
            select.comuna(bot,update,client)
            return pm.SELECT_COMUNA
        elif update.message.text == "Dormitorios":
            client.pop("dormitorios")
            select.dorms(bot,update,client)
            return pm.SELECT_DORMS
        elif update.message.text == "Baños":
            client.pop("baños")
            select.baths(bot,update,client)
            return pm.SELECT_BATHS
        elif update.message.text == "Estacionamientos":
            client.pop("estacionamientos")
            select.feature(bot,update,client)
            return pm.SELECT_FEATURE
        elif update.message.text == "Bodegas":
            client.pop("bodegas")
            select.feature(bot,update,client)
            return pm.SELECT_FEATURE
        elif update.message.text == "Superficie":
            client.pop("metros")
            client.pop("total")
            select.area(bot,update,client)
            return pm.SELECT_AREA
        elif update.message.text == "Direccion":
            client.pop("adress")
            select.adress(bot,update,client)
            return pm.SELECT_ADRESS
        elif update.message.text == "Atrás":
            select.confirm_tasacion(bot, update, client)
            return pm.CONFIRM_TASACION
        else:
            bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
            select.modify(bot, update, client)
            return pm.MODIFY

    elif client["product"]=="Ficha":
        #Back to beggining product
        pass

    elif client["product"]=="CRM" and client["crm"]=="Buscar":
        if update.message.text == "Operacion":
            client.pop("operacion")
            select.operacion(bot,update,client)
            return pm.SELECT_OP
        elif update.message.text == "Tipo":
            client.pop("tipo")
            select.tipo(bot,update,client)
            return pm.SELECT_TIPO
        elif update.message.text == "Región":
            client.pop("region")
            select.region(bot,update,client)
            return pm.SELECT_REGION
        elif update.message.text == "Comuna":
            client.pop("comuna")
            select.comuna(bot,update,client)
            return pm.SELECT_COMUNA
        elif update.message.text == "Dormitorios":
            client.pop("dormitorios")
            select.dorms(bot,update,client)
            return pm.SELECT_DORMS
        elif update.message.text == "Baños":
            client.pop("banos")
            select.baths(bot,update,client)
            return pm.SELECT_BATHS
        elif update.message.text == "Precio":
            client.pop("preciomin")
            client.pop("preciomax")
            client.pop("moneda")
            select.price_range(bot,update,client)
            return pm.SELECT_PRICE_RANGE
        elif update.message.text == "Superficie":
            client.pop("metrosmin")
            client.pop("metrosmax")
            client.pop("totalmin")
            client.pop("totalmax")
            select.area_range(bot,update,client)
            return pm.SELECT_AREA_RANGE
        elif update.message.text == "Atrás":
            select.confirm_report(bot, update, client)
            return pm.CONFIRM_REPORT
        else:
            bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
            select.modify(bot, update, client)
            return pm.MODIFY

    elif client["product"]=="CRM" and client["crm"]=="Nueva":
        if update.message.text == "Operacion":
            client.pop("operacion")
            select.operacion(bot,update,client)
            return pm.SELECT_OP
        elif update.message.text == "Región":
            client.pop("region")
            select.region(bot,update,client)
            return pm.SELECT_REGION
        elif update.message.text == "Comuna":
            client.pop("comuna")
            select.comuna(bot,update,client)
            return pm.SELECT_COMUNA
        elif update.message.text == "Tipo":
            client.pop("tipo")
            select.tipo(bot,update,client)
            return pm.SELECT_TIPO
        elif update.message.text == "Dormitorios":
            client.pop("dormitorios")
            select.dorms(bot,update,client)
            return pm.SELECT_DORMS
        elif update.message.text == "Baños":
            client.pop("baños")
            select.baths(bot,update,client)
            return pm.SELECT_BATHS
        elif update.message.text == "Estacionamientos":
            client.pop("estacionamientos")
            select.feature(bot,update,client)
            return pm.SELECT_FEATURE
        elif update.message.text == "Bodegas":
            client.pop("bodegas")
            select.feature(bot,update,client)
            return pm.SELECT_FEATURE
        elif update.message.text == "Superficie":
            client.pop("metros")
            client.pop("total")
            select.area(bot,update,client)
            return pm.SELECT_AREA
        elif update.message.text == "Precio":
            client.pop("moneda")
            client.pop("preciomin")
            select.price_range(bot,update,client)
            return pm.SELECT_PRICE_RANGE
        elif update.message.text == "Direccion":
            client.pop("adress")
            select.adress(bot,update,client)
            return pm.SELECT_ADRESS
        elif update.message.text == "Datos Cliente":
            client.pop("telefono")
            client.pop("mailcliente")
            select.crm_feature(bot,update,client)
            return pm.CRM_FEATURE
        elif update.message.text == "Link":
            client.pop("linkPortal")
            client.pop("linkYapo")
            select.crm_feature(bot,update,client)
            return pm.CRM_FEATURE
        elif update.message.text == "Condiciones":
            client.pop("comision")
            client.pop("canje")
            select.crm_feature(bot,update,client)
            return pm.CRM_FEATURE
        elif update.message.text == "Atrás":
            select.confirm_tasacion(bot, update,client)
            return pm.CONFIRM_TASACION
        else:
            bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
            select.modify(bot, update, client)
            return pm.MODIFY

    elif client["product"]=="CRM" and client["crm"]=="Lista Completa":
        if update.message.text == "Operacion":
            pass
        elif update.message.text == "Tipo":
            select.tipo(bot,update,client)
            return pm.SELECT_TIPO
        elif update.message.text == "Región":
            select.region(bot,update,client)
            return pm.SELECT_REGION
        elif update.message.text == "Comuna":
            select.comuna(bot,update,client)
            return pm.SELECT_COMUNA
        elif update.message.text == "Atrás":
            select.crm_feature(bot, update, client)
            return pm.CRM_FEATURE
        else:
            bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
            select.modify(bot, update, client)
            return pm.MODIFY

    elif client["product"]=="CRM" and (client["crm"]=="Actualizar" or client["crm"]=="Eliminar"):
        #Back to begin
        pass


    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        select.modify(bot, update, client)
        return pm.MODIFY

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
        client["fichapro"]=False
        client["fichainterna"] = False
        select.confirm_file(bot, update, client,client["fichapro"],client["fichainterna"])
        print(client)
        return pm.CONFIRM_FILE
    if update.message.text == "www.yapo.cl":
        select.id_prop(bot, update)
        client["fichapro"]=False
        client["fichainterna"] = False
        select.confirm_file(bot, update, client,client["fichapro"],client["fichainterna"])
        print(client)
        return pm.CONFIRM_FILE
    elif update.message.text == "Atrás":
        client.pop("site")
        select.id_prop(bot, update)
        return pm.SELECT_ID
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
        print("logro calcular int, por lo que es un id y no un link")
        print(client)
        select.site(bot,update)
        return pm.SELECT_SITE

    except:
        if "portalinmobiliario.com" in update.message.text:
            client["sitio"] = "www.portalinmobiliario.com"
            print("NO logro calcular int, por lo que es un link y no un id")
            client["link_prop"] = update.message.text
            client["fichapro"]=False
            client["fichainterna"] = False
            select.confirm_file(bot, update, client,client["fichapro"],client["fichainterna"])
            print(client)
            return pm.CONFIRM_FILE
        elif "yapo.cl" in update.message.text:
            client["sitio"] = "www.yapo.cl"
            print("NO logro calcular int, por lo que es un link y no un id")
            client["link_prop"] = update.message.text
            client["fichapro"]=False
            client["fichainterna"] = False
            select.confirm_file(bot, update, client,client["fichapro"],client["fichainterna"])
            print(client)
            return pm.CONFIRM_FILE


        else:
            print("NO logro sacar nada")
            bot.send_message(chat_id=update.message.chat_id, text="Si usted inentó ingresar un id, debe ser un número entero. Si usted intentó ingresar un link, debe ser válido. ")
            select.id_prop(bot, update)
            return pm.SELECT_ID

def confirm_file(bot, update):


    global STATE

    # set client
    client = clientsDict[update.message.from_user.id]

    if update.message.text == "Confirmar" and client["product"]=="CRM":
        bot.send_message(chat_id=update.message.chat_id, text="Buscando propiedad en CRM")
        try:
            if client["cmr"]=="Actualizar":
                text=connector.actualizar(client)
                client["success"] = "check"
            else:
                text = connector.eliminar(client)
                client["success"] = "check"
        except Exception as e:
            print(e)
            text="No se encuentra la propiedad solicitada en el CRM"

        bot.send_message(chat_id=update.message.chat_id, text=text)
        select.menu(bot, update)
        return pm.MENU

    elif update.message.text == "Confirmar":
        bot.send_message(chat_id=update.message.chat_id, text="Generando Ficha")
        try:
            if "historial" in client:
                client = lastoperations["Ficha"][0]
            text=connector.connectorFicha(client)
            client["success"] = "check"
        except Exception as e:
            print(e)
            text="No se ha podido crear la ficha"

        bot.send_message(chat_id=update.message.chat_id, text=text)
        select.menu(bot, update)
        return pm.MENU
    elif update.message.text == "Modificar":
        select.modify(bot, update, client)
        return pm.MODIFY
    elif update.message.text == "Agregar Tasación":
        client["fichapro"] = True
        select.confirm_file(bot, update, client,client["fichapro"],client["fichainterna"])
        return pm.CONFIRM_FILE
    elif update.message.text == "Agregar Contacto Publicación":
        client["fichainterna"] = True
        select.confirm_file(bot, update, client,client["fichapro"],client["fichainterna"])
        return pm.CONFIRM_FILE
    elif update.message.text == "Quitar Tasación":
        client["fichapro"] = False
        select.confirm_file(bot, update, client,client["fichapro"],client["fichainterna"])
        return pm.CONFIRM_FILE
    elif update.message.text == "Quitar Contacto Publicación":
        client["fichainterna"] = False
        select.confirm_file(bot, update, client,client["fichapro"],client["fichainterna"])
        return pm.CONFIRM_FILE
    elif update.message.text == "Atrás":
        select.id_prop(bot, update)
        return pm.SELECT_ID
    elif update.message.text == "Salir":
        select.menu(bot, update)
        return pm.MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        select.confirm_file(bot, update, client, client["fichapro"], client["fichainterna"])
        return pm.CONFIRM_FILE

#FUNCIONES TASADOR

def feature(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE

    # set client
    client = clientsDict[update.message.from_user.id]
    print(client)

    if update.message.text == "0" or update.message.text == "1" or update.message.text == "2" or update.message.text == "3+":
        if "estacionamientos" not in client:
            client["estacionamientos"]= update.message.text.replace("3+","3")
            if client["tipo"]=="Departamento":
                if "modify" in client:
                    return callback(bot,update)
                else:
                    select.feature(bot,update,client)
                    return pm.SELECT_FEATURE
            else:
                select.area(bot,update,client)
                return pm.SELECT_AREA
        else:
            client["bodegas"]= update.message.text
            if "modify" in client:
                return callback(bot,update)
            else:
                select.area(bot,update,client)
                return pm.SELECT_AREA
    elif update.message.text == "Atrás":
        if "estacionamientos" in client:
            client.pop("estacionamientos")
            select.feature(bot, update,client)
            return pm.SELECT_FEATURE
        else:
            client.pop("baños")
            select.baths(bot, update,client)
            return pm.SELECT_BATHS
    elif update.message.text == "Salir":
        select.menu(bot, update)
        return pm.MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        select.feature(bot, update,client)
        return pm.SELECT_FEATURE

def area(bot,update):
    global STATE

    # set client
    client = clientsDict[update.message.from_user.id]

    if update.message.text == "Atrás":
        if "total" in client:
            client.pop("total")
            select.area(bot,update,client)
            return pm.SELECT_AREA

        elif "metros" in client:
            client.pop("metros")
            select.area(bot,update,client)
            return pm.SELECT_AREA
        else:
            client.pop("baños")
            select.baths(bot, update,client)
            return pm.SELECT_BATHS

    elif update.message.text == "Salir":
        select.menu(bot, update)
        return pm.MENU

    elif update.message.text == "Otra":
        if "metros" not in client or client["metros"]=="Otra":
            client["metros"]=update.message.text
        else:
            client["total"]=update.message.text
        select.area(bot, update, client)
        return pm.SELECT_AREA

    elif "metros" not in client or client["metros"]=="Otra":
        try:
            client["metros"] = int(update.message.text)
            select.area(bot, update, client)
            print(client)
            return pm.SELECT_AREA
        except:
            bot.send_message(chat_id=update.message.chat_id, text="Favor ingresar número entero")
            select.area(bot, update, client)
            return pm.SELECT_AREA

    else:
        try:
            client["total"] = int(update.message.text)
            if "modify" in client:
                return callback(bot,update)
            else:
                select.adress(bot, update, client)
                print(client)
                return pm.SELECT_ADRESS
        except:
            bot.send_message(chat_id=update.message.chat_id, text="Favor ingresar número entero")
            select.area(bot, update, client)
            return pm.SELECT_AREA

def adress(bot,update):

    client = clientsDict[update.message.from_user.id]
    client["adress"] = update.message.text

    if client["product"]=="CRM":
        if "modify" in client:
            return callback(bot,update)
        else:
            select.price_range(bot,update,client)
            return pm.SELECT_PRICE_RANGE
    else:
        try:
            direccion=str(update.message.text)+", "+str(client["comuna"]+", Chile")
            latD, lonD = gm.getCoordsWithAdress(direccion)
            client["lat"]=latD
            client["lon"]=lonD
            print(direccion)
            print(latD)
            print(lonD)
        except Exception as e:
            print(e)
            bot.send_message(chat_id=update.message.chat_id, text="Dirección incorrecta. Favor revisar y reenviar.")
            select.adress(bot,update,client)
            return pm.SELECT_ADRESS
        if "modify" in client:
            return callback(bot,update)
        else:
            select.confirm_tasacion(bot, update, client)
            print(client)
            return pm.CONFIRM_TASACION

def confirm_tasacion(bot,update):

    global STATE

    # set client
    client = clientsDict[update.message.from_user.id]

    if update.message.text == "Confirmar" and client["product"]=="CRM" and client["crm"]=="Nueva":
        bot.send_message(chat_id=update.message.chat_id, text="Ingresando propiedad nueva a Base de Datos")
        # Ingresar prop nueva
        text=connector.nueva(client)
        client["success"] = "check"
        bot.send_message(chat_id=update.message.chat_id, text=text,disable_web_page_preview=True)
        select.menu(bot, update)
        return pm.MENU
    elif update.message.text == "Confirmar":
        bot.send_message(chat_id=update.message.chat_id, text="Generando Tasación")
        if "historial" in client:
            client = lastoperations["Tasador"][0]
        print(client)
        text=connector.tasador(client)
        client["success"] = "check"
        bot.send_message(chat_id=update.message.chat_id, text=text,disable_web_page_preview=True)
        select.menu(bot, update)
        return pm.MENU
    elif update.message.text == "Modificar":
        select.modify(bot, update, client)
        return pm.MODIFY
    elif update.message.text == "Atrás":
        select.adress(bot, update,client)
        return pm.SELECT_ADRESS
    elif update.message.text == "Salir":
        select.menu(bot, update)
        return pm.MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        select.confirm_tasacion(bot, update, client)
        return pm.CONFIRM_TASACION

#FUNCIONES CRM

def crm(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE

    # set client
    client = clientsDict[update.message.from_user.id]
    print(client)
    client["crm"] = update.message.text

    if update.message.text == "Buscar":
        select.operacion(bot, update,client)
        return pm.SELECT_OP
    elif update.message.text == "Lista Completa":
        select.operacion(bot, update,client)
        return pm.SELECT_OP
    elif update.message.text == "Nueva":
        select.operacion(bot, update,client)
        return pm.SELECT_OP
    elif update.message.text == "Actualizar":
        select.id_prop(bot,update)
        return pm.SELECT_ID
    elif update.message.text == "Eliminar":
        select.id_prop(bot,update)
        return pm.SELECT_ID
    elif update.message.text == "Salir":
        select.menu(bot, update)
        return pm.MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        select.crm(bot, update)
        return pm.CRM

def crm_feature(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE

    # set client
    client = clientsDict[update.message.from_user.id]
    print(client)

    if client["crm"] == "Buscar":
        select.menu(bot, update)
        return pm.MENU
    elif client["crm"] == "Lista Completa":

        if update.message.text == "Confirmar":
            bot.send_message(chat_id=update.message.chat_id, text="Generando lista Completa")
            print(client)
            text=connector.listaCompleta(client)
            client["success"] = "check"
            bot.send_message(chat_id=update.message.chat_id, text=text,disable_web_page_preview=True)
            select.menu(bot, update)
            return pm.MENU
        elif update.message.text == "Modificar":
            select.modify(bot, update, client)
            return pm.MODIFY
        elif update.message.text == "Atrás":
            select.tipo(bot, update,client)
            return pm.SELECT_TIPO
        elif update.message.text == "Salir":
            select.menu(bot, update)
            return pm.MENU
        else:
            bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
            select.confirm_tasacion(bot, update, client)
            return pm.CONFIRM_TASACION
    elif client["crm"] == "Nueva":
        if "telefono" not in client:
            client["telefono"]= update.message.text
            if "modify" in client:
                return callback(bot,update)
            else:
                select.crm_feature(bot,update,client)
                return pm.CRM_FEATURE
        elif "mailcliente" not in client:
            client["mailcliente"]= update.message.text
            if "modify" in client:
                return callback(bot,update)
            else:
                select.crm_feature(bot,update,client)
                return pm.CRM_FEATURE
        elif "linkPortal" not in client:
            if "modify" in client:
                return callback(bot,update)
            else:
                client["linkPortal"]= update.message.text
                select.crm_feature(bot,update,client)
                return pm.CRM_FEATURE
        elif "linkYapo" not in client:
            if "modify" in client:
                return callback(bot,update)
            else:
                client["linkYapo"]= update.message.text
                select.crm_feature(bot,update,client)
                return pm.CRM_FEATURE
        elif "comision" not in client:
            if "modify" in client:
                return callback(bot,update)
            else:
                client["comision"]= update.message.text
                select.crm_feature(bot,update,client)
                return pm.CRM_FEATURE
        elif "canje" not in client:
            client["canje"]= update.message.text
            bot.send_message(chat_id=update.message.chat_id, text="Procesó toda la info.")
            select.confirm_tasacion(bot, update,client)
            return pm.CONFIRM_TASACION
        else:
            update.message.reply_text("Error inesperado. Volviendo al Menu")
            select.menu(bot,update)
            return pm.MENU
    elif client["crm"] == "Actualizar":
        select.menu(bot, update)
        return pm.MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Error. Regresando al Menu")
        select.menu(bot, update)
        return pm.MENU




