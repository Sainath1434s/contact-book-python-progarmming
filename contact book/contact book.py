class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        self.contacts[name] = {'phone_number': phone_number, 'email': email, 'address': address}

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['phone_number']}")

    def search_contact(self, search_term):
        for name, details in self.contacts.items():
            if search_term in name or search_term == details['phone_number']:
                print(f"Name: {name}, Phone: {details['phone_number']}, Email: {details['email']}, Address: {details['address']}")
                return
        print("Contact not found.")

    def update_contact(self, name, phone_number=None, email=None, address=None):
        if name not in self.contacts:
            print("Contact not found.")
        else:
            contact = self.contacts[name]
            if phone_number:
                contact['phone_number'] = phone_number
            if email:
                contact['email'] = email
            if address:
                contact['address'] = address
            print("Contact updated successfully.")

    def delete_contact(self, name):
        if name not in self.contacts:
            print("Contact not found.")
        else:
            del self.contacts[name]
            print("Contact deleted successfully.")


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone_number, email, address)
            print("Contact added successfully.")
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == '4':
            name = input("Enter name of contact to update: ")
            phone_number = input("Enter new phone number (leave blank to keep existing): ")
            email = input("Enter new email (leave blank to keep existing): ")
            address = input("Enter new address (leave blank to keep existing): ")
            contact_book.update_contact(name, phone_number, email, address)
        elif choice == '5':
            name = input("Enter name of contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
