#!/usr/bin/python
import time

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from dic import getInfo
# from dic import only_Keys
from dic import staff_data

API_TOKEN = '6600776348:AAFIUiJZPsAen2jrVkDDRJFcxrDAwRaVlOI'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu Alaykum Botimizga Xush Kelibsiz , Iltimos Proyektlarni Qidirishdan Oldin /help buyrugi orqali, Nomzodlar Ismi Bilan Tanishib Chiqing va Nusxa Olish Orqali Botdan Foydalaning, Chunki Bu Bot Ishlashini Yana Optimallashtiradi!")


@bot.message_handler(commands=['help'])
def support_help(message):
    for key in staff_data:
        time.sleep(1)
        bot.send_message(message.chat.id, key)



@bot.message_handler(func=lambda message: True)   # PyTelegramBoTAPI da functiondan oldin har doim shu handler majburiy qoyiladi 1!...
def handle_message(message):
    user_input = message.text.strip()  # Get the user's input   # STRIP YORDAMIDA BOSH JOYLARNI OLIB TASHIMIZ 1!....

    # Use the imported function to retrieve the response.
    response = getInfo(user_input)    # Message ga qiymat berib olganimizdan kegin user_input yordamida, functiondan chiqqan javobga qiymat beramiz 1!.....

    # Send the response back to the user.
    bot.send_message(message.chat.id, response)    # CHAT ID DEGANDA OSHA YOZGAN ODAMMI YOZGAN CHATI , YA'NI ALOHIDA ID RAQAM BERISH SHART EMAS 1!.....



bot.infinity_polling()






