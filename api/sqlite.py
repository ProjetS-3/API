import sqlite3

DB_PATH = "../db/db.sqlite"


def create(id, product_id, quantity):
    connect = sqlite3.connect(DB_PATH)
    cursor = connect.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS dbtable (
                        id TEXT PRIMARY KEY,
                        productId INTEGER,
                        quantity INTEGER)''')
    cursor.execute("INSERT INTO dbtable (id, productId, quantity) VALUES (?, ?, ?)", (id, product_id, quantity))
    connect.commit()


def get_all():
    connect = sqlite3.connect(DB_PATH)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM dbtable")
    rows = cursor.fetchall()
    connect.close()
    return rows


def get_from_id(id):
    connect = sqlite3.connect(DB_PATH)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM dbtable WHERE id=?", (id,))
    row = cursor.fetchone()
    connect.close()
    return row


def delete_from_id(id):
    connect = sqlite3.connect(DB_PATH)
    cursor = connect.cursor()
    cursor.execute("DELETE FROM dbtable WHERE id=?", (id,))
    connect.commit()
    connect.close()
