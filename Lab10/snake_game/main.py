import sys
from db.database import connect_db, get_or_create_user
from game.gamelogic import SnakeGame

def main():
    # Connect to the database
    try:
        connection = connect_db()
        cursor = connection.cursor()

        # Get or create a user
        username = input("Please enter your username to start playing: ")
        user_id = get_or_create_user(cursor, username)
        cursor.close()
        connection.close()

        # Start the game with the user ID
        game = SnakeGame(user_id)
        game.run()
    
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
