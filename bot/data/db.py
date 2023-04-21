import sqlite3 as sq
import time



def connected_db():
    global base, cursor
    base = sq.connect('users_db.db')
    cursor = base.cursor()
    if base:
        print('Base conected')
    base.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, user_name TEXT, time_sub INTEGER DEFAULT 0 NOT NULL)")
    base.commit()

def days_to_seconds(days):
    return days*24*60*60

def time_sub_day(get_time):
    time_now = int(time.time())
    midle_time = int(get_time) - time_now

    if midle_time <= 0:
        return False
    else:
        return True


async def add_user(user_id, user_name):
    with base:
        cursor.execute("INSERT INTO users (user_id, user_name) VALUES (?,?)", (user_id, user_name,))
        base.commit()


async def user_exist(user_id):
    with base:
        result = cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchall()
        return bool(len(result))

async def set_time_sub(user_id, time_sub):
    with base:
        return cursor.execute('UPDATE users SET time_sub = ? WHERE user_id = ?', (time_sub, user_id,))


async def get_time_sub(user_id):
    with base:
        result = cursor.execute("SELECT time_sub FROM users WHERE user_id = ?", (user_id,)).fetchall()
        for row in result:
            time_sub = int(row[0])
        return time_sub


async def get_sub_status(user_id):
    with base:
        result = cursor.execute("SELECT time_sub FROM users WHERE user_id = ?", (user_id,)).fetchall()
        for row in result:
            time_sub = int(row[0])
        
        if time_sub > int(time.time()):
            return True
        else:
            return False

async def get_user_list():
    with base:
        result = cursor.execute("SELECT user_id FROM users").fetchall()
        list_users = []
        for row in result:
            list_users.append(row[0])
        return list_users



async def get_user_data():
    with base:
        result = cursor.execute("SELECT * FROM users").fetchall()
        user_base = {}
        for row in result:
            user_base.update({row[0]: (row[1], row[2])})
        return user_base
