import aioschedule
from aiogram import types, Dispatcher
from my_bots.bot2.venv.config import bot
import asyncio


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id

    await message.answer('Okey :)')


async def let_talk():
    await bot.send_message(chat_id=chat_id, text='good evening')


async def wake_up():
    video = open("media/mems/И так каждый понедельник.mp4", "rb")
    await bot.send_video(chat_id=chat_id, video=video)


async def sheduler():
    aioschedule.every().monday.at('07:00').do(wake_up)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)



def register_handlers_notifications(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'напомни' in word.text)
