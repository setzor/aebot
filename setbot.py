from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher, requests, io
import logging

logging.basicConfig(format='%(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)
updater = None

def echo(update, context):
    command = context.args[0].lower()
    if("on" == command):
        context.user_data[echo] = True
        update.message.reply_text("Repeater Started")
    elif("off" == command):
        context.user_data[echo] = False
        update.message.reply_text("Repeater Stopped")

def start(update, context):
    sss = "Hi there, I am AE. A little test bot."
    update.message.reply_text(sss)

def repeater(update, context):
    if context.user_data[echo]:
        update.message.reply_text(update.message.text)

def start_bot():
    global updater
    updater = Updater(
        'xxx', use_context=True)
    
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('echo', echo))
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text, repeater))

    
    

    updater.start_polling()
    updater.idle()
    
start_bot()



