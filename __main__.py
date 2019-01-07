import os
import logging
from telegram.ext import Updater, CommandHandler

API_TOKEN = os.environ.get('BRUTALIC_TOKEN')

updater = Updater(API_TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


def start(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
