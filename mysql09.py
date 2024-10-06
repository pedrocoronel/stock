import mysql.connector
from mysql.connector import Error
from os import getenv
from dotenv import load_dotenv

load_dotenv()

def connection():
    con = None
    try:
        con = mysql.connector.connect(
            host='localhost',
            user=getenv('mysql_user'),
            password=getenv('mysql_password'),
            database=getenv('mysql_database')
        )

        if con.is_connected():
            print("Conexão bem-sucedida ao banco de dados.")
            return con
    except Error as e:
        print(f"log [mysql09/conectin]: {e}")

connection()

