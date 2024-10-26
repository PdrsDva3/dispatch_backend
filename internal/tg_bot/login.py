from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardButton


import internal.tg_bot.keyboard as kb
import internal.tg_bot.login as login
from internal.tg_bot.init import dp


DATA = """
ВВЕДИТЕ Ваш логин и пароль
Логин      {}
Пароль       {}
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
            tt.add(InlineKeyboardButton(text='все верно', callback_data="cr_pr_ok"))
            await call.message.edit_text(text="проверьте введенные данные и если все "
                                              "верно нажмите на соответсвующую кнопку \n\n" +
                                              DATA.format(l, PWD),
                                         reply_markup=tt)
        else:
            await call.message.edit_text(DATA.format(l, (PWD if p != "None" else p)),
                                         reply_markup=kb.login_kb())


@dp.callback_query_handler(text='start', state="*")
async def new_fr(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(login="None")
    await state.update_data(pwd="None")
    await state.update_data(callback=call)
    await update_keyboard(state)


@dp.callback_query_handler(text='login', state="*")
async def inl_new_fr_name(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("введите ваш login")
    await LoginState.login.set()


@dp.callback_query_handler(text='pwd', state="*")
async def inl_new_fr_name(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("введите ваш пароль")
    await LoginState.pwd.set()


@dp.callback_query_handler(text='cr_pr_ok', state="*")
async def inl_new_fr_name(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text("Посмотреть данные", reply_markup=kb.main_kb())



@dp.message_handler(state=LoginState.login)
async def price_state(message: types.Message, state: FSMContext):
    ll = message.text.lower()
    await state.update_data(login=ll)
    await update_keyboard(state)
    await message.delete()
    await state.set_state(LoginState.wait.state)


@dp.message_handler(state=LoginState.pwd)
async def price_state(message: types.Message, state: FSMContext):
    pwd = message.text.lower()
    await state.update_data(pwd=pwd)
    await update_keyboard(state)
    await message.delete()
    await state.set_state(LoginState.wait.state)


@dp.message_handler(state=LoginState.wait)
async def wait_state(message: types.Message, state: FSMContext):
    await update_keyboard(state)
