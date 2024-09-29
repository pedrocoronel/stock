from db import connection

def insert_data(username, password, nivel):
    con, cur = connection()
    try:
        cur.execute("""
            INSERT INTO roles (username, password, nivel) 
            VALUES (?, ?, ?);""", (username, password, nivel))
        con.commit()
    except Exception as e:
        print(f"Error inserting data: {e}")
    finally:
        con.close() 

def read_data(username, password):
    con, cur = connection()
    try:
        cur.execute("""
            SELECT username, password FROM roles
            WHERE username = ? AND password = ?;""", (username, password))
        datas = cur.fetchall() 
        return datas  # Retornar aqui evita que seja executado o finally antes
    except Exception as e:
        print(f"Error reading data: {e}")
        return []  # Retorna uma lista vazia em caso de erro
    finally:
        con.close() 

def delete_data(username):
    con, cur = connection()
    try:            
        cur.execute("""
            DELETE FROM roles
            WHERE username = ?;""", (username,))
        con.commit()
    except Exception as e:
        print(f"Error deleting data: {e}")
    finally:
        con.close()
