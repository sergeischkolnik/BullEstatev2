from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler
from telegram.ext import ConversationHandler, CallbackQueryHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import logging

telegram_token = "666842820:AAGg1F_NjlQBL7IPv9XlfMEC0PJ6iWlVLj0"

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)

# Global vars:

MENU, SELECT_OP, SELECT_REGION, SELECT_COMUNA = range(4)
STATE = MENU

vars_us = dict()
comunas = {
  "RM": ["Las Condes","Providencia","Santiago","Vitacura"],
  "Valpo": ["Viña","Valpo"],
  "Otros": ["Otros"]
}


def start(bot, update):
    """
    Start function. Displayed whenever the /start command is called.
    This function sets the language of the bot.
    """

    user = update.message.from_user
    if user.id not in vars_us:
        vars_us[user.id] = dict()


    menu(bot, update)
    return MENU

def menu(bot, update):
    global STATE
    print(STATE)
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
    logger.info("{} está en el menu principal.".format(user.first_name))
    update.message.reply_text("menu principal", reply_markup=reply_markup)


    STATE = MENU
    return MENU

def select_region(bot, update):
    """
    Main menu function.
    This will display the options from the main menu.
    """
    # Create buttons to slect language:
    keyboard = [["RM","Valpo"],
                ["Atras", "Salir"]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)

    user = update.message.from_user
    logger.info("{} está seleccionando region.".format(user.first_name))
    update.message.reply_text("Seleccionar region", reply_markup=reply_markup)

    return SELECT_REGION

def select_comuna(bot,update):
    user = update.message.from_user
    reg = vars_us[user.id]["Region"]
    lista_comunas = comunas[reg]


    keyboard = [lista_comunas,
                ["Atras", "Salir"]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)


    logger.info("{} está seleccionando region.".format(user.first_name))
    update.message.reply_text("Seleccionar region", reply_markup=reply_markup)

def set_state(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE
    user = update.message.from_user
    if update.message.text == "Reporte":
        STATE = SELECT_OP
        report(bot, update)
        return SELECT_OP
    elif update.message.text == "Ficha":
        faq(bot, update)
        menu(bot, update)
        return MENU
    elif update.message.text == "Ayuda":
        about_bot(bot, update)
        menu(bot, update)
        return MENU
    else:
        STATE = MENU
        return MENU

def set_operacion(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE
    user = update.message.from_user
    if update.message.text == "Comprar":
        STATE = SELECT_REGION
        vars_us[user.id]["OP"] = "Comprar"
        select_region(bot,update)
        return SELECT_REGION
    elif update.message.text == "Arrendar":
        STATE = SELECT_REGION
        vars_us[user.id]["OP"] = "Arrendar"
        select_region(bot, update)
        return SELECT_REGION
    elif update.message.text == "Atras":
        STATE = MENU
        menu(bot, update)
        return MENU
    elif update.message.text == "Salir":
        menu(bot, update)
        return MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        report(bot, update)
        STATE = SELECT_OP
        return SELECT_OP


def set_region(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE
    user = update.message.from_user
    if update.message.text == "RM":
        STATE = SELECT_COMUNA
        vars_us[user.id]["Region"] = "RM"
        select_comuna(bot,update)
        return MENU
    elif update.message.text == "Valpo":
        STATE = SELECT_COMUNA
        vars_us[user.id]["Region"] = "Valpo"
        select_comuna(bot, update)
        return MENU
    elif update.message.text == "Atras":
        STATE = SELECT_OP
        report(bot, update)
        return SELECT_OP
    elif update.message.text == "Salir":
        menu(bot, update)
        return MENU
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Comando invalido, presione algun boton.")
        set_region(bot, update)
        STATE = SELECT_REGION
        return SELECT_REGION

def report(bot, update):

    user = update.message.from_user
    logger.info("Report requested by {}.".format(user.first_name))

    keyboard = [["Comprar","Arrendar"],
                ["Atras", "Salir"]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)

    user = update.message.from_user
    logger.info("{} está eligigiendo operacion.".format(user.first_name))
    update.message.reply_text("Seleccione operacion", reply_markup=reply_markup)

    return SELECT_OP



def about_bot(bot, update):
    """
    About function. Displays info about DisAtBot.
    """
    user = update.message.from_user
    logger.info("About info requested by {}.".format(user.first_name))
    bot.send_message(chat_id=update.message.chat_id, text="acerca de ...")
    bot.send_message(chat_id=update.message.chat_id, text="volviendo a menu")
    return


def help(bot, update):
    """
    Help function.
    This displays a set of commands available for the bot.
    """
    user = update.message.from_user
    logger.info("User {} asked for help.".format(user.first_name))
    update.message.reply_text("texto de ayuda",
                              reply_markup=ReplyKeyboardRemove())


def cancel(bot, update):
    """
    User cancelation function.
    Cancel conersation by user.
    """
    user = update.message.from_user
    logger.info("User {} canceled the conversation.".format(user.first_name))
    update.message.reply_text("mensaje adiuos",
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """
    Main function.
    This function handles the conversation flow by setting
    states on each step of the flow. Each state has its own
    handler for the interaction with the user.
    """

    # Create the EventHandler and pass it your bot's token.
    updater = Updater(telegram_token)

    # Get the dispatcher to register handlers:
    dp = updater.dispatcher

    # Add conversation handler with predefined states:
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={

            MENU: [RegexHandler(
                        '^({}|{}|{})$'.format("Reporte", "Ficha", "Ayuda"),set_state)],

            SELECT_OP: [RegexHandler(
                        '^({}|{}|{}|{})$'.format("Comprar", "Arrendar", "Atras", "Salir"),set_operacion)],

            SELECT_REGION: [RegexHandler(
                '^({}|{}|{}|{})$'.format("RM", "Valpo", "Atras", "Salir"), set_region)],

            SELECT_COMUNA: [RegexHandler(
                '^(*)$'.format("RM", "Valpo", "Atras", "Salir"), set_region)]


        },

        fallbacks=[CommandHandler('cancel', cancel),
                   CommandHandler('help', help)]
    )

    dp.add_handler(conv_handler)

    # Log all errors:
    dp.add_error_handler(error)

    # Start DisAtBot:
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process
    # receives SIGINT, SIGTERM or SIGABRT:
    updater.idle()


if __name__ == '__main__':
    main()