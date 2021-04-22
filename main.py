
import os
import telebot
from flask import Flask, request

TOKEN = '1790892466:AAEo2tiTgaDjpXiA9omYZGKmZHFdLLXaPQY'  # это мой токен
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


@bot.message_handler(commands=['start'])
def send_info(message):
   text = (
   "<b>Welcome to the Medium 🤖!</b>\n"
   "Say Hello to the bot to get a reply from it!"
   )
   bot.send_message(message.chat.id, text, parse_mode='HTML')
# Если строка на входе непустая, то бот повторит ее
@bot.message_handler(func=lambda msg: msg.text is not None)
def reply_to_message(message):
    bot.reply_to(message.chat.id, message.text)


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://mytelegramproject.herokuapp.com/' + TOKEN)  #
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
