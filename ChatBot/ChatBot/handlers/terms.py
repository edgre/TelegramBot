from create_bot import dp, bot
from aiogram import types, Dispatcher



#@dp.message_handler(commands=["attack", "database", "informationsecurity", "malware", "availability",
#                             "informationsystem", "information", "threatsource", "virus", "confidentiality",
#                             "attacker", "unauthorizedaccess", "potential", "event", "threat",
#                             "securitythreat", "vulnerability", "integrity"])
async def find_term(message: types.Message):
    f = open("terms.txt")
    term = message.text + ' '
    for line in f:
        if term in line:
            defenition = line
    defenition = defenition.replace (message.text, '')
    await message.reply(defenition)

def handlers_term(dp:Dispatcher):
    dp.register_message_handler(find_term, commands = ["attack", "database", "informationsecurity", "malware", "availability",
                             "informationsystem", "information", "threatsource", "virus", "confidentiality",
                             "attacker", "unauthorizedaccess", "potential", "event", "threat",
                             "securitythreat", "vulnerability", "integrity"])

