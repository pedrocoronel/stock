from db import connection

def insert_data(name, price, validity, quantity):
    con, cur = connection()
    try:
        cur.execute("""
            INSERT INTO stock (name, price, validity, quantity) 
            VALUES (?, ?, ?, ?);""", (name, price, validity, quantity))
        con.commit()
    finally:
        con.close() 