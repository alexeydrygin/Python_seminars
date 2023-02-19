# Напишите Бота, удаляющего из текста все слова, содержащие "абв". (Ввод от пользователя)


import logging
import re
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware
from aiogram.types import ParseMode

# Задаем уровень логов
logging.basicConfig(level=logging.INFO)

# Создаем бота
bot = Bot(token="----------------------------------")

# Создаем диспетчер для обработки запросов
dp = Dispatcher(bot)

# Создаем миддлвар для управления сроком жизни сессий
session_life_time = LifetimeControllerMiddleware(lifetime=60*60*24)  # 24 часа
dp.middleware.setup(session_life_time)

# Обработка команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Я бот, который удаляет из текста все слова, содержащие 'абв'.\n\nВведите текст:")

# Обработка текста
@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def handle_text(message: types.Message):
    text = message.text
    # Удаляем все слова, содержащие "абв"
    text = re.sub(r'\b\w*абв\w*\b', '', text)
    await message.answer(f"Текст без слов, содержащих 'абв':\n\n{text}")

# Обработка ошибок в телеграмм-боте
async def on_error(update: types.Update, exception: Exception):
    logging.exception(f"Update {update} caused error {exception}")

# Запуск бота
if __name__ == '__main__':
    dp.middleware.setup(LifetimeControllerMiddleware())
    dp.register_errors_handler(on_error)
    dp.start_polling()
