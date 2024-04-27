# operations/insertions.py
import json
from db.connection import create_connection

def insert_contact(name, phone):
    """Insert a single contact into the database."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        print("Contact inserted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def insert_contacts_from_csv(file_path):
    """Insert multiple contacts from a CSV file."""
    import csv
    conn = create_connection()
    try:
        cursor = conn.cursor()
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                cursor.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (row[0], row[1]))
            conn.commit()
            print("Contacts inserted from CSV successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def upsert_contact(name, phone):
    """Insert a new contact or update the phone number if the contact already exists."""
    conn = create_connection()
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM contacts WHERE name = %s", (name,))
        result = cursor.fetchone()

        if result:
            # Contact exists, update the phone number
            cursor.execute("UPDATE contacts SET phone = %s WHERE name = %s", (phone, name))
        else:
            # Contact does not exist, insert new
            cursor.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
        
        conn.commit()
        action = "updated" if result else "inserted"
        print(f"Contact {action} successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def insert_multiple_contacts_via_procedure(contacts):
    conn = create_connection()
    cursor = conn.cursor()
    # Convert the list of contact dictionaries to a JSON string
    contacts_json = json.dumps(contacts)
    try:
        cursor.callproc('insert_multiple_contacts', [contacts_json])
        conn.commit()
        
        incorrect_contacts = cursor.fetchall()
        if incorrect_contacts:
            print("Some contacts were incorrect and not inserted:", incorrect_contacts)
        else:
            print("All contacts were inserted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()