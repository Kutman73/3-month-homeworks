from aiogram import types, Dispatcherfrom my_bots.bot2.venv.config import botasync def echo(message: types.Message):    bad_words = ['html', 'java']    answer = f'@{message.from_user.username}' if message.from_user.username is not None else message.from_user.full_name    for word in bad_words:        if word in message.text.lower():            await bot.delete_message(message.chat.id, message.message_id)            if message.from_user.username is not None:                await message.answer(f'Не матерись {answer}')    if message.chat.type == "private":        try:            if message.text == '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':                message_int = int(message.text)                m = message_int * message_int                await bot.send_message(message.from_user.id, m)        except ValueError:            await bot.send_message(message.from_user.id, message.text)def register_handlers_extra(dp: Dispatcher):    dp.register_message_handler(echo)