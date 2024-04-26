import psycopg2
from psycopg2 import OperationalError

def create_connection():
    try:
        conn = psycopg2.connect(
            dbname="phone_book",
            user="postgres",
            password="postgresql123",
            host="localhost",
            port="5432"
        )
        return conn
    except OperationalError as e:
        print(f"The error '{e}' occured")