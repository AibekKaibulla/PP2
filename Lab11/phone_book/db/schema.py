from .connection import create_connection

def create_phonebook_table():
    conn = create_connection()
    cursor = conn.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        name VARCHAR(128) NOT NULL,
        phone VARCHAR(20) NOT NULL
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    conn.close()
