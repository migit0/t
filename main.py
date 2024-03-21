import telebot

token = "7110556019:AAG05mzFIypf8PlpbNOj5_w8qGmr3ez-NYk"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Bot is working!")

bot.infinity_polling()