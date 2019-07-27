from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler
from telegram.ext import ConversationHandler, CallbackQueryHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import logging
import botPropertyMain as pm
import botPropertySelect as select
import botPropertyDataBase as db

global id


def menu(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE
    user = update.message.from_user
    if update.message.text == "Reporte":
        STATE = SELECT_OP
        select.operacion(bot, update)
        return product,SELECT_OP
    elif update.message.text == "Ficha":
        select.menu(bot, update)
        return MENU
    elif update.message.text == "Ayuda":
        select.menu(bot, update)
        return MENU
    else:
        STATE = MENU
        return MENU

def operacion(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE
    user = update.message.from_user
    if update.message.text == "Comprar":
        STATE = SELECT_MULTIPLE
        vars_us[user.id]["OP"] = "Comprar"
        select.region(bot,update)
        return SELECT_MULTIPLE
    elif update.message.text == "Arrendar":
        STATE = SELECT_MULTIPLE
        vars_us[user.id]["OP"] = "Arrendar"
        select.region(bot, update)
        return SELECT_MULTIPLE
    elif update.message.text == "Atras":
        STATE = MENU
        select.menu(bot, update)
        return MENU
    elif update.message.text == "Salir":
        select.menu(bot, update)
        return MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        select.operacion(bot, update)
        STATE = SELECT_OP
        return SELECT_OP

def region(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE
    user = update.message.from_user
    if update.message.text == "RM":
        STATE = SELECT_COMUNA
        vars_us[user.id]["Region"] = "RM"
        select.comuna(bot,update)
        return MENU
    elif update.message.text == "Valpo":
        STATE = SELECT_COMUNA
        vars_us[user.id]["Region"] = "Valpo"
        select.comuna(bot, update)
        return MENU
    elif update.message.text == "Atras":
        STATE = SELECT_OP
        report(bot, update)
        return SELECT_OP
    elif update.message.text == "Salir":
        select.menu(bot, update)
        return MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        set.region(bot, update)
        STATE = SELECT_REGION
        return SELECT_REGION