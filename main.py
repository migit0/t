import asyncio
import logging
import sys
from typing import List

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import hbold

token = "7110556019:AAG05mzFIypf8PlpbNOj5_w8qGmr3ez-NYk"
bot = Bot(token, parse_mode=ParseMode.HTML)
dp = Dispatcher()


class ButtonText:
    HELLO = "Привет"
    HELP = "Показать возможности"
    DOC = "Скачать документ"
    DOCLINK = "https://drive.google.com/file/d/1d9-yNINYFJqAAFWk2ngcPDCfyq2U2cCu/view?usp=sharing"
    TEAMBILD = "Запись на мероприятие"
    TEAMBILINK = "https://t.me/c/1775748072/693"


tg_docs_btn = InlineKeyboardButton(text=ButtonText.DOC, url=ButtonText.DOCLINK)
tg_thems_btn = InlineKeyboardButton(text=ButtonText.TEAMBILD, url=ButtonText.TEAMBILINK)

row = [tg_docs_btn, tg_thems_btn]
buttons_row = [row]
func_list = InlineKeyboardMarkup(inline_keyboard=buttons_row)


@dp.message(CommandStart())
async def start_handler(message: Message) -> None:
    button_hello = KeyboardButton(text=ButtonText.HELLO)
    button_help = KeyboardButton(text=ButtonText.HELP)

    buttons_row = [button_hello, button_help]
    keyboard = ReplyKeyboardMarkup(keyboard=[buttons_row], resize_keyboard=True)
    await message.answer(
        text=f"Привет, {hbold(message.from_user.full_name)}!",
        reply_markup=keyboard)


@dp.message(Command("help"))
async def handler_help_handler(message: Message) -> None:
    text = "Как Вам помочь?"
    await message.answer(text="Ресусры", reply_markup=func_list)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
