import sqlite3
db = sqlite3.connect("bot.sqlite3")
cursor = db.cursor()


def sql_create():
    #global db, cursor
    if db:
        print('База данных подключена!')

    db.execute('CREATE TABLE IF NOT EXISTS mentors'
                "(name TEXT, id INTEGER PRIMARY KEY, "
                "direct TEXT, age INTEGER, Mgroup INTEGER)")
    db.commit()


async def sgl_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO mentors VALUES (?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()
