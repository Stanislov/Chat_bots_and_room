# -*- coding: utf-8 -*-
import telebot

bot = telebot.TeleBot("673")
@bot.message_handler(content_types=["text"])
mess = ['Привет','привет','прив', 'Hi', 'hi', 'Hello', 'hello']

def handle_text(message):
    if message.text in mess:
        bot.send_message(message.from_user.id, "Привет! Я бот. Давай познакомимся?")
    
    elif message.text == "How are you?" or message.text == "How are u?":
        bot.send_message(message.from_user.id, "I'm fine, thanks. And you?")
    
    else:
        bot.send_message(message.from_user.id, "Sorry, i dont understand you.")

bot.polling(none_stop=True, interval=0)

# Обработчик команд '/start' и '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    pass

 # Обработчик для документов и аудиофайлов
@bot.message_handler(content_types=['document', 'audio'])
def handle_document_audio(message):
    pass

bot.polling(none_stop=True, interval=0)