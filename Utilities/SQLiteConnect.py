import sqlite3


class SQLiteConnect:
    __instance = None

    def __init__(self, db_name):
        self.sqlite_connection = sqlite3.connect(db_name)
        self.sqlite_handler = self.sqlite_connection.cursor()

    @classmethod
    def getConnect(cls, db_name):
        if not cls.__instance:
            try:
                sqlite_connection = sqlite3.connect(db_name)
            except sqlite3.Error as error:
                print(error)
            finally:
                if sqlite_connection:
                    cls.__instance = SQLiteConnect(db_name)
                    sqlite_connection.close()
                    return cls.__instance
                else:
                    return None
        else:
            return cls.__instance
