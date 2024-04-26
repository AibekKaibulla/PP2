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
