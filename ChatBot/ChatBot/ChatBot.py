import asyncio
from aiogram.utils import executor
from aiogram import types
from create_bot import dp
from data_base import threats

if __name__ == '__main__':
    threats.sql_start()
    from handlers import terms, menu, module1
    menu.handlers_menu(dp)
    terms.handlers_term(dp)
    module1.handlers_text(dp)
    executor.start_polling(dp)
    
