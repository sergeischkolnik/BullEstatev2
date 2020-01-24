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
                ["Ficha","Historial"],
                ["Props. Cerca", "CRM"]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)



    user = update.message.from_user
    pm.logger.info("{} está en el menu principal.".format(user.first_name))
    update.message.reply_text("Menu Principal", reply_markup=reply_markup)
    return pm.MENU

def last(bot, update):

    user = update.message.from_user
    pm.logger.info("Report requested by {}.".format(user.first_name))

    keyboard = [["Reporte","Tasador"],
                ["Ficha", "Atrás"]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)

    user = update.message.from_user
    pm.logger.info("{} está eligiendo operacion del historial.".format(user.first_name))
    update.message.reply_text("Seleccione operacion realizada", reply_markup=reply_markup)

    return pm.SELECT_LAST

def callback(bot,update,client):
    if "modify" in client:
        print("Calback activated. Modify Variable is: "+str(client["modify"]))
        if client["modify"]:
            client.pop("modify")
            print("Variable modify was eliminated")
            if client["product"]=="Reporte":
                confirm_report(bot,update,client)
                return pm.CONFIRM_REPORT
            elif client["product"]=="Tasador":
                confirm_tasacion(bot,update,client)
                return pm.CONFIRM_TASACION
            elif client["product"]=="CRM" and client["crm"]=="Buscar":
                confirm_report(bot,update,client)
                return pm.CONFIRM_REPORT
            elif client["product"]=="CRM" and client["crm"]=="Nueva":
                confirm_tasacion(bot,update,client)
                return pm.CONFIRM_TASACION
            elif client["product"]=="CRM" and client["crm"]=="Lista Completa":
                crm_feature(bot,update,client)
                return pm.CRM_FEATURE
        else:
            client["modify"]=True
            print("Variable modify was switched from False to True")
            return
    else:
        return
##### FUNCIONES DEL REPORTE

def operacion(bot, update,client):

    if "modify" in client:
        callback(bot,update,client)

    user = update.message.from_user
    pm.logger.info("Report requested by {}.".format(user.first_name))

    if client["product"]=="Reporte":
        keyboard = [["Comprar","Arrendar"],
                    ["Atrás", "Salir"]]
    elif client["product"]=="CRM":
        keyboard = [["Venta","Arriendo"],
                    ["Atrás", "Salir"]]
    else:
        keyboard = [["Simple","Full"],
                    ["Atrás", "Salir"]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)

    user = update.message.from_user
    pm.logger.info("{} está eligiendo operacion.".format(user.first_name))
    if client["product"] == "Reporte":
        update.message.reply_text("Seleccione operacion", reply_markup=reply_markup)
    elif client["product"] == "CRM":
        update.message.reply_text("Seleccione operacion", reply_markup=reply_markup)
    else:
        update.message.reply_text("Seleccione tipo de tasación", reply_markup=reply_markup)

    return pm.SELECT_OP

def region(bot, update,client):

    if "modify" in client:
        callback(bot,update,client)
        return

    """
    Main menu function.
    This will display the options from the main menu.
    """
    user = update.message.from_user
    # Create buttons to slect language:
    if "region" not in client:

        keyboard = [["Metropolitana","Valparaiso"],
                    ["Biobio","Coquimbo"],
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
    if "modify" in client:
        callback(bot,update,client)

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

def tipo(bot,update,client):
    if "modify" in client:
        callback(bot,update,client)

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

    if "modify" in client:
        callback(bot,update,client)

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

    if "modify" in client:
        callback(bot,update,client)
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

    if "modify" in client:
        callback(bot,update,client)

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
    elif "preciomin" not in client and client["product"]=="CRM" and client["crm"]=="Nueva":
        user = update.message.from_user
        pm.logger.info("{} está en seleccionando precio.".format(user.first_name))
        update.message.reply_text("Ingresar precio")
        return pm.SELECT_PRICE_RANGE
    elif "preciomin" not in client:
        if client["moneda"]=="UF":
            user = update.message.from_user
            if client["operacion"]=="Arrendar":
                keyboard = [["0","5","10","15","20","25","50"],
                            ["Otro","Default","Atrás","Salir"]]

            else:
                keyboard = [["0","1.000","2.000","3.000"],
                            ["4.000","5.000","7.000","10.000"],
                            ["Otro","Default","Atrás","Salir"]]

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
                            ["75.000.000","100.000.000","200.000.000"],
                            ["Otro","Default","Atrás","Salir"]]

            else:
                keyboard = [["0","150.000","200.000"],
                            ["300.000","500.000","1.000.000"],
                            ["Otro","Default","Atrás","Salir"]]

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
            if client["operacion"]=="Arrendar":
               keyboard = [['{:,}'.format(x+2).replace(",","."),'{:,}'.format(x+5).replace(",","."),'{:,}'.format(x+10).replace(",",".")],
                            ['{:,}'.format(x+15).replace(",","."),'{:,}'.format(x+20).replace(",","."),'{:,}'.format(x+50).replace(",",".")],
                            ['{:,}'.format(x+100).replace(",","."),"Otro","Atrás","Salir"]]
            else:
                keyboard = [['{:,}'.format(x+500).replace(",","."),'{:,}'.format(x+1000).replace(",","."),'{:,}'.format(x+2000).replace(",",".")],
                            ['{:,}'.format(x+3000).replace(",","."),'{:,}'.format(x+5000).replace(",","."),'{:,}'.format(x+10000).replace(",",".")],
                            ['{:,}'.format(x+200000).replace(",","."),"Otro","Atrás","Salir"]]

            reply_markup = ReplyKeyboardMarkup(keyboard,
                                               one_time_keyboard=True,
                                               resize_keyboard=True)

            pm.logger.info("{} está seleccionando moneda.".format(user.first_name))
            update.message.reply_text("Seleccionar Precio Máximo en UF", reply_markup=reply_markup)
            return pm.SELECT_PRICE_RANGE
        else:
            user = update.message.from_user
            x=client["preciomin"]
            if client["operacion"]=="Arrendar":
                keyboard = [['{:,}'.format(x+50000).replace(",","."),'{:,}'.format(x+100000).replace(",",".")],
                            ['{:,}'.format(x+200000).replace(",","."),'{:,}'.format(x+500000).replace(",",".")],
                            ['{:,}'.format(x+1000000).replace(",","."),"Otro","Atrás","Salir"]]

            else:
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
    if "modify" in client:
        callback(bot,update,client)
    user = update.message.from_user
    print("entro al select de arearange")
    print("esta en tipo: " + client["tipo"])

    if client["tipo"] == "Departamento" or client["tipo"] == "Oficina" or client["tipo"] == "Comercial":

        if "metrosmin" not in client:
            user = update.message.from_user

            keyboard = [["0","20","30","40","50","75","100","150"],
                        ["200","Otra","Default","Atrás","Salir"]]

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

            pm.logger.info("{} está en seleccionando superficie máxima.".format(user.first_name))
            if client["tipo"] == "Comercial":
                update.message.reply_text("Seleccionar superficie máxima (en m2)", reply_markup=reply_markup)
                return pm.SELECT_AREA_RANGE
            else:
                update.message.reply_text("Seleccionar superficie útil máxima (en m2)", reply_markup=reply_markup)
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
                ["Atrás","Avanzado","Salir"]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)


    pm.logger.info("{} está confirmando reporte.".format(user.first_name))
    confirmtext=[]
    if client["product"]=="CRM" and client["crm"]=="Buscar":
        confirmtext.append("Generar búsqueda para las siguientes características:")
    else:
        confirmtext.append("Generar reporte para las siguientes características:")
    confirmtext.append("Operación: "+client["operacion"])
    confirmtext.append("Región: "+client["region"])
    if type(client["comuna"]) is list:
        comunas=""
        for comuna in client["comuna"]:
            comunas+=str(comuna)+" - "
        comunas=comunas[:-3]
        confirmtext.append("Comunas: " + comunas)
    else:
        confirmtext.append("Comuna: "+client["comuna"])
    confirmtext.append("Tipo: "+client["tipo"])
    if client["tipo"]=="Departamento":
        if "DormMin" in client and "DormMax" in client:
            confirmtext.append("Dormitorios: " + str(client["DormMin"])+" - "+str(client["DormMax"]))
        elif "dormitorios" in client:
            confirmtext.append("Dormitorios: "+client["dormitorios"])
        else:
            pass
        if "BathMin" in client and "BathMax" in client:
            confirmtext.append("Baños: " + str(client["BathMin"])+" - "+str(client["BathMax"]))
        else:
            confirmtext.append("Baños: "+client["baños"])

    elif client["tipo"]=="Oficina":
        if "DormMin" in client and "DormMax" in client:
            confirmtext.append("Privados: " + str(client["DormMin"]) + " - " + str(client["DormMax"]))
        else:
            confirmtext.append("Privados: " + client["dormitorios"])
        if "BathMin" in client and "BathMax" in client:
            confirmtext.append("Baños: " + str(client["BathMin"]) + " - " + str(client["BathMax"]))
        else:
            confirmtext.append("Baños: " + client["baños"])
    else:
        if "DormMin" in client and "DormMax" in client:
            confirmtext.append("Dormitorios: " + str(client["DormMin"]) + " - " + str(client["DormMax"]))
        elif "dormitorios" in client:
            confirmtext.append("Dormitorios: "+client["dormitorios"])
        else:
            pass
        if "BathMin" in client and "BathMax" in client:
            confirmtext.append("Baños: " + str(client["BathMin"]) + " - " + str(client["BathMax"]))
        else:
            confirmtext.append("Baños: " + client["baños"])

    if client["preciomin"] is not None:
        if client["moneda"]=="UF":
            confirmtext.append("Desde: "+client["moneda"]+" "'{:,}'.format(client["preciomin"]).replace(",",".")+", Hasta: "+client["moneda"]+" "+'{:,}'.format(client["preciomax"]).replace(",","."))
        else:
            confirmtext.append("Desde: $ "+'{:,}'.format(client["preciomin"]).replace(",",".")+", Hasta: $ "+'{:,}'.format(client["preciomax"]).replace(",","."))
    if client["metrosmin"] is not None:
        if client["tipo"]=="Departamento":
            confirmtext.append("Desde: "+str(client["metrosmin"])+"m2 útiles, Hasta: "+str(client["metrosmax"])+"m2 útiles")
            confirmtext.append("Desde: "+str(client["totalmin"])+"m2 totales, Hasta: "+str(client["totalmax"])+"m2 totales")
        if client["tipo"]=="Casa":
            confirmtext.append("Desde: "+str(client["metrosmin"])+"m2 construidos, Hasta: "+str(client["metrosmax"])+"m2 construidos")
            confirmtext.append("Desde: "+str(client["totalmin"])+"m2 de terreno, Hasta: "+str(client["totalmax"])+"m2 de terreno")
    if "Center" in client and "Radius" in client:
        confirmtext.append("Buscando propiedades a un máximo de " + str(client["Radius"]) + " de la dirección: "+ client["Center"] )

    if client["product"]=="CRM" and client["crm"]=="Buscar":
        confirmtext.append("La Búsqueda solicitada "+protext+" Incluye Tasación")
        confirmtext.append("La Búsqueda solicitada "+internatext+" Incluye Datos de contacto de Publicación")
        confirmtext.append("La Búsqueda solicitada "+metrotext+" Incluye distancia a estación de metro más cercana")
    else:
        confirmtext.append("El Reporte solicitado "+protext+" Incluye Tasación")
        confirmtext.append("El Reporte solicitado "+internatext+" Incluye Datos de contacto de Publicación")
        confirmtext.append("El Reporte solicitado "+metrotext+" Incluye distancia a estación de metro más cercana")


    confirmtext="\n".join(confirmtext)
    print(confirmtext)
    update.message.reply_text(confirmtext, reply_markup=reply_markup)

    return pm.CONFIRM_REPORT

def advance(bot,update,client):

    if client["DormRange"] is True:
        if "DormMin" not in client:
            user = update.message.from_user
            pm.logger.info("{} está seleccionando Rango de Dormitorios.".format(user.first_name))
            if client["tipo"] == "Oficina":
                update.message.reply_text("Ingresar Privados máximos")
            else:
                update.message.reply_text("Ingresar Dormitorios mínimos")
        else:
            user = update.message.from_user
            pm.logger.info("{} está seleccionando Rango de Dormitorios.".format(user.first_name))
            if client["tipo"] == "Oficina":
                update.message.reply_text("Ingresar Privados máximos")
            else:
                update.message.reply_text("Ingresar Dormitorios máximos")

    elif client["BathRange"] is True:
        if "BathMin" not in client:
            user = update.message.from_user
            pm.logger.info("{} está seleccionando Rango de Baños.".format(user.first_name))
            update.message.reply_text("Ingresar Baños mínimos")
        else:
            user = update.message.from_user
            pm.logger.info("{} está seleccionando Rango de Baños.".format(user.first_name))
            update.message.reply_text("Ingresar Baños máximos")

    elif client["Adress"] is True:
        if "Center" not in client:
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando Direccion.".format(user.first_name))
            update.message.reply_text("Ingresar Direccion de Busqueda")
        else:
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando Radio.".format(user.first_name))
            update.message.reply_text("Ingresar Radio de Búsqueda (en metros)")

    elif client["OtraComuna"] is True:
        user = update.message.from_user
        pm.logger.info("{} está en seleccionando otra comuna.".format(user.first_name))
        update.message.reply_text("Ingresar Comuna que desea agregar")

    else:
        user = update.message.from_user
        if client["tipo"]=="Oficina":
            rango="Rango Privados"
        else:
            rango="Rango Dormitorios"
        keyboard = [[rango],
                ["Rango Baños"],
                ["Buscar por dirección"],
                ["Agregar Comuna"],
                ["Confirmar","Atrás","Salir"]]


        reply_markup = ReplyKeyboardMarkup(keyboard,
                                           one_time_keyboard=True,
                                           resize_keyboard=True)

        pm.logger.info("{} está opciones avanzadas.".format(user.first_name))
        update.message.reply_text("Seleccionar Opción", reply_markup=reply_markup)

    return pm.ADVANCE

def modify(bot, update,client):
    user = update.message.from_user
    if client["product"]=="Reporte":
        keyboard = [["Operacion","Tipo"],
                    ["Región","Comuna"],
                    ["Dormitorios","Baños"],
                    ["Precio","Superficie"],
                    ["Atrás","Salir"]]
    elif client["product"]=="Tasador":
        keyboard = [["Tipo Tasacion","Tipo Propiedad"],
                    ["Región","Comuna"],
                    ["Dormitorios","Baños"],
                    ["Estacionamientos","Bodegas"],
                    ["Superficie","Direccion"],
                    ["Atrás","Salir"]]
    elif client["product"]=="Ficha":
        #Back to beggining product
        pass
    elif client["product"]=="CRM" and client["crm"]=="Buscar":
        keyboard = [["Operacion","Tipo"],
                    ["Región","Comuna"],
                    ["Dormitorios","Baños"],
                    ["Superficie","Precio"],
                    ["Atrás","Salir"]]

    elif client["product"]=="CRM" and client["crm"]=="Nueva":
        keyboard = [["Operacion","Región","Comuna"],
                    ["Tipo","Dormitorios","Baños"],
                    ["Estacionamientos","Bodegas"],
                    ["Superficie","Precio","Direccion"],
                    ["Datos Cliente","Link","Condiciones"],
                    ["Atrás","Salir"]]
    elif client["product"]=="CRM" and client["crm"]=="Lista Completa":
        keyboard = [["Operacion","Tipo"],
                    ["Region","Comuna"],
                    ["Atrás","Salir"]]
    elif client["product"]=="CRM" and (client["crm"]=="Actualizar" or client["crm"]=="Eliminar"):
        #Back to begin
        pass
    else:
        pass
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                           one_time_keyboard=True,
                                           resize_keyboard=True)
    pm.logger.info("{} está modificando.".format(user.first_name))
    update.message.reply_text("Seleccionar Opción que desee modificar", reply_markup=reply_markup)

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

    if client["product"]=="CRM":
        keyboard = [["Confirmar","Modificar"],
                    ["Atrás", "Salir"]]
    else:
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
    if client["product"]=="CRM":
        confirmtext.append(str(client["crm"])+" la siguiente propiedad:")
        #cargar datos propiedad
        if "id_prop" in client:
            confirmtext.append("ID Propiedad:"+str(client["id_prop"]))
            confirmtext.append("Sitio de origen:"+client["sitio"])
        else:
            confirmtext.append("URL Propiedad:" + str(client["link_prop"]))
    else:
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

    if "modify" in client:
        callback(bot,update,client)

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
    if "modify" in client:
        callback(bot,update,client)
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

    if "modify" in client:
        callback(bot,update,client)

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
    if client["product"]=="CRM":
        confirmtext.append("Ignresar Propiedad al CRM con las siguientes características:")
        confirmtext.append("Tipo de Propiedad: "+client["tipotasacion"])
    else:
        confirmtext.append("Tasar Propiedad con las siguientes características:")
        confirmtext.append("Tipo de Tasacion: "+client["tipotasacion"])
    confirmtext.append("Región: "+client["region"])
    confirmtext.append("Comuna: "+client["comuna"])
    confirmtext.append("Tipo: "+client["tipo"])
    if client["tipo"]=="Departamento" or client["tipo"]=="Casa":
        confirmtext.append("Dormitorios: "+client["dormitorios"])
        confirmtext.append("Baños: "+client["baños"])
    elif client["tipo"]=="Oficina":
        confirmtext.append("Privados: "+client["dormitorios"])
        confirmtext.append("Baños: "+client["baños"])
    else:
        confirmtext.append("Baños: "+client["baños"])
    if client["tipo"]!="Comercial":
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
    if client["product"]=="CRM":
        if client["moneda"]=="UF":
            confirmtext.append("Precio: "+client["moneda"]+" "'{:,}'.format(client["preciomin"]).replace(",","."))
        else:
            confirmtext.append("Precio: $ "+'{:,}'.format(client["preciomin"]).replace(",","."))
        confirmtext.append("Telefono Cliente: "+client["estacionamientos"])
        confirmtext.append("Mail Cliente: "+client["estacionamientos"])
        confirmtext.append("Link Portalinmmobiliario: "+client["estacionamientos"])
        confirmtext.append("Link Yapo: "+client["estacionamientos"])
        confirmtext.append("Comision: "+client["estacionamientos"])
        confirmtext.append("¿Es Canje?: "+client["estacionamientos"])


    confirmtext="\n".join(confirmtext)
    print(confirmtext)
    update.message.reply_text(confirmtext, reply_markup=reply_markup,disable_web_page_preview=True)

    return pm.CONFIRM_TASACION

##### MODIFICAR

def modificar(bot,update,client):

    user = update.message.from_user

    if client["producto"]=="Reporte":

        keyboard = [["Operacion","Region","Comuna"],
                    ["Tipo","Dormitorios","Baños"],
                    ["Precio","Superficie"],
                    ["Atrás", "Salir"]]

    elif client["producto"]=="Tasación":

        keyboard = [["Operacion","Region","Comuna"],
                    ["Tipo","Dormitorios","Baños"],
                    ["Estacionamientos","Bodegas"],
                    ["Sup. Útil","Sup. Total","Dirección"],
                    ["Atrás", "Salir"]]

    elif client["producto"]=="Ficha":

        keyboard = [["Sitio","ID","URL"],
                    ["Atrás", "Salir"]]


    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)

    pm.logger.info("{} está Modificando.".format(user.first_name))
    update.message.reply_text("Seleccionar Atributo que desea modificar", reply_markup=reply_markup)

    return pm.SELECT_FEATURE

##### CRM

def crm(bot, update):

    user = update.message.from_user
    pm.logger.info("Report requested by {}.".format(user.first_name))


    keyboard = [["Buscar","Lista Completa"],
                ["Nueva","Actualizar"],
                ["Eliminar", "Salir"]]


    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)

    user = update.message.from_user
    pm.logger.info("{} está eligiendo operacion del CRM.".format(user.first_name))
    update.message.reply_text("Seleccione acción a realizar", reply_markup=reply_markup)


    return pm.CRM

def crm_feature(bot, update,client):
    if "modify" in client:
        callback(bot,update,client)
    if client["crm"]=="Nueva":
        if "telefono" not in client:
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando telefono.".format(user.first_name))
            update.message.reply_text("Ingresar teléfono")
            return pm.CRM_FEATURE
        elif "mailcliente" not in client:
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando mail cliente.".format(user.first_name))
            update.message.reply_text("Ingresar Mail Cliente")
            return pm.CRM_FEATURE
        elif "linkPortal" not in client:
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando linkPortal.".format(user.first_name))
            update.message.reply_text("Ingresar link Portal Inmobiliario")
            return pm.CRM_FEATURE
        elif "linkYapo" not in client:
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando linkYapo.".format(user.first_name))
            update.message.reply_text("Ingresar link de Yapo.cl")
            return pm.CRM_FEATURE
        elif "comision" not in client:
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando comision.".format(user.first_name))
            update.message.reply_text("Ingresar Comisión")
            return pm.CRM_FEATURE
        elif "canje" not in client:
            user = update.message.from_user
            pm.logger.info("{} está en seleccionando canje.".format(user.first_name))
            update.message.reply_text("Ingresar Si/No es Canje")
            return pm.CRM_FEATURE
        else:
            update.message.reply_text("Error inesperado. Volviendo al Menu")
            return pm.MENU
    elif client["crm"]=="Lista Completa":
        user = update.message.from_user

        keyboard = [["Confirmar","Modificar"],
                    ["Atrás", "Salir"]]

        reply_markup = ReplyKeyboardMarkup(keyboard,
                                           one_time_keyboard=True,
                                           resize_keyboard=True)
        print("creo el teclado")

        pm.logger.info("{} está confirmando Lista con las siguientes características.".format(user.first_name))
        confirmtext=[]
        confirmtext.append("Obtener lista de propiedades con las siguientes caracteristicas:")
        confirmtext.append("Operación: "+client["tipotasacion"])
        confirmtext.append("Tipo de Propiedad: "+client["tipo"])
        confirmtext.append("Región: "+client["region"])
        confirmtext.append("Comuna: "+client["comuna"])
        confirmtext="\n".join(confirmtext)
        print(confirmtext)
        update.message.reply_text(confirmtext, reply_markup=reply_markup,disable_web_page_preview=True)

        return pm.CRM_FEATURE
