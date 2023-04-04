import os
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

API_KEY = os.getenv('BOT_TOKEN')
bot = Bot(token=API_KEY)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(msg):
    print(msg.text)
    await bot.send_message(chat_id=msg.chat.id, text='Привет! Я эхо бот!', reply_to_message_id=msg.message_id)


@dp.message_handler(commands=['help'])
async def start(msg):
    print(msg.text)
    await bot.send_message(chat_id=msg.chat.id, text='Привет, я эхо бот!Я прям как попугай!', reply_to_message_id=msg.message_id)


@dp.message_handler()
async def echo_message(msg):
    print("Сообщение полученно!Печатает...")
    await bot.send_message(msg.from_user.id, msg.text, reply_to_message_id=msg.message_id)


if __name__ == '__main__':
    print('Bot_starting!')
    executor.start_polling(dp, timeout=3)

