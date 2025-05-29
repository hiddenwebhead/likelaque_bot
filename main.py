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
    await message.answer("👋 Вітаємо в салоні Like Laque!\nНапишіть /services щоб дізнатися більше.")

@dp.message(Command("services"))
async def services_handler(message: Message):
    text = (
        "📋 [Дізнатися о послугах](https://likelaque.com.ua/pdf/price.pdf)
"
        "🗓 [Записатися на послуги онлайн](https://n53924.alteg.io)
"
        "📍 [Дізнатися як дістатися](https://www.google.com/maps/place/Yevhena+Konovaltsia+St,+3,+Kyiv)
"
        "🕒 [Дізнатися графік роботи](https://t.me/Like_Laque_bot?start=schedule)
"
        "📸 [Подивитисі світлини в Instagram](https://www.instagram.com/likelaque/)
"
        "📞 [Зателефонувати у салон](tel:+380678322330)
"
        "💬 [Написати в салон](https://www.instagram.com/direct/t/117822186276861)"
    )
    await message.answer(text, disable_web_page_preview=True)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
