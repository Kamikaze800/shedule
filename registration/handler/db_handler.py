import sqlite3
import os
import sys

import main_window

def login(login, passw, signal):
    con = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), 'users')))
    cur = con.cursor()

    # Проверяем есть ли такой пользователь
    cur.execute(f'SELECT * FROM users WHERE name="{login}";')
    value = cur.fetchall()

    if value != [] and value[0][2] == passw:
        signal.emit('Успешная авторизация!')
        abs_path = os.path.abspath('main_window_start.py')
        os.system(f'python {abs_path}')
        # sys.exit()
        # os.system('python D:\\work\\shedule\\main_window.py')
    else:
        signal.emit('Проверьте правильность ввода данных!')

    cur.close()
    con.close()



def register(login, passw, signal):
    con = sqlite3.connect('handler/users')
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
