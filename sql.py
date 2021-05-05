import sqlite3


def login(login, passw, signal):
    con = sqlite3.connect('users')
    cur = con.cursor()

    # ----------------Проверка пользователя--------------------
    cur.execute(f'SELECT * FROM users WHERE name="{login}";')
    value = cur.fetchall()

    if value != [] and value[0][2] == passw:
        signal.emit('Успешная авторизация!')
    else:
        signal.emit('Проверьте ввод')

    cur.close()
    con.close()


def register(login, password, signal):
    con = sqlite3.connect('users')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE name="{login}";')
    value = cur.fetchall()

    if value != []:
        signal.emit('Такое имя уже есть')

    elif value == []:
        cur.execute(f"INSERT INTO users (name, password) VALUES ('{login}', '{password}')")
        signal.emit('Вы успешно зарегистрированы!')
        con.commit()

    cur.close()
    con.close()
