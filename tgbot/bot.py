from random import choice
from time import time
from aiogram import executor, types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove
from aiogram import Bot, Dispatcher, types
# import fms.login, fms.create, fms.question
# import db.db
# from config import TOKEN_API
# import yagpt.gpt
# from yagpt.gpt import epi
# from command import dp
# from db.db import db_start, db_deader
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from config import TOKEN_API
import keyboard as kb
import login
import report
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from init import dp

START = """Здравствуйте!\n \nБота создала команда MISIS GogoRiki"""

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    """
    Стартовое сообщение
    Запрос входных данных
    :param message: сообщение, на которое происходит ответ
    :return: ничего, но сообщение имеет несколько кнопок, которые введут на другие функции
    """
    await message.reply(text=START)
    await message.answer(text="Для работы необходимо авторизироваться", reply_markup=kb.start())
    await message.delete()

