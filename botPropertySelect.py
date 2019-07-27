from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler
from telegram.ext import ConversationHandler, CallbackQueryHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import logging
import botPropertyMain as pm
import botPropertySet as set
import botPropertyDataBase as db

global id


def menu(bot, update):
    global STATE
    """
    Main menu function.
    This will display the options from the main menu.
    """
    # Create buttons to slect language:
    keyboard = [["Reporte"],
                ["Ficha", "Ayuda"]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)

    user = update.message.from_user
    pm.logger.info("{} está en el menu principal.".format(user.first_name))
    update.message.reply_text("menu principal", reply_markup=reply_markup)

    return pm.MENU

def operacion(bot, update):

    user = update.message.from_user
    pm.logger.info("Report requested by {}.".format(user.first_name))

    keyboard = [["Comprar","Arrendar"],
                ["Atras", "Salir"]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)

    user = update.message.from_user
    pm.logger.info("{} está eligigiendo operacion.".format(user.first_name))
    update.message.reply_text("Seleccione operacion", reply_markup=reply_markup)

    return pm.SELECT_OP

def region(bot, update):
    """
    Main menu function.
    This will display the options from the main menu.
    """
    user = update.message.from_user
    # Create buttons to slect language:
    keyboard = [["RM","Valpo"],
                ["Atras", "Salir"]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)


    pm.logger.info("{} está seleccionando region.".format(user.first_name))
    update.message.reply_text("Seleccionar region", reply_markup=reply_markup)

    return pm.SELECT_REGION

def comuna(bot,update):

    user = update.message.from_user


    keyboard = [["Las Condes","Providencia"],
                ["Atras", "Salir"]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)

    pm.logger.info("{} está seleccionando comuna.".format(user.first_name))
    update.message.reply_text("Seleccionar Comuna", reply_markup=reply_markup)

    return pm.SELECT_COM

def tipo(bot,update):

    user = update.message.from_user


    keyboard = [["Departamento","Casa"],
                ["Atras", "Salir"]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)

    pm.logger.info("{} está seleccionando Tipo.".format(user.first_name))
    update.message.reply_text("Seleccionar Tipo", reply_markup=reply_markup)

    return pm.SELECT_TIPO