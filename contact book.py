# Contact Manager Program

# Dictionary to store contacts
contacts = {}

def add_contact():
    """Add a new contact with details."""
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print(f"Contact '{name}' already exists!")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    address = input("Enter address: ").strip()
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    """Display a list of all contacts with names and phone numbers."""
    if not contacts:
        print("No contacts available.")
        return
    print("\n--- Contact List ---")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")

def search_contacts():
    """Search for contacts by name or phone number."""
    search_term = input("Enter name or phone number to search: ").strip()
    found = False
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term == details['phone']:
            print(f"\n--- Contact Found ---")
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            found = True
            break
    if not found:
        print("No contact found with that name or phone number.")

def update_contact():
    """Update details of an existing contact."""
    name = input("Enter the name of the contact to update: ").strip()
    if name not in contacts:
        print(f"Contact '{name}' not found.")
        return
    print(f"Current details for '{name}': {contacts[name]}")
    phone = input("Enter new phone number (press Enter to keep current): ").strip()
    email = input("Enter new email address (press Enter to keep current): ").strip()
    address = input("Enter new address (press Enter to keep current): ").strip()
    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email
    if address:
        contacts[name]['address'] = address
    print(f"Contact '{name}' updated successfully!")

def delete_contact():
    """Delete a contact."""
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found.")

def main_menu():
    """Main menu for interacting with the contact manager."""
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contacts List")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contacts()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
        
        # Ask user if they want to continue
        continue_choice = input("\nWould you like to perform another action? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Exiting Contact Manager. Goodbye!")
            break
if __name__ == "__main__":
    main_menu()