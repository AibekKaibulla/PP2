import psycopg2
from psycopg2 import sql
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

def get_or_create_user(cursor, username):
    """Retrieve an existing user or create a new one if not present."""
    cursor.execute("SELECT player_id FROM player WHERE username = %s;", (username,))
    user_id = cursor.fetchone()
    if user_id is None:
        cursor.execute("INSERT INTO player (username) VALUES (%s) RETURNING player_id;", (username,))
        user_id = cursor.fetchone()[0]  # Get the newly created user_id
        # cursor.connection.commit()  # Commit right after creation
        print("New player created with ID:", user_id)

    else:
        user_id = user_id[0]
        print("Welcome back player ID:", user_id)

    return user_id

def load_user_level_and_score(cursor, user_id):
    """Load the highest level and score for a user."""
    cursor.execute("SELECT MAX(level), MAX(score) FROM player_score WHERE player_id = %s;", (user_id,))
    result = cursor.fetchone()
    return result if result[0] is not None else (1, 0)

def save_game_state(cursor, user_id, score, level):
    print("Attempting to save game state for user_id:", user_id)
    cursor.execute("INSERT INTO player_score (player_id, score, level) VALUES (%s, %s, %s);", (user_id, score, level))
    cursor.connection.commit()  # Ensure changes are committed to the database