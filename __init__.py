import os
from telegram.ext import Updater, CommandHandler

API_TOKEN = os.environ.get('BRUTALIC_TOKEN')

updater = Updater(API_TOKEN)


def say_hello(bot, update):
    print(update)
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


updater.dispatcher.add_handler(CommandHandler('hello', say_hello))

updater.start_polling()
updater.idle()
