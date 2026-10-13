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
            current_data_code = float(f"{current_date.year}{current_date.month:02d}{current_date.day:02d}.{current_date.hour:02d}{current_date.minute:02d}{current_date.second:02d}")

            for i in range(len(data["currencies"])):

                DB.execute('''INSERT INTO currency_data
                                                        (symbol, price, date)VALUES(?, ?, ?)''',   
                                                        (data["currencies"][i], data["prices"][i], current_data_code))


    def get_data(self, specified_date = None):

        with sql.connect("Currencies_data.db") as DB:

            data = DB.execute('SELECT * FROM currency_data').fetchall()

        all_data = {}

        currencies = []
        prices = []
        dates = []

        for row in data:

            currencies.append(row[1])
            prices.append(row[2])
            dates.append(row[3])

        all_data["currencies"] = currencies
        all_data["prices"] = prices
        all_data["dates"] = dates

        newest_data = {"currencies" : [data[-1][1], data[-2][1]],
                        "prices" : [data[-1][2], data[-2][2]],
                        "dates" : [data[-1][3], data[-2][3]]}

        return newest_data, all_data
        
            
    def edit_data(self):

        pass