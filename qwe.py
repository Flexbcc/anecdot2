import sqlite3

try:
    sqlite_connection = sqlite3.connect('anekdots.db')
    sqlite_create_table_query = '''CREATE TABLE anekdots (
                                id INTEGER PRIMARY KEY,
                                text TEXT NOT NULL UNIQUE,
                                date text NOT NULL,
                                publish text NOT NULL,
                                interesting TEXT NOT NULL,
                                view TEXT NOT NULL);'''

    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print("Таблица SQLite создана")

    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")