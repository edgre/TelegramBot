import sqlite3 as sq
from create_bot import bot

def sql_start():
    global data, cur
    data = sq.connect('threats.db')
    cur = data.cursor()

    