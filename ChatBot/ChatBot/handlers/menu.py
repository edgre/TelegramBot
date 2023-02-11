from create_bot import dp, bot
from aiogram import types, Dispatcher

#@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    f = open('start.txt')
    await message.reply(f.read())

#@dp.message_handler(commands=["glossary"])
async def cmd_glossary(message: types.Message):
    f = open ('glossary.txt')
    await message.reply(f.read())

def handlers_menu (dp:Dispatcher):
    dp.register_message_handler(cmd_start, commands = ["start"])
    dp.register_message_handler(cmd_glossary, commands = ["glossary"])