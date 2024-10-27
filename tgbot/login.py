from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardButton


import tgbot.keyboard as kb
import tgbot.login as login
from tgbot.init import dp


DATA = """
ВВЕДИТЕ Ваш логин и пароль
Логин        {}
Пароль      {}
"""
PWD = "********"


class LoginState(StatesGroup):
    login = State()
    pwd = State()
    wait = State()


async def update_keyboard(state: FSMContext):
    async with state.proxy() as data:
        l = data['login']
        p = data['pwd']
        call = data['callback']
        if (p != "None" and l != "None"):
            tt = kb.login_kb()
            tt.add(InlineKeyboardButton(text='Все верно', callback_data="cr_pr_ok"))
            await call.message.edit_text(text="Проверьте введенные данные и если все "
                                              "верно нажмите на соответсвующую кнопку \n\n" +
                                              DATA.format(l, PWD),
                                         reply_markup=tt)
        else:
            await call.message.edit_text(DATA.format(l, (PWD if p != "None" else p)),
                                         reply_markup=kb.login_kb())


@dp.callback_query_handler(text='start', state="*")
async def start(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(login="None")
    await state.update_data(pwd="None")
    await state.update_data(callback=call)
    await update_keyboard(state)


@dp.callback_query_handler(text='login', state="*")
async def login(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("Введите ваш login")
    await LoginState.login.set()


@dp.callback_query_handler(text='pwd', state="*")
async def pwd(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("Введите ваш пароль")
    await LoginState.pwd.set()


@dp.callback_query_handler(text='cr_pr_ok', state="*")
async def all_ok(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text("Посмотреть данные", reply_markup=kb.main_kb())



@dp.message_handler(state=LoginState.login)
async def login_state(message: types.Message, state: FSMContext):
    ll = message.text.lower()
    await state.update_data(login=ll)
    await update_keyboard(state)
    await message.delete()
    await state.set_state(LoginState.wait.state)


@dp.message_handler(state=LoginState.pwd)
async def pwd_state(message: types.Message, state: FSMContext):
    pwd = message.text.lower()
    await state.update_data(pwd=pwd)
    await update_keyboard(state)
    await message.delete()
    await state.set_state(LoginState.wait.state)


@dp.message_handler(state=LoginState.wait)
async def wait_state(message: types.Message, state: FSMContext):
    await update_keyboard(state)
