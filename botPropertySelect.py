from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler
from telegram.ext import ConversationHandler, CallbackQueryHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import logging
import botPropertyMain as pm
import botPropertySet as set
import botPropertyDataBase as db

global id

def signedup(bot,update,id):
    global STATE

    data=db.registered_data(id)
    keyboard = [["Si","No"]]


    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)



    user = update.message.from_user
    pm.logger.info("{} decidiendo si sigue con su correo registrado.".format(user.first_name))
    update.message.reply_text("Desea continuar con el correo: "+str(data[1]), reply_markup=reply_markup)
    return pm.SIGNEDUP


def first(bot,update):

    global STATE

    keyboard = [["Iniciar Sesión"],
                ["Registrarse"]]


    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)



    user = update.message.from_user
    pm.logger.info("{} decidiendo si inicia sesión, o si se registra.".format(user.first_name))
    update.message.reply_text("Favor presionar Iniciar Sesión si ud. ya posee una cuenta, o bien Registrar si es un usuario nuevo.", reply_markup=reply_markup)
    return pm.FIRST

def signup(bot,update,client):
    global STATE

    if "mail" not in client:

        user = update.message.from_user
        pm.logger.info("{} está en mail signup.".format(user.first_name))
        update.message.reply_text("Favor ingrese su correo electrónico")

    elif "pass" not in client:

        user = update.message.from_user
        pm.logger.info("{} está en pass signup.".format(user.first_name))
        update.message.reply_text("Favor ingrese su contraseña")

    elif "firstname" not in client:

        user = update.message.from_user
        pm.logger.info("{} está en firsname signup.".format(user.first_name))
        update.message.reply_text("Favor ingrese su Nombre")

    else:

        user = update.message.from_user

        pm.logger.info("{} está en Lastname signup.".format(user.first_name))
        update.message.reply_text("Favor ingrese su apellido")

    return pm.SIGNUP

def login(bot, update,client):
    global STATE

    if "mail" not in client:

        user = update.message.from_user
        pm.logger.info("{} está en mail login.".format(user.first_name))
        update.message.reply_text("Favor ingrese su correo electrónico")

    elif "pass" not in client:

        user = update.message.from_user
        pm.logger.info("{} está en pass login.".format(user.first_name))
        update.message.reply_text("Favor ingrese su contraseña")

    elif "firstname" not in client:

        user = update.message.from_user
        pm.logger.info("{} está en firsname login.".format(user.first_name))
        update.message.reply_text("Favor ingrese su Nombre")

    else:

        user = update.message.from_user

        pm.logger.info("{} está en Lastname login.".format(user.first_name))
        update.message.reply_text("Favor ingrese su apellido")

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
                                       one_time_keyboard=True,
                                       resize_keyboard=True)



    user = update.message.from_user
    pm.logger.info("{} está en el menu principal.".format(user.first_name))
    update.message.reply_text("Menu Principal", reply_markup=reply_markup)
    return pm.MENU

##### FUNCIONES DEL REPORTE

def operacion(bot, update):

    user = update.message.from_user
    pm.logger.info("Report requested by {}.".format(user.first_name))

    keyboard = [["Comprar","Arrendar"],
                ["Atrás", "Salir"]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)

    user = update.message.from_user
    pm.logger.info("{} está eligiendo operacion.".format(user.first_name))
    update.message.reply_text("Seleccione operacion", reply_markup=reply_markup)

    return pm.SELECT_OP

def region(bot, update,client):
    """
    Main menu function.
    This will display the options from the main menu.
    """
    user = update.message.from_user
    # Create buttons to slect language:
    if "region" not in client:

        keyboard = [["Metropolitana","Valparaíso"],
                    ["Bio-Bio","Coquimbo"],
                    ["Antofagasta","Otra"],
                    ["Atrás", "Salir"]]

        reply_markup = ReplyKeyboardMarkup(keyboard,
                                           one_time_keyboard=True,
                                           resize_keyboard=True)


        pm.logger.info("{} está seleccionando region.".format(user.first_name))
        update.message.reply_text("Seleccionar region", reply_markup=reply_markup)

    else:
        pm.logger.info("{} está seleccionando region.".format(user.first_name))
        update.message.reply_text("Favor ingresar una de las siguientes opciones:\nArica\nIquique\nAtacama\nOhiggins\nMaule\nÑuble\nAraucanía\nLos Ríos\nLos Lagos\nAysen\nMagallanes")

    return pm.SELECT_REGION

def comuna(bot,update,client):

    user = update.message.from_user
    if "comuna" not in client:
        if client["region"] == "Metropolitana":
            keyboard = [["Las Condes","Providencia"],
                        ["Ñuñoa","Santiago Centro"],
                        ["San Miguel","Otra"],
                        ["Atrás", "Salir"]]
            reply_markup = ReplyKeyboardMarkup(keyboard,
                                               one_time_keyboard=True,
                                               resize_keyboard=True)

            pm.logger.info("{} está seleccionando comuna.".format(user.first_name))
            update.message.reply_text("Seleccionar Comuna", reply_markup=reply_markup)

        elif client["region"] == "Valparaíso":
            keyboard = [["Valparaíso","Viña del Mar"],
                        ["Quilpue","Concon"],
                        ["Quillota","Otra"],
                        ["Atrás", "Salir"]]

            reply_markup = ReplyKeyboardMarkup(keyboard,
                                               one_time_keyboard=True,
                                               resize_keyboard=True)

            pm.logger.info("{} está seleccionando comuna.".format(user.first_name))
            update.message.reply_text("Seleccionar Comuna", reply_markup=reply_markup)
        else:

            pm.logger.info("{} está seleccionando comuna.".format(user.first_name))
            update.message.reply_text("Ingresar Comuna")
    else:
        pm.logger.info("{} está seleccionando comuna.".format(user.first_name))
        update.message.reply_text("Ingresar Comuna")

    return pm.SELECT_COMUNA

def tipo(bot,update):

    user = update.message.from_user


    keyboard = [["Departamento","Casa"],
                ["Atrás", "Salir"]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)

    pm.logger.info("{} está seleccionando Tipo.".format(user.first_name))
    update.message.reply_text("Seleccionar Tipo", reply_markup=reply_markup)

    return pm.SELECT_TIPO

def dorms(bot,update):

    user = update.message.from_user


    keyboard = [["1","2","3","4+"],
                ["Atrás", "Salir"]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)

    pm.logger.info("{} está seleccionando Dormitorios.".format(user.first_name))
    update.message.reply_text("Seleccionar Número de Dormitorios", reply_markup=reply_markup)

    return pm.SELECT_DORMS

def baths(bot,update):

    user = update.message.from_user


    keyboard = [["1","2","3","4+"],
                ["Atrás", "Salir"]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)

    pm.logger.info("{} está seleccionando Baños.".format(user.first_name))
    update.message.reply_text("Seleccionar Número de Baños", reply_markup=reply_markup)

    return pm.SELECT_BATHS

def price_range(bot, update,client):
    global STATE
    """
    Main menu function.
    This will display the options from the main menu.
    """
    # Create buttons to slect language:
    print("entro al select de pricerange")

    if "moneda" not in client:

        user = update.message.from_user

        print("entro al if de moneda")
        keyboard = [["UF", "Pesos"],
                    ["Atrás", "Salir"]]

        reply_markup = ReplyKeyboardMarkup(keyboard,
                                           one_time_keyboard=True,
                                           resize_keyboard=True)

        pm.logger.info("{} está seleccionando moneda.".format(user.first_name))
        update.message.reply_text("Seleccionar Moneda", reply_markup=reply_markup)
        return pm.SELECT_PRICE_RANGE

    elif "preciomin" not in client:
        if client["moneda"]=="UF":
            user = update.message.from_user

            keyboard = [["0","1000","2000","3000","4000","5000"],
                        ["7000","10000","15000","Otro","Atrás","Salir"]]

            reply_markup = ReplyKeyboardMarkup(keyboard,
                                               one_time_keyboard=True,
                                               resize_keyboard=True)

            pm.logger.info("{} está seleccionando moneda.".format(user.first_name))
            update.message.reply_text("Seleccionar Precio Mínimo en UF", reply_markup=reply_markup)
            return pm.SELECT_PRICE_RANGE

        else:
            user = update.message.from_user

            print("entro al if de moneda")
            keyboard = [["0","25.000.000","50.000.000","100.000.000"],
                        ["150.000.000","200.000.000","Otro","Atrás","Salir"]]

            reply_markup = ReplyKeyboardMarkup(keyboard,
                                               one_time_keyboard=True,
                                               resize_keyboard=True)

            pm.logger.info("{} está seleccionando moneda.".format(user.first_name))
            update.message.reply_text("Seleccionar Precio Mínimo en Pesos", reply_markup=reply_markup)
            return pm.SELECT_PRICE_RANGE

    elif client["preciomin"]=="Otro":
        user = update.message.from_user
        pm.logger.info("{} está en seleccionando precio mínimo.".format(user.first_name))
        update.message.reply_text("Ingresar precio mínimo")
        return pm.SELECT_PRICE_RANGE

    elif "preciomax" not in client:
        if client["moneda"]=="UF":
            user = update.message.from_user
            x=client["preciomin"]
            keyboard = [[str(x+1000),str(x+2000),str(x+3000),str(x+4000),str(x+5000)],
                        [str(x+7000),str(x+10000),"Otro","Atrás","Salir"]]

            reply_markup = ReplyKeyboardMarkup(keyboard,
                                               one_time_keyboard=True,
                                               resize_keyboard=True)

            pm.logger.info("{} está seleccionando moneda.".format(user.first_name))
            update.message.reply_text("Seleccionar Precio Máximo en UF", reply_markup=reply_markup)
            return pm.SELECT_PRICE_RANGE
        else:
            user = update.message.from_user
            x=client["preciomin"]
            keyboard = [[str(x+10000000),str(x+2000000),str(x+30000000),str(x+50000000)],
                        [str(x+100000000),"Otro","Atrás","Salir"]]

            reply_markup = ReplyKeyboardMarkup(keyboard,
                                               one_time_keyboard=True,
                                               resize_keyboard=True)

            pm.logger.info("{} está seleccionando moneda.".format(user.first_name))
            update.message.reply_text("Seleccionar Precio Máximo en Pesos", reply_markup=reply_markup)
            return pm.SELECT_PRICE_RANGE
    elif client["preciomax"]=="Otro":
        user = update.message.from_user
        pm.logger.info("{} está en seleccionando precio máximo.".format(user.first_name))
        update.message.reply_text("Ingresar precio máximo")
        return pm.SELECT_PRICE_RANGE



def area_range(bot, update, stage,tip):
    global STATE
    """
    Main menu function.
    This will display the options from the main menu.
    """
    # Create buttons to slect language:
    user = update.message.from_user
    print("entro al select de arearange")
    print("esta en stage: " + stage)
    print("esta en tipo: " + tip)

    if tip == "Departamento":

        if stage == "metrosmin":
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando superficie mínima.".format(user.first_name))
            update.message.reply_text("Ingresar superficie útil mínima (en m2)")

        if stage == "metrosmax":
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando superficie máxima.".format(user.first_name))
            update.message.reply_text("Ingresar superficie útil máxima (en m2)")

        if stage == "totalmin":
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando superficie máxima.".format(user.first_name))
            update.message.reply_text("Ingresar superficie total mínima (en m2)")

        if stage == "totalmax":
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando superficie máxima.".format(user.first_name))
            update.message.reply_text("Ingresar superficie total máxima (en m2)")

    if tip == "Casa":

        if stage == "metrosmin":
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando superficie mínima.".format(user.first_name))
            update.message.reply_text("Ingresar superficie construída mínima (en m2)")

        if stage == "metrosmax":
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando superficie máxima.".format(user.first_name))
            update.message.reply_text("Ingresar superficie construída máxima (en m2)")

        if stage == "totalmin":
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando superficie máxima.".format(user.first_name))
            update.message.reply_text("Ingresar superficie terreno mínima (en m2)")

        if stage == "totalmax":
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando superficie máxima.".format(user.first_name))
            update.message.reply_text("Ingresar superficie terreno máxima (en m2)")



    return pm.SELECT_AREA_RANGE

def confirm_report(bot,update,client):

    user = update.message.from_user


    keyboard = [["SI","Modificar"],
                ["Atrás", "Salir"]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)


    pm.logger.info("{} está confirmando reporte.".format(user.first_name))
    confirmtext=[]
    confirmtext.append("Generar reporte para las siguientes características:")
    confirmtext.append("Operación:"+client["operacion"])
    confirmtext.append("Región:"+client["region"])
    confirmtext.append("Comuna:"+client["comuna"])
    confirmtext.append("Tipo:"+client["tipo"])
    confirmtext.append("Dormitorios:"+client["dormitorios"])
    confirmtext.append("Baños:"+client["baños"])
    confirmtext.append("Desde: "+client["moneda"]+" "+str(client["preciomin"])+", Hasta: "+client["moneda"]+" "+str(client["preciomax"]))
    if client["tipo"]=="Departamento":
        confirmtext.append("Desde: "+str(client["metrosmin"])+"m2 útiles, Hasta: "+str(client["metrosmax"])+"m2 útiles")
        confirmtext.append("Desde: "+str(client["metrosmin"])+"m2 totales, Hasta: "+str(client["metrosmax"])+"m2 totales")
    if client["tipo"]=="Casa":
        confirmtext.append("Desde: "+str(client["metrosmin"])+"m2 construidos, Hasta: "+str(client["metrosmax"])+"m2 construidos")
        confirmtext.append("Desde: "+str(client["metrosmin"])+"m2 de terreno, Hasta: "+str(client["metrosmax"])+"m2 de terreno")


    confirmtext="\n".join(confirmtext)
    print(confirmtext)
    update.message.reply_text(confirmtext, reply_markup=reply_markup)

    return pm.CONFIRM_REPORT

##### FUNCIONES DE LAS FICHAS

def site(bot, update):
    global STATE
    """
    Main menu function.
    This will display the options from the main menu.
    """
    # Create buttons to slect language:
    keyboard = [["www.portalinmobiliario.com"],
                ["www.yapo.cl"],
                ["Atrás", "Salir"]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)



    user = update.message.from_user
    pm.logger.info("{} está escogiendo sitio de origen.".format(user.first_name))
    update.message.reply_text("Seleccionar sitio de origen", reply_markup=reply_markup)
    return pm.SELECT_SITE

def id_prop(bot, update):
    global STATE
    """
    Main menu function.
    This will display the options from the main menu.
    """

    user = update.message.from_user
    pm.logger.info("{} está escogiendo id o link.".format(user.first_name))
    update.message.reply_text("Ingrese id propiedad, o bien el link de la publicación")
    return pm.SELECT_ID
def confirm_file(bot, update,client,pro,interna):
    user = update.message.from_user

    if pro:
        probutton="Quitar"
        protext="Si"
    else:
        probutton="Agregar"
        protext = "No"
    if interna:
        internabutton="Quitar"
        internatext="Si"
    else:
        internabutton="Agregar"
        internatext="No"


    keyboard = [["Confirmar","Modificar"],
                [probutton+" Tasación"],
                [internabutton+" Contacto Publicación"],
                ["Atrás", "Salir"]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)
    print("creo el teclado")

    pm.logger.info("{} está confirmando ficha.".format(user.first_name))
    confirmtext=[]
    confirmtext.append("Generar ficha para las siguientes características:")
    confirmtext.append("Sitio de origen:"+client["sitio"])
    if "id_prop" in client:
        confirmtext.append("ID Propiedad:"+str(client["id_prop"]))
    else:
        confirmtext.append("URL Propiedad:" + str(client["link_prop"]))
    confirmtext.append("La Ficha solicitada "+protext+" Incluye Tasación")
    confirmtext.append("La Ficha solicitada "+internatext+" Incluye Datos de contacto de Publicación")
    confirmtext.append("Se enviara al siguiente correo:"+client["mail"])

    confirmtext="\n".join(confirmtext)
    print(confirmtext)
    update.message.reply_text(confirmtext, reply_markup=reply_markup,disable_web_page_preview=True)

    return pm.CONFIRM_FILE
