from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler
from telegram.ext import ConversationHandler, CallbackQueryHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import logging
import botPropertyMain as pm
import botPropertySelect as select
import botPropertyDataBase as db

global client


def start(bot, update):
    global client
    client = {}

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


    select.login(bot, update,client)
    return pm.LOGIN

def login(bot,update):
    # Set state:
    global STATE
    print("Cliente inicial:")
    print(client)
    client["id"] = update.message.chat_id
    if "mail" not in client and (('@' and '.') in update.message.text):
        client["mail"]=update.message.text
        select.login(bot, update,client)
        return pm.LOGIN
    elif "mail" not in client and (('@' and '.') not in update.message.text):
        bot.send_message(chat_id=update.message.chat_id, text="Correo incorrecto. Favor ingresar correo valido")
        select.login(bot, update, client)
        return pm.LOGIN
    else:
        client["pass"] = update.message.text
        select.menu(bot, update)
        return pm.MENU

def menu(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE

    #set client
    global client

    client["product"] = update.message.text
    print(client)

    if update.message.text == "Reporte":
        select.operacion(bot, update)
        return pm.SELECT_OP
    elif update.message.text == "Ficha":
        select.menu(bot, update)
        return pm.MENU
    elif update.message.text == "Ayuda":
        select.menu(bot, update)
        return pm.MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        client.pop("product")
        select.menu(bot, update)
        return pm.MENU

def operacion(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE

    # set client
    global client
    client["operacion"] = update.message.text
    print(client)

    user = update.message.from_user
    if update.message.text == "Comprar":
        select.region(bot,update)
        return pm.SELECT_REGION
    elif update.message.text == "Arrendar":
        select.region(bot, update)
        return pm.SELECT_REGION
    elif update.message.text == "Atras":
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
    global client
    client["region"] = update.message.text
    print(client)

    if update.message.text == "RM":
        select.comuna(bot,update)
        return pm.SELECT_COMUNA
    elif update.message.text == "Valpo":
        select.comuna(bot, update)
        return pm.SELECT_COMUNA
    elif update.message.text == "Atras":
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
    global client
    client["comuna"] = update.message.text
    print(client)

    if update.message.text == "Las Condes":
        select.tipo(bot,update)
        return pm.SELECT_TIPO
    elif update.message.text == "Providencia":
        select.tipo(bot, update)
        return pm.SELECT_TIPO
    elif update.message.text == "Atras":
        select.region(bot, update)
        return pm.SELECT_REGION
    elif update.message.text == "Salir":
        select.menu(bot, update)
        return pm.MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        select.comuna(bot, update)
        return pm.SELECT_COMUNA

def tipo(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE

    # set client
    global client
    client["tipo"] = update.message.text
    print(client)

    if update.message.text == "Departamento":
        select.dorms(bot,update)
        return pm.SELECT_DORMS
    elif update.message.text == "Casa":
        select.dorms(bot, update)
        return pm.SELECT_DORMS
    elif update.message.text == "Atras":
        select.comuna(bot, update)
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
    global client
    client["dormitorios"] = update.message.text
    print(client)

    if update.message.text == ("1" or "2" or "3" or "4+"):
        select.baths(bot,update)
        return pm.SELECT_BATHS
    elif update.message.text == "Atras":
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
    global client
    client["baños"] = update.message.text
    print(client)

    if update.message.text == ("1" or "2" or "3" or "4+"):
        select.price_range(bot,update,"moneda")
        return pm.SELECT_PRICE_RANGE
    elif update.message.text == "Atras":
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
    global client
    if "moneda" not in client:
        client["moneda"] = update.message.text
        if update.message.text == "UF":
            select.price_range(bot, update, "preciomin")
            return pm.SELECT_PRICE_RANGE
        elif update.message.text == "Pesos":
            select.price_range(bot, update, "preciomin")
            return pm.SELECT_PRICE_RANGE
        elif update.message.text == "Atras":
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
            select.area_range(bot, update, "metrosmin")
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
    global client
    if "metrosmin" not in client:
        try:
            client["metrosmin"] = int(update.message.text)
            select.area_range(bot, update, "metrosmax")
            print(client)
            return pm.SELECT_AREA_RANGE
        except:
            bot.send_message(chat_id=update.message.chat_id, text="Favor ingresar número entero")
            select.area_range(bot, update, "metrosmin")
            return pm.SELECT_AREA_RANGE

    else:
        try:
            client["metrosmax"] = int(update.message.text)
            select.confirm_report(bot, update, client)
            print(client)
            return pm.CONFIRM_REPORT
        except:
            bot.send_message(chat_id=update.message.chat_id, text="Favor ingresar número entero")
            select.area_range(bot, update, "metrosmax")
            return pm.SELECT_AREA_RANGE


def confirm_report(bot,update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE

    # set client
    global client

    if update.message.text == "SI":
        #generar reporte para cliente, enviar al correo correspondiente
        bot.send_message(chat_id=update.message.chat_id, text="Reporte generado y enviado exitosamente al correo: "+(client["mail"])+".")
        select.menu(bot, update)
        return pm.MENU
    elif update.message.text == "NO":
        bot.send_message(chat_id=update.message.chat_id, text="Reporte Cancelado")
        select.menu(bot, update)
        return pm.MENU