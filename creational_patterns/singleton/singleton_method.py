import sqlite3

conn = sqlite3.connect('singelton.db')

cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS Users(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Age INTEGER);')
conn.commit()
class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class DataBase(metaclass=SingletonMeta):
    def take_info(self, id):
        cur.execute('SELECT * FROM Users WHERE id  = ?', (id,))
        return cur.fetchone()
    def delete_info(self, id):
        cur.execute('DELETE FROM Users WHERE id = ?', (id,))
        conn.commit()
    def write_new_info(self, name, age):
        cur.execute('INSERT INTO Users (Name, Age) VALUES (?, ?)', (name, age))
        conn.commit()


class sometink_else(metaclass=SingletonMeta):
    def function(self):
        pass


if __name__ == "__main__":
    user_1 = DataBase()
    user_1.write_new_info("Tim", 16)
    user_1.write_new_info('Bob', 52)

    user_2 = DataBase()
    print(user_2.take_info(2))

    user_3 = DataBase()
    user_3.delete_info(8)

    user_4 = sometink_else()

    print(user_1 is user_2)
    print(user_1 is user_3)
    print(user_2 is user_3)
    print(user_4 is user_1)