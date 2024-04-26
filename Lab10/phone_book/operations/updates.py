# operations/updates.py
from db.connection import create_connection

def update_contact_name(old_name, new_name):
    """Update a contact's name."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE contacts SET name = %s WHERE name = %s", (new_name, old_name))
        conn.commit()
        print("Contact name updated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def update_contact_phone(name, new_phone):
    """Update a contact's phone number."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE contacts SET phone = %s WHERE name = %s", (new_phone, name))
        conn.commit()
        print("Contact phone updated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
