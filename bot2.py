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
LANG = "EN"
MENU, SET_STAT, REPORT, MAP, FAQ, ABOUT = range(6)
STATE = MENU


def start(bot, update):
    """
    Start function. Displayed whenever the /start command is called.
    This function sets the language of the bot.
    """
    # Create buttons to slect language:
    keyboard = [['ES', 'EN']]

    # Create initial message:
    message = "Hola, soy el bot de admin de props. "

    menu(bot, update)

    return MENU

def menu(bot, update):
    """
    Main menu function.
    This will display the options from the main menu.
    """
    # Create buttons to slect language:
    keyboard = [["reporte"],
                ["faq", "acerca"]]

    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)

    user = update.message.from_user
    logger.info("Menu command requested by {}.".format(user.first_name))
    update.message.reply_text("menu principal", reply_markup=reply_markup)

    return MENU


def set_state(bot, update):
    """
    Set option selected from menu.
    """
    # Set state:
    global STATE
    user = update.message.from_user
    if update.message.text == "reporte":
        STATE = REPORT
        report(bot, update)
        menu(bot, update)
        return SET_STAT
    elif update.message.text == "faq":
        STATE = FAQ
        faq(bot, update)
        return MENU
    elif update.message.text == "acerca":
        STATE = ABOUT
        about_bot(bot, update)
        return MENU
    else:
        STATE = MENU
        return MENU


def report(bot, update):
    """
    FAQ function. Displays FAQ about disaster situations.
    """
    user = update.message.from_user
    logger.info("Report requested by {}.".format(user.first_name))
    update.message.reply_text("generando reporte")
    bot.send_message(chat_id=update.message.chat_id, text="volviendo a menu")
    return


def faq(bot, update):
    """
    FAQ function. Displays FAQ about disaster situations.
    """
    user = update.message.from_user
    logger.info("FAQ requested by {}.".format(user.first_name))
    bot.send_message(chat_id=update.message.chat_id, text="FAQ")
    bot.send_message(chat_id=update.message.chat_id, text="volviendo a menu")
    return


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
    global LANG
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(telegram_token)

    # Get the dispatcher to register handlers:
    dp = updater.dispatcher

    # Add conversation handler with predefined states:
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={

            MENU: [CommandHandler('menu', menu)],

            SET_STAT: [RegexHandler(
                        '^({}|{}|{})$'.format("reporte", "faq", "acerca"),set_state)]
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