from mysql09 import connection

def insert_data(username, password, nivel):
    con, cur = connection()
    try:
        cur.execute("""
            INSERT INTO roles (username, password, nivel) 
            VALUES (?, ?, ?);""", (username, password, nivel))
        con.commit()
    except Exception as e:
        print(f"\nlog [roles/insert_data]: {e}")
    finally:
        con.close() 

def read_data(username, password):
    con, cur = connection()
    try:
        cur.execute("""
            SELECT id FROM roles
            WHERE username = ? AND password = ?;""", (username, password))
        datas = cur.fetchall() 
        return datas
    except Exception as e:
        print(f"\nlog [roles/read_data]: {e}")
    finally:
        con.close() 

def delete_data(username):
    con, cur = connection()
    try:            
        cur.execute("""
            DELETE FROM roles
            WHERE username = ?;""", (username))
        con.commit()
    except Exception as e:
        print(f"\nlog [roles/delete_data]: {e}")
    finally:
        con.close()
