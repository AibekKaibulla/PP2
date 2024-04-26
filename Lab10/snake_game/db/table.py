import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def connect_db():
    """Establish a connection to the PostgreSQL database."""
    connection = psycopg2.connect(
        dbname="snake",
        user="postgres",
        password="postgresql123",
        host="localhost",
        port="5432"
    )
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    return connection

def create_tables():
    """Create database tables directly via psycopg2, avoiding reserved keywords."""
    commands = [
        """
        CREATE TABLE IF NOT EXISTS player (
            player_id SERIAL PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS player_score (
            score_id SERIAL PRIMARY KEY,
            player_id INT NOT NULL,
            score INT NOT NULL,
            level INT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (player_id) REFERENCES player (player_id)
        )
        """
    ]
    conn = connect_db()
    cursor = conn.cursor()
    try:
        for command in commands:
            cursor.execute(command)
        print("Tables created successfully.")
    except Exception as e:
        print(f"An error occurred while creating tables: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    create_tables()
