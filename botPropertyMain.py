from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler
from telegram.ext import ConversationHandler, CallbackQueryHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import logging
import botPropertySelect as select
import botPropertySet as set
import botPropertyDataBase as db

global id


#telegram_token = "666842820:AAGg1F_NjlQBL7IPv9XlfMEC0PJ6iWlVLj0"
telegram_token = "864014186:AAGrFbg92jxFplBVlYSXh9brToc2aal3RMg"
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)

# Global vars:

LOGIN,MENU, SELECT_OP, SELECT_REGION, SELECT_COMUNA, SELECT_TIPO, SELECT_DORMS,SELECT_BATHS, \
SELECT_PRICE_RANGE, SELECT_AREA_RANGE,CONFIRM_REPORT,SELECT_SITE,SELECT_ID,CONFIRM_FILE = range(14)

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
    update.message.reply_text("mensaje adiuos",
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

            SELECT_SITE: [MessageHandler(Filters.text, set.site)],

            SELECT_ID: [MessageHandler(Filters.text, set.id_prop)],

            CONFIRM_FILE: [MessageHandler(Filters.text, set.confirm_file)]
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