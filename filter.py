import os
from telebot import TeleBot



bot = TeleBot('5402545793:AAGLuWHk32tGEezCYz7rDPqu8pdRve58-_s')

@bot.message_handler(commands = ["help", "start"])
def enviar_mensaje(message):
    bot.reply_to(message, "Приветики, я бот")

@bot.message_handler(func=lambda message: True)
def message(message):
    bot.reply_to(message, message.text)

bot.polling()