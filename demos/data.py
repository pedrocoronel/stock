import sqlite3

def connection():
    con = sqlite3.connect("file.db")
    cur = con.cursor()
    try:
        yield con, cur
    finally:
        con.close()

class Roles:
    @staticmethod
    def create_table():
        with connection() as (con, cur):
            try:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS roles (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        password TEXT
                    );""")
                con.commit()
            finally:
              con.close()  

    @staticmethod
    def insert_data(username, password):
        with connection() as (con, cur):
            try:
                cur.execute("""
                    INSERT INTO roles (username, password) 
                    VALUES (?, ?);""", (username, password))
                con.commit()
            finally:
              con.close() 

    @staticmethod
    def read_data():
        with connection() as (con, cur):
            try:
                cur.execute("SELECT * FROM roles;")
                rows = cur.fetchall() 
                return rows
            finally:
              con.close() 

    @staticmethod
    def delete_data(username):
        with connection() as (con, cur):
            try:            
                cur.execute("""
                    DELETE FROM roles
                    WHERE username = ?;""", (username,))
                con.commit()
            finally:
              con.close()


class stock:
    @staticmethod
    def create_table():
        with connection() as (con, cur):
            cur.execute("""
                CREATE TABLE IF NOT EXISTS stock (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price INTEGER NOT NULL,
                    validity TEXT,
                    quantity INTEGER NOT NULL
                );""")
            con.commit()

    @staticmethod
    def insert_data(name, price, validity, quantity):
        with connection() as (con, cur):
            cur.execute("""
                INSERT INTO stock (name, price, validity, quantity) 
                VALUES (?, ?, ?, ?);""", (name, price, validity, quantity))
            con.commit()
