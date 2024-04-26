# operations/insertions.py
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
