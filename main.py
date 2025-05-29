import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()

# Словари языков
texts = {
    "ua": {
        "welcome": "✨ Вітаємо в манікюрному салоні Like Laque! Оберіть мову:",
        "menu": "📋 Оберіть розділ:",
        "schedule": "🕒 Графік роботи:
ПН–ПТ: 09:00–21:00
СБ–НД: 10:00–21:00"
    },
    "en": {
        "welcome": "✨ Welcome to Like Laque! Please choose your language:",
        "menu": "📋 Choose a section:",
        "schedule": "🕒 Working hours:
Mon–Fri: 09:00–21:00
Sat–Sun: 10:00–21:00"
    }
}

user_lang = {}  # chat_id -> "ua" | "en"

@dp.message(Command("start"))
async def start_handler(message: Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🇺🇦 Українська", callback_data="lang_ua"),
             InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en")]
        ]
    )
    await message.answer("✨ Welcome / Вітаємо!", reply_markup=kb)

@dp.callback_query(lambda c: c.data.startswith("lang_"))
async def set_language(callback_query: CallbackQuery):
    lang = callback_query.data.split("_")[1]
    user_lang[callback_query.from_user.id] = lang
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📋 Меню / Menu", callback_data="show_menu")]
        ]
    )
    await callback_query.message.answer(texts[lang]["welcome"], reply_markup=kb)
    await callback_query.answer()

@dp.callback_query(lambda c: c.data == "show_menu")
async def show_menu(callback_query: CallbackQuery):
    lang = user_lang.get(callback_query.from_user.id, "ua")
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🗓 Онлайн-запис", url="https://n53924.alteg.io")],
            [InlineKeyboardButton(text="📍 Як дістатися", url="https://www.google.com/maps/place/Yevhena+Konovaltsia+St,+3,+Kyiv,+02000/@50.4235062,30.5175455,17z")],
            [InlineKeyboardButton(text="📞 Зателефонувати", url="tel:+380678322330")],
            [InlineKeyboardButton(text="🕒 Графік роботи", callback_data="schedule")],
            [InlineKeyboardButton(text="📸 Instagram", url="https://www.instagram.com/likelaque/")],
            [InlineKeyboardButton(text="💬 Написати в салон", url="https://www.instagram.com/direct/t/117822186276861")],
            [InlineKeyboardButton(text="📋 Послуги та ціни", url="https://likelaque.com.ua/pdf/price.pdf")]
        ]
    )
    await callback_query.message.answer(texts[lang]["menu"], reply_markup=kb)
    await callback_query.answer()

@dp.callback_query(lambda c: c.data == "schedule")
async def send_schedule(callback_query: CallbackQuery):
    lang = user_lang.get(callback_query.from_user.id, "ua")
    await callback_query.message.answer(texts[lang]["schedule"])
    await callback_query.answer()

# Напоминания каждые 10 дней (86400 * 10 секунд)
async def reminder_loop():
    while True:
        await asyncio.sleep(864000)
        for chat_id in user_lang:
            lang = user_lang[chat_id]
            text = "🧴 Не забудьте записатися на манікюр! 💅" if lang == "ua" else "💅 Don't forget to book your manicure!"
            try:
                await bot.send_message(chat_id, text)
            except Exception:
                pass

async def main():
    asyncio.create_task(reminder_loop())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
