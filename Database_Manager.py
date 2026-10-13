import sqlite3 as sql
from datetime import datetime

class Database_Manager:

    def __init__(self):

        self.DB = sql.connect("Currencies_data.db")
        self.cursor = self.DB.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS currency_data(
                                                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                        symbol TEXT NOT NULL,
                                                                        price FLOAT NOT NULL,
                                                                        date INTEGER NOT NULL)''')
        self.DB.commit()
        self.DB.close()


    def save_data(self, data):

        with sql.connect("Currencies_data.db") as DB:

            current_date = datetime.now()
            current_data_code = float(f"{current_date.year}{current_date.month}{current_date.day}.{current_date.hour}{current_date.minute}{current_date.second}")

            for i in range(len(data["currencies"])):

                DB.execute('''INSERT INTO currency_data
                                                        (symbol, price, date)VALUES(?, ?, ?)''',   
                                                        (data["currencies"][i], data["prices"][i], current_data_code))


    def get_data(self):

        pass


    def edit_data(self):

        pass