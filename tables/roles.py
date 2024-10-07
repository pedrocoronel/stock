from mysql09 import connection

def insert_data(username, password, nivel):
    con, cur = connection()
    try:
        cur.execute("""
            INSERT INTO roles (username, password, nivel) 
            VALUES (%s, %s, %s);""", (username, password, nivel))
        con.commit()

    except Exception as e:
        print(f"log [roles/insert_data]: {e}\n")
    finally:
        con.close()

def read_data(username, password):
    con, cur = connection()
    try:
        cur.execute("""
            SELECT id FROM roles
            WHERE username = %s AND password = %s;""", (username, password))
        datas = cur.fetchall() 
        return datas
    except Exception as e:
        print(f"log [roles/read_data]: {e}\n")
    finally:
        con.close()

def delete_data(username):
    con, cur = connection()
    try:            
        cur.execute("""
            DELETE FROM roles
            WHERE username = %s;""", (username,))
        con.commit()
    except Exception as e:
        print(f"log [roles/delete_data]: {e}\n")
    finally:
        con.close()
