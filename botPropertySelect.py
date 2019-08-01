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
    keyboard = [["Reporte","Tasador"],
                ["Ficha", "Ayuda"]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)



    user = update.message.from_user
    pm.logger.info("{} está en el menu principal.".format(user.first_name))
    update.message.reply_text("Menu Principal", reply_markup=reply_markup)
    return pm.MENU

##### FUNCIONES DEL REPORTE

def operacion(bot, update,client):

    user = update.message.from_user
    pm.logger.info("Report requested by {}.".format(user.first_name))

    if client["product"]=="Reporte":
        keyboard = [["Comprar","Arrendar"],
                    ["Atrás", "Salir"]]
    else:
        keyboard = [["Venta","Arriendo"],
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
        update.message.reply_text("Favor ingresar una de las siguientes opciones:\nArica\nIquique\nAtacama\nOhiggins\nMaule\nÑuble\nAraucanía\nLos Ríos\nLos Lagos\nAysén\nMagallanes")

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
                ["Oficina","Comercial"],
                ["Atrás", "Salir"]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)

    pm.logger.info("{} está seleccionando Tipo.".format(user.first_name))
    update.message.reply_text("Seleccionar Tipo", reply_markup=reply_markup)

    return pm.SELECT_TIPO

def dorms(bot,update,client):

    user = update.message.from_user

    if client["product"]=="Reporte":
        keyboard = [["1","2","3","4+"],
                    ["Atrás", "Salir"]]
    else:
        keyboard = [["1","2","3","4","5","6","7"],
                    ["8","9","10","Atrás", "Salir"]]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)
    if client["tipo"]=="Departamento" or client["tipo"]=="Casa":
        pm.logger.info("{} está seleccionando Dormitorios.".format(user.first_name))
        update.message.reply_text("Seleccionar Número de Dormitorios", reply_markup=reply_markup)
    elif client["tipo"]=="Oficina":
        pm.logger.info("{} está seleccionando Privados.".format(user.first_name))
        update.message.reply_text("Seleccionar Número de Privados", reply_markup=reply_markup)
    return pm.SELECT_DORMS

def baths(bot,update,client):

    user = update.message.from_user


    if client["product"]=="Reporte":
        keyboard = [["1","2","3","4+"],
                    ["Atrás", "Salir"]]
    else:
        keyboard = [["1","2","3","4","5","6","7"],
                    ["8","9","10","Atrás", "Salir"]]

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
            if client["operacion"]=="Arrendar":
                keyboard = [["0","5","10","15","20","25"],
                            ["35","50","75","Otro","Atrás","Salir"]]

            else:
                keyboard = [["0","1.000","2.000","3.000"],
                            ["4.000","5.000","7.000","10.000"],
                            ["15.000","Otro","Atrás","Salir"]]

            reply_markup = ReplyKeyboardMarkup(keyboard,
                                               one_time_keyboard=True,
                                               resize_keyboard=True)

            pm.logger.info("{} está seleccionando moneda.".format(user.first_name))
            update.message.reply_text("Seleccionar Precio Mínimo en UF", reply_markup=reply_markup)
            return pm.SELECT_PRICE_RANGE

        else:
            user = update.message.from_user

            print("entro al if de moneda")
            if client["operacion"]=="Comprar":
                keyboard = [["0","25.000.000","50.000.000"],
                            ["75.000.000","100.000.000","150.000.000"],
                            ["200.000.000","Otro","Atrás","Salir"]]

            else:
                keyboard = [["0","150.000","200.000"],
                            ["300.000","500.000","750.000"],
                            ["1.000.000","Otro","Atrás","Salir"]]

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
            keyboard = [['{:,}'.format(x+1000).replace(",","."),'{:,}'.format(x+2000).replace(",","."),'{:,}'.format(x+3000).replace(",",".")],
                        ['{:,}'.format(x+4000).replace(",","."),'{:,}'.format(x+5000).replace(",","."),'{:,}'.format(x+7000).replace(",",".")],
                        ['{:,}'.format(x+10000).replace(",","."),"Otro","Atrás","Salir"]]

            reply_markup = ReplyKeyboardMarkup(keyboard,
                                               one_time_keyboard=True,
                                               resize_keyboard=True)

            pm.logger.info("{} está seleccionando moneda.".format(user.first_name))
            update.message.reply_text("Seleccionar Precio Máximo en UF", reply_markup=reply_markup)
            return pm.SELECT_PRICE_RANGE
        else:
            user = update.message.from_user
            x=client["preciomin"]
            keyboard = [['{:,}'.format(x+10000000).replace(",","."),'{:,}'.format(x+2000000).replace(",",".")],
                        ['{:,}'.format(x+30000000).replace(",","."),'{:,}'.format(x+50000000).replace(",",".")],
                        ['{:,}'.format(x+100000000).replace(",","."),"Otro","Atrás","Salir"]]

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

def area_range(bot, update,client):
    global STATE
    """
    Main menu function.
    This will display the options from the main menu.
    """
    # Create buttons to slect language:
    user = update.message.from_user
    print("entro al select de arearange")
    print("esta en tipo: " + client["tipo"])

    if client["tipo"] == "Departamento" or client["tipo"] == "Oficina" or client["tipo"] == "Comercial":

        if "metrosmin" not in client:
            user = update.message.from_user

            keyboard = [["0","20","30","40","50","60","70","80"],
                        ["100","150","200","Otra","Atrás","Salir"]]

            reply_markup = ReplyKeyboardMarkup(keyboard,
                                               one_time_keyboard=True,
                                               resize_keyboard=True)

            pm.logger.info("{} está en seleccionando superficie mínima.".format(user.first_name))
            if client["tipo"] == "Comercial":
                update.message.reply_text("Seleccionar superficie mínima (en m2)", reply_markup=reply_markup)
                return pm.SELECT_AREA_RANGE
            else:
                update.message.reply_text("Seleccionar superficie útil mínima (en m2)", reply_markup=reply_markup)
                return pm.SELECT_AREA_RANGE

        elif client["metrosmin"]=="Otra":
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando superficie mínima.".format(user.first_name))
            if client["tipo"] == "Comercial":
                update.message.reply_text("Seleccionar superficie mínima (en m2)")
                return pm.SELECT_AREA_RANGE
            else:
                update.message.reply_text("Seleccionar superficie útil mínima (en m2)")
                return pm.SELECT_AREA_RANGE

        elif "metrosmax" not in client:
            user = update.message.from_user
            x=int(client["metrosmin"])

            keyboard = [[str(x+5),str(x+10),str(x+15),str(x+20),str(x+30),str(x+40),str(x+50)],
                        [str(x+100),str(x+200),"Otra","Atrás","Salir"]]

            reply_markup = ReplyKeyboardMarkup(keyboard,
                                               one_time_keyboard=True,
                                               resize_keyboard=True)

            pm.logger.info("{} está en seleccionando superficie mínima.".format(user.first_name))
            if client["tipo"] == "Comercial":
                update.message.reply_text("Seleccionar superficie mínima (en m2)", reply_markup=reply_markup)
                return pm.SELECT_AREA_RANGE
            else:
                update.message.reply_text("Seleccionar superficie útil mínima (en m2)", reply_markup=reply_markup)
                return pm.SELECT_AREA_RANGE

        elif client["metrosmax"]=="Otra":
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando superficie máxima.".format(user.first_name))
            update.message.reply_text("Ingresar superficie útil máxima (en m2)")
            return pm.SELECT_AREA_RANGE

        elif "totalmin" not in client:
            user = update.message.from_user

            x=int(client["metrosmin"])

            keyboard = [[str(x+0),str(x+2),str(x+5),str(x+7),str(x+10),str(x+15),str(x+20)],
                        [str(x+30),str(x+50),"Otra","Atrás","Salir"]]

            reply_markup = ReplyKeyboardMarkup(keyboard,
                                               one_time_keyboard=True,
                                               resize_keyboard=True)

            pm.logger.info("{} está en seleccionando superficie mínima.".format(user.first_name))
            update.message.reply_text("Seleccionar superficie total mínima (en m2)", reply_markup=reply_markup)
            return pm.SELECT_AREA_RANGE

        elif client["totalmin"]=="Otra":
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando superficie máxima.".format(user.first_name))
            update.message.reply_text("Ingresar superficie total mínima (en m2)")
            return pm.SELECT_AREA_RANGE

        elif "totalmax" not in client:
            user = update.message.from_user

            x=min(int(client["metrosmax"]),client["totalmin"])

            keyboard = [[str(x+5),str(x+10),str(x+15),str(x+20),str(x+30),str(x+40),str(x+50)],
                        [str(x+100),str(x+200),"Otra","Atrás","Salir"]]


            reply_markup = ReplyKeyboardMarkup(keyboard,
                                               one_time_keyboard=True,
                                               resize_keyboard=True)

            pm.logger.info("{} está en seleccionando superficie mínima.".format(user.first_name))
            update.message.reply_text("Seleccionar superficie total máxima (en m2)", reply_markup=reply_markup)
            return pm.SELECT_AREA_RANGE

        elif client["totalmax"]=="Otra":
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando superficie máxima.".format(user.first_name))
            update.message.reply_text("Ingresar superficie total máxima (en m2)")
            return pm.SELECT_AREA_RANGE

    if client["tipo"] == "Casa":

        if "metrosmin" not in client:
            user = update.message.from_user

            keyboard = [["0","30","40","50","60"],
                        ["80","100","150","200","300"],
                        ["400","Otra","Atrás","Salir"]]

            reply_markup = ReplyKeyboardMarkup(keyboard,
                                               one_time_keyboard=True,
                                               resize_keyboard=True)

            pm.logger.info("{} está en seleccionando superficie mínima.".format(user.first_name))
            update.message.reply_text("Seleccionar superficie construida mínima (en m2)", reply_markup=reply_markup)
            return pm.SELECT_AREA_RANGE

        elif client["metrosmin"]=="Otra":
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando superficie mínima.".format(user.first_name))
            update.message.reply_text("Ingresar superficie construida mínima (en m2)")

        elif "metrosmax" not in client:
            user = update.message.from_user

            x=int(client["metrosmin"])

            keyboard = [[str(x+10),str(x+20),str(x+30),str(x+40),str(x+50),str(x+70)],
                        [str(x+100),str(x+200),str(x+300),"Otra","Atrás","Salir"]]

            reply_markup = ReplyKeyboardMarkup(keyboard,
                                               one_time_keyboard=True,
                                               resize_keyboard=True)

            pm.logger.info("{} está en seleccionando superficie mínima.".format(user.first_name))
            update.message.reply_text("Seleccionar superficie construida máxima (en m2)", reply_markup=reply_markup)
            return pm.SELECT_AREA_RANGE

        elif client["metrosmax"]=="Otra":
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando superficie máxima.".format(user.first_name))
            update.message.reply_text("Ingresar superficie construída máxima (en m2)")

        elif "totalmin" not in client:
            user = update.message.from_user


            keyboard = [["0","50","100","200","400"],
                        ["500","600","800","1000"],
                        ["2000","5000","Otra","Atrás","Salir"]]

            reply_markup = ReplyKeyboardMarkup(keyboard,
                                               one_time_keyboard=True,
                                               resize_keyboard=True)

            pm.logger.info("{} está en seleccionando superficie mínima.".format(user.first_name))
            update.message.reply_text("Seleccionar superficie terreno mínima (en m2)", reply_markup=reply_markup)
            return pm.SELECT_AREA_RANGE

        elif client["totalmin"]=="Otra":
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando superficie máxima.".format(user.first_name))
            update.message.reply_text("Ingresar superficie terreno mínima (en m2)")

        elif "totalmax" not in client:
            user = update.message.from_user

            x=client["totalmin"]

            keyboard = [[str(x+20),str(x+50),str(x+100),str(x+200),str(x+500)],
                        [str(x+1000),str(x+2000),str(x+5000),str(x+10000)],
                        ["Otra","Atrás","Salir"]]

            reply_markup = ReplyKeyboardMarkup(keyboard,
                                               one_time_keyboard=True,
                                               resize_keyboard=True)

            pm.logger.info("{} está en seleccionando superficie mínima.".format(user.first_name))
            update.message.reply_text("Seleccionar superficie terreno máxima (en m2)", reply_markup=reply_markup)
            return pm.SELECT_AREA_RANGE

        elif client["totalmax"]=="Otra":
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando superficie máxima.".format(user.first_name))
            update.message.reply_text("Ingresar superficie terreno máxima (en m2)")



    return pm.SELECT_AREA_RANGE

def confirm_report(bot,update,client):

    user = update.message.from_user


    if client["reportepro"]:
        probutton="Quitar"
        protext="Si"
    else:
        probutton="Agregar"
        protext = "No"
    if client["reporteinterno"]:
        internabutton="Quitar"
        internatext="Si"
    else:
        internabutton="Agregar"
        internatext="No"
    if client["reportemetro"]:
        metrobutton="Quitar"
        metrotext="Si"
    else:
        metrobutton="Agregar"
        metrotext="No"

    keyboard = [["SI","Modificar"],
                [probutton+" Tasación"],
                [internabutton+" Contacto Publicación"],
                [metrobutton+" Distancia al metro"],
                ["Atrás", "Salir"]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)


    pm.logger.info("{} está confirmando reporte.".format(user.first_name))
    confirmtext=[]
    confirmtext.append("Generar reporte para las siguientes características:")
    confirmtext.append("Operación: "+client["operacion"])
    confirmtext.append("Región: "+client["region"])
    confirmtext.append("Comuna: "+client["comuna"])
    confirmtext.append("Tipo: "+client["tipo"])
    if client["tipo"]=="Departamento" or client["tipo"]=="Departamento":
        confirmtext.append("Dormitorios: "+client["dormitorios"])
        confirmtext.append("Baños: "+client["baños"])
    elif client["tipo"]=="Oficina":
        confirmtext.append("Privados: "+client["dormitorios"])
        confirmtext.append("Baños: "+client["baños"])
    else:
        confirmtext.append("Baños: "+client["baños"])
    if client["moneda"]=="UF":
        confirmtext.append("Desde: "+client["moneda"]+" "'{:,}'.format(client["preciomin"]).replace(",",".")+", Hasta: "+client["moneda"]+" "+'{:,}'.format(client["preciomax"]).replace(",","."))
    else:
        confirmtext.append("Desde: $ "+'{:,}'.format(client["preciomin"]).replace(",",".")+", Hasta: $ "+'{:,}'.format(client["preciomax"]).replace(",","."))
    if client["tipo"]=="Departamento":
        confirmtext.append("Desde: "+str(client["metrosmin"])+"m2 útiles, Hasta: "+str(client["metrosmax"])+"m2 útiles")
        confirmtext.append("Desde: "+str(client["totalmin"])+"m2 totales, Hasta: "+str(client["totalmax"])+"m2 totales")
    if client["tipo"]=="Casa":
        confirmtext.append("Desde: "+str(client["metrosmin"])+"m2 construidos, Hasta: "+str(client["metrosmax"])+"m2 construidos")
        confirmtext.append("Desde: "+str(client["totalmin"])+"m2 de terreno, Hasta: "+str(client["totalmax"])+"m2 de terreno")
    confirmtext.append("El Reporte solicitado "+protext+" Incluye Tasación")
    confirmtext.append("El Reporte solicitado "+internatext+" Incluye Datos de contacto de Publicación")
    confirmtext.append("El Reporte solicitado "+metrotext+" Incluye distancia a estación de metro más cercana")



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

##### FUNCIONES DEL TASADOR

def feature(bot,update,client):

    user = update.message.from_user


    keyboard = [["0","1","2","3+"],
                ["Atrás", "Salir"]]


    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)

    if "estacionamientos" not in client:
        pm.logger.info("{} está seleccionando Estacionamientos.".format(user.first_name))
        update.message.reply_text("Seleccionar Número de Estacionamientos", reply_markup=reply_markup)
    else:
        pm.logger.info("{} está seleccionando Bodegas.".format(user.first_name))
        update.message.reply_text("Seleccionar Número de Bodegas", reply_markup=reply_markup)

    return pm.SELECT_FEATURE

def area(bot, update,client):
    global STATE
    """
    Main menu function.
    This will display the options from the main menu.
    """
    # Create buttons to slect language:
    user = update.message.from_user
    print("entro al select de arearange")
    print("esta en tipo: " + client["tipo"])

    if client["tipo"] == "Departamento" or client["tipo"] == "Oficina" or client["tipo"] == "Comercial":

        if "metros" not in client:
            user = update.message.from_user

            keyboard = [["0","20","30","40","50","60","70","80"],
                        ["100","150","200","Otra","Atrás","Salir"]]

            reply_markup = ReplyKeyboardMarkup(keyboard,
                                               one_time_keyboard=True,
                                               resize_keyboard=True)

            pm.logger.info("{} está en seleccionando superficie mínima.".format(user.first_name))
            update.message.reply_text("Seleccionar superficie útil (en m2)", reply_markup=reply_markup)
            return pm.SELECT_AREA

        elif client["metros"]=="Otra":
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando superficie mínima.".format(user.first_name))
            update.message.reply_text("Ingresar superficie útil (en m2)")
            return pm.SELECT_AREA


        elif "total" not in client:
            user = update.message.from_user

            x=int(client["metros"])

            keyboard = [[str(x+0),str(x+2),str(x+5),str(x+7),str(x+10),str(x+15),str(x+20)],
                        [str(x+30),str(x+50),"Otra","Atrás","Salir"]]

            reply_markup = ReplyKeyboardMarkup(keyboard,
                                               one_time_keyboard=True,
                                               resize_keyboard=True)

            pm.logger.info("{} está en seleccionando superficie maxima.".format(user.first_name))
            update.message.reply_text("Seleccionar superficie total (en m2)", reply_markup=reply_markup)
            return pm.SELECT_AREA


        elif client["totalmax"]=="Otra":
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando superficie máxima.".format(user.first_name))
            update.message.reply_text("Ingresar superficie total (en m2)")
            return pm.SELECT_AREA

    if client["tipo"] == "Casa":

        if "metros" not in client:
            user = update.message.from_user

            keyboard = [["0","30","40","50","60","80","100","150"],
                        ["200","300","400","Otra","Atrás","Salir"]]

            reply_markup = ReplyKeyboardMarkup(keyboard,
                                               one_time_keyboard=True,
                                               resize_keyboard=True)

            pm.logger.info("{} está en seleccionando superficie mínima.".format(user.first_name))
            update.message.reply_text("Seleccionar superficie construida (en m2)", reply_markup=reply_markup)
            return pm.SELECT_AREA

        elif client["metros"]=="Otra":
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando superficie mínima.".format(user.first_name))
            update.message.reply_text("Ingresar superficie construida (en m2)")

        elif "total" not in client:
            user = update.message.from_user


            keyboard = [["0","50","100","200","400","500","600","800"],
                        ["1000","2000","5000","Otra","Atrás","Salir"]]

            reply_markup = ReplyKeyboardMarkup(keyboard,
                                               one_time_keyboard=True,
                                               resize_keyboard=True)

            pm.logger.info("{} está en seleccionando superficie mínima.".format(user.first_name))
            update.message.reply_text("Seleccionar superficie terreno (en m2)", reply_markup=reply_markup)
            return pm.SELECT_AREA

        elif client["total"]=="Otra":
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando superficie máxima.".format(user.first_name))
            update.message.reply_text("Ingresar superficie terreno (en m2)")
            return pm.SELECT_AREA

def adress(bot, update,client):
    global STATE
    """
    Main menu function.
    This will display the options from the main menu.
    """

    user = update.message.from_user
    pm.logger.info("{} está escogiendo direccion.".format(user.first_name))
    update.message.reply_text("Ingrese la dirección de la propiedad, sin comuna ni región")
    return pm.SELECT_ADRESS

def confirm_tasacion(bot, update,client):
    user = update.message.from_user

    keyboard = [["Confirmar","Modificar"],
                ["Atrás", "Salir"]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)
    print("creo el teclado")

    pm.logger.info("{} está confirmando tasacion.".format(user.first_name))
    confirmtext=[]
    confirmtext.append("Tasar Propiedad con las siguientes características:")
    confirmtext.append("Operación: "+client["operacion"])
    confirmtext.append("Región: "+client["region"])
    confirmtext.append("Comuna: "+client["comuna"])
    confirmtext.append("Tipo: "+client["tipo"])
    if client["tipo"]=="Departamento" or client["tipo"]=="Departamento":
        confirmtext.append("Dormitorios: "+client["dormitorios"])
        confirmtext.append("Baños: "+client["baños"])
    elif client["tipo"]=="Oficina":
        confirmtext.append("Privados: "+client["dormitorios"])
        confirmtext.append("Baños: "+client["baños"])
    else:
        confirmtext.append("Baños: "+client["baños"])
    confirmtext.append("Estacionamientos: "+client["estacionamientos"])
    if client["tipo"]=="Departamento":
        confirmtext.append("Bodegas: "+client["bodegas"])
    if client["tipo"]=="Departamento" or client["tipo"]=="Oficina" or client["tipo"]=="Comercial":
        confirmtext.append("Superficie: "+str(client["metros"])+"m2 útiles")
        confirmtext.append("Superficie: "+str(client["total"])+"m2 totales")
    if client["tipo"]=="Casa":
        confirmtext.append("Superficie: "+str(client["metros"])+"m2 construidos")
        confirmtext.append("Superficie: "+str(client["total"])+"m2 de terreno")
    confirmtext.append("Dirección: "+client["adress"])


    confirmtext="\n".join(confirmtext)
    print(confirmtext)
    update.message.reply_text(confirmtext, reply_markup=reply_markup,disable_web_page_preview=True)

    return pm.CONFIRM_TASACION
