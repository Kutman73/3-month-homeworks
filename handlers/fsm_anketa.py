from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from my_bots.bot2.config import bot, ADMIN
from my_bots.bot2.database.bot_db import sgl_command_insert
from my_bots.bot2.test import r_id


class FSMAdmin(StatesGroup):
    name = State()
    ids = State()
    direct = State()
    age = State()
    Mgroup = State()
    submit = State()


async def fsm_start(message: types.Message, state: FSMContext):
    if message.chat.type == 'private':
        if not message.from_user.id in ADMIN:
            await message.answer('Эта команда доступна толька админам')
        else:
            await FSMAdmin.name.set()
            await message.answer(
                f'Привет {message.from_user.full_name}'
                f'\nКак тебя зовут?'
                )
    else:
        await message.answer('Пиши в личку!')


async def mentor_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Отправте любое сообщение')


async def mentor_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = r_id.n
    await FSMAdmin.next()
    await message.answer('Какое у вас направление?')


async def mentor_direct(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direct'] = message.text
    await FSMAdmin.next()
    await message.answer('Сколько лет?')


async def mentor_age(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['age'] = int(message.text)
        await FSMAdmin.next()
        await message.answer("В какой группе?")
    except:
        await message.answer("Только цифрами!")


async def mentor_group(message: types.Message, state: FSMContext):
    photo = open("media/photo_mentors/photo_2022-07-30_17-47-13.jpg", 'rb')
    try:
        async with state.proxy() as data:
            data['Mgroup'] = message.text
        print(data)
        await FSMAdmin.next()
        await bot.send_photo(message.from_user.id, photo=photo,
                                caption=f"Имя: {data['name']}\nID: {data['id']}\nНаправление: {data['direct']}\n"
                                     f"Возраст: {data['age']}\nГруппа: {data['Mgroup']}")
        await message.answer('Всё правильно?\nНапишите (да) или (нет) это обязательно!!!')
    except:
        await message.answer("Только цифрами!")


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        await sgl_command_insert(state)
        await state.finish()
        await message.answer('Регистрация завершена')
    if message.text.lower() == 'нет':
        await state.finish()
        await message.answer('отменено!')


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('отменено!')


def register_handlers_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True),
                                state='*')
    dp.register_message_handler(mentor_name, state=FSMAdmin.name)
    dp.register_message_handler(mentor_direct, state=FSMAdmin.direct)
    dp.register_message_handler(mentor_age, state=FSMAdmin.age)
    dp.register_message_handler(mentor_group, state=FSMAdmin.Mgroup)
    dp.register_message_handler(mentor_id, state=FSMAdmin.ids)
    dp.register_message_handler(submit, state=FSMAdmin.submit)

