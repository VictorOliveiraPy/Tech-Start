import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('cadastro.db')
        self.cursor = self.conn.cursor()

    def commit(self):
        self.conn.commit()
        self.close()