# operations/queries.py
from db.connection import create_connection

def get_all_contacts():
    """Fetch all contacts."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, phone FROM contacts")
        contacts = cursor.fetchall()
        for contact in contacts:
            print(contact)
    finally:
        cursor.close()
        conn.close()

def get_contact_by_name(name):
    """Fetch a contact by name."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, phone FROM contacts WHERE name = %s", (name,))
        contact = cursor.fetchone()
        print(contact)
    finally:
        cursor.close()
        conn.close()

def search_contacts(pattern):
    """Search for contacts based on a pattern in their name, surname, or phone number."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        # Using ILIKE for case-insensitive search, and %% for wildcards in psycopg2
        query = """
        SELECT id, name, phone FROM contacts
        WHERE name ILIKE %s OR phone ILIKE %s;
        """
        wildcard_pattern = f"%{pattern}%"
        cursor.execute(query, (wildcard_pattern, wildcard_pattern))
        matches = cursor.fetchall()
        for match in matches:
            print(match)
    finally:
        cursor.close()
        conn.close()

def fetch_contacts_with_pagination(page, page_size):
    """Fetch contacts with pagination.
    
    Args:
        page (int): The current page number.
        page_size (int): The number of contacts per page.

    Returns:
        list: A list of contacts for the specified page.
    """
    # Calculate the offset
    offset = (page - 1) * page_size
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, phone FROM contacts ORDER BY id LIMIT %s OFFSET %s", (page_size, offset))
        contacts = cursor.fetchall()
        return contacts
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    finally:
        cursor.close()
        conn.close()