from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from internal.tg_bot.init import dp
from internal.tg_bot.keyboard import return_kb, calendar_kb, return_calendar_kb, today_kb, return_today_kb


@dp.callback_query_handler(text='report')
async def new_fr(call: types.CallbackQuery):
    await call.message.edit_text("здесь данные с ручки информации в данный момент", reply_markup=today_kb())


@dp.callback_query_handler(text='calendar')
async def main_callback(call: types.CallbackQuery):
    await call.message.edit_text(text="выберите день", reply_markup=calendar_kb())


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('day'))
async def main_callback(call: types.CallbackQuery):
    await call.message.edit_text(text="здесь данные по ручке на " + call.data, reply_markup=return_calendar_kb())


@dp.callback_query_handler(text='download')
async def new_fr(call: types.CallbackQuery):
    await call.message.edit_text("здесь отправляется файл на скачивание отчета", reply_markup=return_today_kb())


@dp.callback_query_handler(text='analiz')
async def new_fr(call: types.CallbackQuery):
    await call.message.edit_text("здесь краткий отчет", reply_markup=return_today_kb())


@dp.callback_query_handler(text='risk')
async def new_fr(call: types.CallbackQuery):
    await call.message.edit_text("здесь анализ рисков от алисы", reply_markup=return_today_kb())
