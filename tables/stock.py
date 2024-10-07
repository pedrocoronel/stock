from mysql09 import connection

def insert_data(name, price, validity, quantity):
    con, cur = connection()
    try:
        cur.execute("""
            INSERT INTO stock (name, price, validity, quantity) 
            VALUES (?, ?, ?, ?);""", (name, price, validity, quantity))
        con.commit()
    except Exception as e:
        print(f"log [stock/insert_data]: {e}\n")
    finally:
        con.close() 