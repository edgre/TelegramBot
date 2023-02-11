import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot (token = '6032787190:AAES_W-m4UPYagBAUaj4l1eWcIc7_BY_kmA')
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    f = open('start.txt')
    await message.reply(f.read())

@dp.message_handler(commands=["glossary"])
async def cmd_glossary(message: types.Message):
    f = open ('glossary.txt')
    await message.reply(f.read())

@dp.message_handler(commands=["attack", "database", "informationsecurity", "malware", "availability",
                             "informationsystem", "information", "threatsource", "virus", "confidentiality",
                              "attacker", "unauthorizedaccess", "potential", "event", "threat",
                              "securitythreat", "vulnerability", "integrity"])
async def find_term(message: types.Message):
    f = open("terms.txt") 
    for line in f:
        if message.text in line:
            term = line
    term = term.replace (message.text, '')
    await message.reply(term)



if __name__ == '__main__':
    executor.start_polling(dp)

