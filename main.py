import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN, parse_mode="Markdown")
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message):
    # При /start отправляем сразу меню услуг
    menu_text = """📋 [Послуги](https://likelaque.com.ua/pdf/price.pdf)
🕒 [ПН-ПТ 09:00-21:00, СБ-НД 10:00-21:00]
🗓 [Онлайн-запис](https://n53924.alteg.io)
📍 [Як дістатися](https://www.google.com/maps/place/Yevhena+Konovaltsia+St,+3,+Kyiv)
📸 [Instagram](https://www.instagram.com/likelaque/)
💬 [Чат](https://www.instagram.com/direct/t/117822186276861)
📞 [80678322330]"""
    await message.answer(menu_text, disable_web_page_preview=True)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
