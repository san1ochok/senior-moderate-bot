from aiogram.dispatcher.filters.state import StatesGroup, State


class BotMailing(StatesGroup):
    text = State()
    state = State()
    photo = State()
