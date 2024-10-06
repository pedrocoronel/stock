'''
Old version DATABASE\n
End of support 06/10/24
'''

import sqlite3

def connection():
    con = sqlite3.connect("file.db")
    cur = con.cursor()
    return con, cur

def table_roles():
    con, cur = connection()
    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS roles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                nivel TEXT NOT NULL
            );""")
        con.commit()
    except Exception as e:
        print(f"\nlog [create_table_roles]\n{e}")
    finally:
        con.close() 

def table_stock():
    con, cur = connection()
    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS stock (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price INTEGER NOT NULL,
                validity TEXT,
                quantity INTEGER NOT NULL
            );""")
        con.commit()
    except Exception as e:
        print(f"\nlog [create_table_stock]\n{e}")
    finally:
        con.close() 

def create_tables():
    table_roles()
    table_stock()