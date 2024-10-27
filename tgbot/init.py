from random import choice
from time import time
from aiogram import executor, types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove
from aiogram import Bot, Dispatcher, types
# import fms.login, fms.create, fms.question
# import db.db
from config import TOKEN_API
# import yagpt.gpt
# from yagpt.gpt import epi
# from command import dp
# from db.db import db_start, db_deader
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN_API
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


bot = Bot(TOKEN_API)
dp = Dispatcher(bot, storage=MemoryStorage())

async def on_startup(_):
    """
    Сообщение о запуске работы чат-бота
    :return: -
    """
    print("HI, i work")


def start_tg():
    """
    Запуск работы чат-бота
    :return: -
    """
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
