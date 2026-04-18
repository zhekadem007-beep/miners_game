import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton

# Твій токен
TOKEN = "8660771922:AAGCT3mO1lwItGPNjS7Eo2plNVZlQNQmaY8"

# Посилання на твої ігри на GitHub Pages
URL_MINES = "https://zhekadem007-beep.github.io/miners_game/"
URL_UPGRADE = "https://zhekadem007-beep.github.io/globalupgrade/"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    # Створюємо кнопки меню
    kb = [
        [
            KeyboardButton(text="💣 PLAY MINES", web_app=WebAppInfo(url=URL_MINES))
        ],
        [
            KeyboardButton(text="⚡ GLOBAL UPGRADE", web_app=WebAppInfo(url=URL_UPGRADE))
        ]
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Обери режим гри..."
    )

    await message.answer(
        "⚡ **Welcome to the Game Center!**\n\n"
        "Choose the game you want to play now by clicking the button below. ",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )


# Запуск бота
async def main():
    print("Бот працює... Натисніть /start у Telegram")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот вимкнений")
