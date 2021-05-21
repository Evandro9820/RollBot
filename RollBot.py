import telebot
import logging
import random
import os
from flask import Flask, request

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
# # Token do bot
# bot = telepot.Bot('1819726569:AAFvgf-gUvd6hxZzVhkVKrNpwOjjRKQGsMA')
#
#
# def handle(msg):
#     chat_id = msg['chat']['id']
#     command = msg['text']
#
#     print("Use o comando /rolldados para rolar dados")
#
#     if command == '/rolldados':
#         bot.sendMessage(chat_id, random.randint(1, 6))
TOKEN = '1819726569:AAFvgf-gUvd6hxZzVhkVKrNpwOjjRKQGsMA'
bot = telebot.TeleBot(TOKEN, parse_mode=None)
server = Flask(__name__)


@bot.message_handler(commands=['start'])
def send_bemvindo(message):
    bot.reply_to(message, "olá eu sou o Rollbot")


@bot.message_handler(commands=['rolldados'])
def send_dados(message,):
    bot.send_message(chat_id=message.chat.id,
                     text="Use /d4 - para rolar um dados de quatro faces \n"
                     "Use /d12 - para rolar um dados de doze faces \n"
                     "Use /d6 - para rolar um dados de seis faces \n"
                     "Use /d20 - para rolar um dados de vinte faces \n"
                     )


# Comando de rolar dados
@bot.message_handler(commands=['d4'])
def fd4(message):
    fd4 = random.randint(1, 4)
    bot.send_message(chat_id=message.chat.id, text=" O resultado é %s" % fd4)
    if fd4 == 4:
        bot.send_message(chat_id=message.chat.id, text="Sucesso absoluto")
    elif fd4 == 1:
        bot.send_message(chat_id=message.chat.id, text="Fracasso")


@bot.message_handler(commands=['d6'])
def fd6(message):
    fd6 = random.randint(1, 6)
    bot.send_message(chat_id=message.chat.id, text=" O resultado é %s" % fd6)
    if fd4 == 6:
        bot.send_message(chat_id=message.chat.id, text="Sucesso absoluto")
    elif fd4 == 1:
        bot.send_message(chat_id=message.chat.id, text="Fracasso")


@bot.message_handler(commands=['d12'])
def fd12(message):
    fd12 = random.randint(1, 12)
    bot.send_message(chat_id=message.chat.id, text=" O resultado é %s" % fd12)
    if fd12 == 4:
        bot.send_message(chat_id=message.chat.id, text="Sucesso absoluto")
    elif fd12 == 1:
        bot.send_message(chat_id=message.chat.id, text="Fracasso")


@bot.message_handler(commands=['d20'])
def fd20(message):
    fd20 = random.randint(1, 20)
    bot.send_message(chat_id=message.chat.id, text=" O resultado é %s" % fd20)
    if fd20 == 20:
        bot.send_message(chat_id=message.chat.id, text="Sucesso absoluto")
    elif fd20 == 1:
        bot.send_message(chat_id=message.chat.id, text="Fracasso")


@server.route("/")
def webhook():
    bot.remove_webhook
    bot.set_webhook(url='https://infinite-depths-02571.herokuapp.com/'
                    + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


# bot.polling()
