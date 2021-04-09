import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('cadastro.db')
        self.cursor = self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

    def criar_database(self):
        db.cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL,
        descricao VARCHAR(200) NOT NULL,
        valor FLOAT NOT NULL)
        ;'''
        )

        db.cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS produto_categoria(
            produto_id INTEGER,
            categoria_id INTEGER,
            FOREIGN KEY(produto_id) REFERENCES produtos(id),
            FOREIGN KEY(categoria_id) REFERENCES categorias(id)
        );
        '''
        )

        db.cursor.execute(
        '''         
        CREATE TABLE IF NOT EXISTS categorias(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL,
        descricao VARCHAR(100) NOT NULL
        );'''
        )
        db.commit()

db = Database()
db.criar_database()
