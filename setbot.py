from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher
import logging

logging.basicConfig(format='%(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)
updater = None

def start(update, context):
    sss = "Hi there, I am AE. A little test bot."
    update.message.reply_text(sss)

def start_bot():
    global updater
    updater = Updater(
        '1643323711:AAH9fIbNx3R2Tl764yyrT_OSNGwXfA64FzE', use_context=True)
    
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()
start_bot()



