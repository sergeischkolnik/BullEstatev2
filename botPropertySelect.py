from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler
from telegram.ext import ConversationHandler, CallbackQueryHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import logging
import botPropertyMain as pm
import botPropertySet as set
import botPropertyDataBase as db

global id


def login(bot, update,client):
    global STATE
    """
    Main menu function.
    This will display the options from the main menu.
    """
    # Create buttons to slect language:
    if "mail" in client:

        user = update.message.from_user
        pm.logger.info("{} está en mail login.".format(user.first_name))
        update.message.reply_text("Favor ingrese su contraseña")
    else:


        user = update.message.from_user
        pm.logger.info("{} está en pass login.".format(user.first_name))
        update.message.reply_text("Favor ingrese su correo electrónico")

    return pm.LOGIN

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
                                       one_time_keyboard=False,
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
    pm.logger.info("{} está eligiendo operacion.".format(user.first_name))
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

    return pm.SELECT_COMUNA

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

def dorms(bot,update):

    user = update.message.from_user


    keyboard = [["1","2","3","4+"],
                ["Atras", "Salir"]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)

    pm.logger.info("{} está seleccionando Tipo.".format(user.first_name))
    update.message.reply_text("Seleccionar Número de Dormitorios", reply_markup=reply_markup)

    return pm.SELECT_DORMS

def baths(bot,update):

    user = update.message.from_user


    keyboard = [["1","2","3","4+"],
                ["Atras", "Salir"]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)

    pm.logger.info("{} está seleccionando Tipo.".format(user.first_name))
    update.message.reply_text("Seleccionar Número de Baños", reply_markup=reply_markup)

    return pm.SELECT_BATHS

def price_range(bot, update,stage):
    global STATE
    """
    Main menu function.
    This will display the options from the main menu.
    """
    # Create buttons to slect language:

    if stage=="moneda":
        keyboard = [["UF", "Pesos"],
                    ["Atras", "Salir"]]

        reply_markup = ReplyKeyboardMarkup(keyboard,
                                           one_time_keyboard=True,
                                           resize_keyboard=True)

        pm.logger.info("{} está seleccionando moneda.".format(user.first_name))
        update.message.reply_text("Seleccionar Moneda", reply_markup=reply_markup)


    if stage=="preciomin":

        user = update.message.from_user
        pm.logger.info("{} está en seleccionando precio mínimo.".format(user.first_name))
        update.message.reply_text("Seleccionar precio mínimo")


    if stage == "preciomax":
        user = update.message.from_user
        pm.logger.info("{} está en seleccionando precio máximo.".format(user.first_name))
        update.message.reply_text("Seleccionar precio máximo")


    return pm.SELECT_PRICE_RANGE


def area_range(bot, update, stage):
    global STATE
    """
    Main menu function.
    This will display the options from the main menu.
    """
    # Create buttons to slect language:


    if stage == "metrosmin":
        user = update.message.from_user
        pm.logger.info("{} está en seleccionando superficie mínima.".format(user.first_name))
        update.message.reply_text("Seleccionar superficie mínima")

    if stage == "metrosmax":
        user = update.message.from_user
        pm.logger.info("{} está en seleccionando superficie máxima.".format(user.first_name))
        update.message.reply_text("Seleccionar superficie máxima")

    return pm.SELECT_AREA_RANGE

def confirm_report(bot,update,client):

    user = update.message.from_user


    keyboard = [["SI","NO"],
                ["Atras", "Salir"]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)

    pm.logger.info("{} está confirmando reporte.".format(user.first_name))
    confirmtext=[]
    confirmtext.append("Generar reporte para las siguientes características:")
    confirmtext.append("Operación:"+client[""])
    confirmtext.append("Región:"+client[""])
    confirmtext.append("Comuna:"+client[""])
    confirmtext.append("Tipo:"+client[""])
    confirmtext.append("Dormitorios:"+client[""])
    confirmtext.append("Baños:"+client[""])
    confirmtext.append("Desde:"+client["moneda"]+" "+client["preciomin"]+", Hasta:"+client["moneda"]+" "+client["preciomax"])
    confirmtext.append("Desde:"+client["metrosmin"]+"m2, Hasta:"+client["metrosmax"]+"m2")

    confirmtext="\n".join(confirmtext)

    update.message.reply_text(confirmtext, reply_markup=reply_markup)

    return pm.CONFIRM_REPORT