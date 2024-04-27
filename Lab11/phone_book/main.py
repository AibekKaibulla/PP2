# main.py
import json
from db.schema import create_phonebook_table
from operations.insertions import insert_contact, insert_contacts_from_csv, upsert_contact, insert_multiple_contacts_via_procedure
from operations.updates import update_contact_name, update_contact_phone
from operations.deletions import delete_contact_by_name, delete_contact_by_phone
from operations.queries import get_all_contacts, get_contact_by_name, search_contacts, fetch_contacts_with_pagination
from utils.csv_loader import load_contacts_from_csv

def main_menu():
    print("\nPhoneBook Application")
    print("1. Add New Contact")
    print("2. Upload Contacts from CSV")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View All Contacts")
    print("6. Search Contact by Name")
    print("7. Search Contacts by Pattern")
    print("8. Insert multiple data")
    print("q. View Contacts with Pagination")
    print("9. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    create_phonebook_table()  # Ensure the database table is ready
    
    while True:
        choice = main_menu()
        
        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            upsert_contact(name, phone)

        
        elif choice == '2':
            filepath = input("Enter CSV file path: ")
            load_contacts_from_csv(filepath)
        
        elif choice == '3':
            name = input("Enter contact name to update: ")
            new_name = input("Enter new name (leave blank if no change): ")
            new_phone = input("Enter new phone (leave blank if no change): ")
            if new_name:
                update_contact_name(name, new_name)
            if new_phone:
                update_contact_phone(name, new_phone)
        
        elif choice == '4':
            name = input("Enter contact name to delete: ")
            delete_contact_by_name(name)
        
        elif choice == '5':
            get_all_contacts()
        
        elif choice == '6':
            name = input("Enter contact name to search: ")
            get_contact_by_name(name)
        
        elif choice == '7':
            pattern = input("Enter search pattern: ")
            search_contacts(pattern)

        elif choice == '8':
            # Example input format: 
            contacts_str = input("Enter list of contacts in JSON format: ")
            try:
                contacts_list = json.loads(contacts_str)
                insert_multiple_contacts_via_procedure(contacts_list)
            except json.JSONDecodeError:
                print("Invalid JSON format.")
        
        elif choice == 'q':
            try:
                page_number = int(input("Enter the page number: "))
                contacts_per_page = int(input("Enter the number of contacts per page: "))
                contacts = fetch_contacts_with_pagination(page_number, contacts_per_page)
                for contact in contacts:
                    print(contact)
            except ValueError:
                print("Please enter valid integers for page number and page size.")
        elif choice == '9':
            print("Exiting the application.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
