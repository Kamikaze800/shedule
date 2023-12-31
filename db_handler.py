import sqlite3
import sys

from main_window import *

def login(login, passw, signal):
    con = sqlite3.connect('static/users') # Подключаемся к базе данных
    cur = con.cursor()

    # Проверяем есть ли такой пользователь
    cur.execute(f'SELECT * FROM users WHERE name="{login}";')
    value = cur.fetchall()

    if value != [] and value[0][2] == passw:


        return True

    else:
        signal.emit('Проверьте правильность ввода данных!')

    cur.close()
    con.close()



def register(login, passw, signal):
    con = sqlite3.connect('users')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE name="{login}";')
    value = cur.fetchall()

    if value != []:
        signal.emit('Такой ник уже используется!')

    elif value == []:
        cur.execute(f"INSERT INTO users (name, password) VALUES ('{login}', '{passw}')")
        signal.emit('Вы успешно зарегистрированы!')
        con.commit()

    cur.close()
    con.close()
