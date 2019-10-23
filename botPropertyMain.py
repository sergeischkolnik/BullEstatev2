from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler
from telegram.ext import ConversationHandler, CallbackQueryHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import logging
import botPropertySelect as select
import botPropertySet as set
import botPropertyDataBase as db
import pymysql as mysql
global id


def getToken():
    sql = "SELECT token FROM tokens WHERE nombre='tgbot'"
    mariadb_connection = mysql.connect(user='root', password='sergei', host='127.0.0.1', database='bullestate')
    cur = mariadb_connection.cursor()
    cur.execute(sql)
    elem = cur.fetchall()
    print(elem[0][0])

telegram_token = getToken()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)

# Global vars:

SIGNEDUP, FIRST, SIGNUP, LOGIN,MENU, SELECT_OP, SELECT_REGION, SELECT_COMUNA, SELECT_TIPO, SELECT_DORMS,SELECT_BATHS, \
SELECT_PRICE_RANGE, SELECT_AREA_RANGE,CONFIRM_REPORT,ADVANCE,SELECT_SITE,SELECT_ID,CONFIRM_FILE,SELECT_FEATURE,SELECT_AREA,\
SELECT_ADRESS,SELECT_LAST,CONFIRM_TASACION = range(23)

STATE = MENU





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
    update.message.reply_text("Conversación finalizada",
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():

    global keyword
    """
    Main function.
    This function handles the conversation flow by setting
    states on each step of the flow. Each state has its own
    handler for the interaction with the user.
    """
    print('Property Admin Bot is now Running')
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(telegram_token)

    # Get the dispatcher to register handlers:
    dp = updater.dispatcher

    # Add conversation handler with predefined states:
    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.text, set.start)],



        states={

            # # MENU: [RegexHandler(
            # #           '^({}|{}|{})$'.format("Reporte", "Ficha", "Ayuda"),set.menu)],
            #
            #
            #
            # SELECT_OP: [RegexHandler(
            #             '^({}|{}|{}|{})$'.format("Comprar", "Arrendar", "Atras", "Salir"),set.operacion)],
            #
            # SELECT_REGION: [RegexHandler(
            #             '^({}|{}|{}|{})$'.format("RM", "Valpo", "Atras", "Salir"), set.region)],
            #
            # SELECT_COM: [RegexHandler(
            #             '^({}|{}|{}|{})$'.format("Las Condes", "Providencia", "Atras", "Salir"), set.comuna)],
            #
            # SELECT_TIPO: [RegexHandler(
            #     '^({}|{}|{}|{})$'.format("Departamento", "Casa", "Atras", "Salir"), set.tipo)]
            #
            #      },

            SIGNEDUP: [MessageHandler(Filters.text, set.signedup)],

            FIRST: [MessageHandler(Filters.text, set.first)],

            SIGNUP: [MessageHandler(Filters.text, set.signup)],

            LOGIN: [MessageHandler(Filters.text, set.login)],

            MENU: [MessageHandler(Filters.text, set.menu)],

            #REPORT STATES:

            SELECT_OP:  [MessageHandler(Filters.text, set.operacion)],

            SELECT_REGION:  [MessageHandler(Filters.text, set.region)],

            SELECT_COMUNA:  [MessageHandler(Filters.text, set.comuna)],

            SELECT_TIPO:  [MessageHandler(Filters.text, set.tipo)],

            SELECT_DORMS: [MessageHandler(Filters.text, set.dorms)],

            SELECT_BATHS: [MessageHandler(Filters.text, set.baths)],

            SELECT_PRICE_RANGE: [MessageHandler(Filters.text, set.price_range)],

            SELECT_AREA_RANGE: [MessageHandler(Filters.text, set.area_range)],

            CONFIRM_REPORT: [MessageHandler(Filters.text, set.confirm_report)],

            ADVANCE: [MessageHandler(Filters.text, set.advance)],

            SELECT_SITE: [MessageHandler(Filters.text, set.site)],

            SELECT_ID: [MessageHandler(Filters.text, set.id_prop)],

            CONFIRM_FILE: [MessageHandler(Filters.text, set.confirm_file)],

            SELECT_FEATURE: [MessageHandler(Filters.text, set.feature)],

            SELECT_AREA: [MessageHandler(Filters.text, set.area)],

            SELECT_ADRESS: [MessageHandler(Filters.text, set.adress)],

            SELECT_LAST: [MessageHandler(Filters.text, set.last)],

            CONFIRM_TASACION: [MessageHandler(Filters.text, set.confirm_tasacion)]
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
