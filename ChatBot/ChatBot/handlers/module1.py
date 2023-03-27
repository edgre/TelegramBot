from create_bot import dp
from aiogram import types, Dispatcher
from data_base.threats import cur


async def text(message: types.Message):
    if message.text[0] != '/':
     cur.execute("SELECT Название FROM threats WHERE №='%s'" % ('УБИ.001'))
     ans = cur.fetchone()
     await message.answer(f'{ans[0]}');

def handlers_text (dp:Dispatcher):
   dp.register_message_handler(text)