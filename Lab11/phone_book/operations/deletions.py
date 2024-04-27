# operations/deletions.py
from db.connection import create_connection

def delete_contact_by_name(name):
    """Delete a contact by name."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM contacts WHERE name = %s", (name,))
        conn.commit()
        print("Contact deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def delete_contact_by_phone(phone):
    """Delete a contact by phone number."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM contacts WHERE phone = %s", (phone,))
        conn.commit()
        print("Contact deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
