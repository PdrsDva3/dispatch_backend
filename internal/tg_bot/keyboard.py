from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_month():
    import datetime
    import calendar
    now = datetime.datetime.now()
    current_month = now.month
    current_year = now.year
    weekday_c = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
    first_weekday, days_in_month = calendar.monthrange(current_year, current_month)
    first_weekday_name = calendar.day_name[first_weekday]
    return weekday_c[first_weekday_name], days_in_month


def start() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button = InlineKeyboardButton("авторизоваться", callback_data="start")
    keyboard.add(button)
    return keyboard


def login_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button = InlineKeyboardButton("Login", callback_data="login")
    button1 = InlineKeyboardButton("password", callback_data="pwd")
    kb.add(button).add(button1)
    return kb


def main_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button = InlineKeyboardButton("сегодня", callback_data="report")
    button1 = InlineKeyboardButton("календарь", callback_data="calendar")
    kb.add(button).add(button1)
    return kb


def today_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    b1 = InlineKeyboardButton("отчет", callback_data="download")
    b2 = InlineKeyboardButton("анализ", callback_data="analiz")
    b3 = InlineKeyboardButton("риски", callback_data="risk")
    button = InlineKeyboardButton("вернуться", callback_data="cr_pr_ok")
    kb.add(b1).add(b2).add(b3).add(button)
    return kb


def return_today_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    b1 = InlineKeyboardButton("вернуться", callback_data="report")
    kb.add(b1)
    return kb

def return_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button = InlineKeyboardButton("вернуться", callback_data="cr_pr_ok")
    kb.add(button)
    return kb


def return_calendar_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button = InlineKeyboardButton("вернуться", callback_data="cr_pr_ok")
    button1 = InlineKeyboardButton("выбрать другой день", callback_data="calendar")
    kb.add(button1).add(button)
    return kb


def calendar_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=7)
    ll = list()
    st, cnt = get_month()
    week = ["Mon", "Tue","Wed", "Thu", "Fri", "Sat", "Sun"]
    for day in week:
        button = InlineKeyboardButton(day, callback_data="calendar")
        ll.append(button)
    for i in range(st):
        button = InlineKeyboardButton(" ", callback_data="calendar")
        ll.append(button)
    for i in range(1, cnt + 1):
        button = InlineKeyboardButton(str(i), callback_data="day" + str(i))
        ll.append(button)
    while len(ll) % 7 != 0:
        button = InlineKeyboardButton(" ", callback_data="calendar")
        ll.append(button)
    kb.add(*ll)
    button = InlineKeyboardButton("вернуться", callback_data="cr_pr_ok")
    kb.add(button)
    return kb
