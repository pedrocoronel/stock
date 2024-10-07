import mysql.connector
from mysql.connector import Error
from os import getenv
from dotenv import load_dotenv

load_dotenv()

def connection():
    try:
        con = mysql.connector.connect(
            host='localhost',
            user=getenv('mysql_user'),
            password=getenv('mysql_password'),
            database=getenv('mysql_database')
        )
        cur = con.cursor()
        return con, cur
    except Error as e:
        print(f"log [mysql09/conection]: {e}")
        return None, None 

con, cur = connection()
if con and cur:
    print("Connection successful!")
else:
    print("Connection to the database failed.")
