# utils/csv_loader.py
import csv
from operations.insertions import insert_contact

def load_contacts_from_csv(file_path):
    """Load contacts from a CSV file and insert them into the database."""
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if validate_contact(row[0], row[1]):
                insert_contact(row[0], row[1])
            else:
                print(f"Invalid data: {row}")

def validate_contact(name, phone):
    """Validate contact details."""
    if len(name) > 0 and len(phone) > 0:  # Simple validation
        return True
    return False
