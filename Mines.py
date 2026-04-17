import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8660771922:AAGCT3mO1lwItGPNjS7Eo2plNVZlQNQmaY8"
# Тобі треба залити свій index.html на будь-який хостинг (наприклад GitHub Pages або Vercel)
# І вставити посилання сюди:
URL = "https://zhekadem007-beep.github.io/miners_game/"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Відкрити Міни 💣", web_app=WebAppInfo(url=URL))]
    ])
    await message.answer("Натисни кнопку нижче, щоб запустити гру:", reply_markup=markup)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())