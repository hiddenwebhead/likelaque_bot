
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()

@dp.message(Command("command1"))
async def handle_online_booking(message: Message):
    url = "https://n429737.alteg.io/company/34048/personal/menu?fbclid=PAZXh0bgNhZW0CMTEAAaeQn-WU4BpebipAS1cn_J1-W6lY9ynQnmUJFA5PhXl4Ov5R8Nm_ldYt0Lo_aem_66VcMl-ZJo4SMs9--OYUvwo&o="
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📅 Перейти до онлайн-запису", url=url)]
        ]
    )
    await message.answer("Оберіть нижче:", reply_markup=kb)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
