from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    age = State()
    gender = State()
    region = State()

async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        pass
    else:
        await message.answer('Пиши в личку!')