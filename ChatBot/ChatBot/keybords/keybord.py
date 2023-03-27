from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

k1 =  KeyboardButton('/help')
k2 =  KeyboardButton('/glossary')

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(k1).add(k2)
