def display_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def add_contact(contacts):
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    contacts[name] = {"Phone": phone, "Email": email}
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts in the book.")
    else:
        print("\nContacts:")
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['Phone']}")
            print(f"Email: {info['Email']}")
            print("")

def search_contact(contacts):
    name = input("Enter the name to search: ")
    if name in contacts:
        print("\nContact found:")
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['Phone']}")
        print(f"Email: {contacts[name]['Email']}")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main():
    contacts = {}
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
