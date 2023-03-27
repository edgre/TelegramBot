from create_bot import dp, bot
from aiogram import types, Dispatcher
from keybords.keybord import kb
from data_base import threats

#@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer()

#@dp.message_handler(commands=["glossary"])
async def cmd_glossary(message: types.Message):
    f = open ('glossary.txt')
    await message.reply(f.read())



def handlers_menu (dp:Dispatcher):
    dp.register_message_handler(cmd_start, commands = ["start", "help"])
    dp.register_message_handler(cmd_glossary, commands = ["glossary"])
    