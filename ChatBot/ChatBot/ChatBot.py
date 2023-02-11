import asyncio
from aiogram.utils import executor
from aiogram import types
from create_bot import dp

if __name__ == '__main__':
    from handlers import terms, menu
    menu.handlers_menu(dp)
    terms.handlers_term(dp)
    executor.start_polling(dp)
    
