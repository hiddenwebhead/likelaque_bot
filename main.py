import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()

subscribed_users = set()

menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📋 Дізнатися о послугах", url="https://likelaque.com.ua/pdf/price.pdf"),
         InlineKeyboardButton(text="🗓 Записатися онлайн", url="https://n53924.alteg.io")],
        [InlineKeyboardButton(text="📍 Як дістатися", url="https://www.google.com/maps/place/Yevhena+Konovaltsia+St,+3,+Kyiv"),
         InlineKeyboardButton(text="🕒 Графік роботи", url="https://t.me/Like_Laque_bot?start=schedule")],
        [InlineKeyboardButton(text="📸 Instagram", url="https://www.instagram.com/likelaque/"),
         InlineKeyboardButton(text="📞 Зателефонувати", url="tel:+380678322330")],
        [InlineKeyboardButton(text="💬 Написати в салон", url="https://www.instagram.com/direct/t/117822186276861")]
    ]
)

@dp.message(Command("start"))
async def start_handler(message: Message):
    subscribed_users.add(message.chat.id)
    await message.answer("👋 Вітаємо в салоні Like Laque! Оберіть потрібне:", reply_markup=menu_keyboard)

async def reminder_loop():
    while True:
        await asyncio.sleep(3000000)
        for chat_id in subscribed_users:
            try:
                await bot.send_message(chat_id, "💅 Нагадування: не забудьте записатися на послуги!")
            except Exception:
                pass

async def main():
    asyncio.create_task(reminder_loop())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
