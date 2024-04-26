# main.py
from db.schema import create_phonebook_table
from operations.insertions import insert_contact, insert_contacts_from_csv
from operations.updates import update_contact_name, update_contact_phone
from operations.deletions import delete_contact_by_name, delete_contact_by_phone
from operations.queries import get_all_contacts, get_contact_by_name
from utils.csv_loader import load_contacts_from_csv

def main_menu():
    print("\nPhoneBook Application")
    print("1. Add New Contact")
    print("2. Upload Contacts from CSV")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View All Contacts")
    print("6. Search Contact by Name")
    print("7. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    create_phonebook_table()  # Ensure the database table is ready
    
    while True:
        choice = main_menu()
        
        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            insert_contact(name, phone)
        
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
            print("Exiting the application.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
