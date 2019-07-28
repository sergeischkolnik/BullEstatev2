from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler
from telegram.ext import ConversationHandler, CallbackQueryHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import logging
import botPropertyMain as pm
import botPropertySelect as select
import botPropertyDataBase as db

global client


def menu(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE

    #set client
    global client
    client = {}
    client["id"] = update.message.chat_id
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
        select.menu(bot,update)
        return pm.MENU
    elif update.message.text == "Casa":
        select.menu(bot, update)
        return pm.MENU
    elif update.message.text == "Atras":
        select.region(bot, update)
        return pm.SELECT_COMUNA
    elif update.message.text == "Salir":
        select.menu(bot, update)
        return pm.MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        select.tipo(bot, update)
        return pm.SELECT_TIPO