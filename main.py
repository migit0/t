import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.markdown import hbold

token = "7110556019:AAG05mzFIypf8PlpbNOj5_w8qGmr3ez-NYk"
bot = Bot(token, parse_mode=ParseMode.HTML)
dp = Dispatcher()


class ButtonText:
    HELLO = "Привет"
    HELP = "Вторая кнопка"


@dp.message(CommandStart())
async def start_handler(message: Message) -> None:
    button_hello = KeyboardButton(text=ButtonText.HELLO)
    button_help = KeyboardButton(text=ButtonText.HELP, URL="https://1c.ru/")

    buttons_row = [button_hello, button_help]
    keyboard = ReplyKeyboardMarkup(keyboard=[buttons_row], resize_keyboard=True)
    await message.answer(
        text=f"Привет, {hbold(message.from_user.full_name)}!",
        reply_markup=keyboard
    )


@dp.message(Command("help"))
async def handler_help_handler(message: Message) -> None:
    text = "Как Вам помочь?"
    await message.answer(text=text)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

'''import telebot

token = "7110556019:AAG05mzFIypf8PlpbNOj5_w8qGmr3ez-NYk"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Bot is working!")

bot.infinity_polling()'''
