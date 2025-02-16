class Contact:

# A class to represent a contact
    
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email} | {self.address}"


class ContactManager:

# A class to manage a list of contacts
    
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
# Adds a new contact to the list

        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"\nContact '{name}' added successfully.")

    def view_contacts(self):
# Displays all saved contacts
        
        if not self.contacts:
            print("\nNo contacts available.")
        else:
            print("\nContact List:")
            for contact in self.contacts:
                print(contact)

    def search_contact(self, keyword):
# Searches contacts by name or phone number
        
        results = [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword in contact.phone]
        
        if results:
            print("\nSearch Results:")
            for contact in results:
                print(contact)
        else:
            print("\nNo contacts found.")

    def update_contact(self, name, new_phone=None, new_email=None, new_address=None):
# Updates contact details based on the provided name
        
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
                print(f"\nContact '{name}' updated successfully.")
                return
        print(f"\nContact '{name}' not found.")

    def delete_contact(self, name):
# Deletes a contact by name
        
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"\nContact '{name}' deleted successfully.")
                return
        print(f"\nContact '{name}' not found.")


def show_menu():
# Displays the menu options
    
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")


def main():
# Main function to run the Contact Management System
    
    manager = ContactManager()

    while True:
        show_menu()
        choice = input("\nChoose an option: ")

        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            manager.add_contact(name, phone, email, address)

        elif choice == '2':
            manager.view_contacts()

        elif choice == '3':
            keyword = input("Enter Name or Phone Number to Search: ")
            manager.search_contact(keyword)

        elif choice == '4':
            name = input("Enter the Name of the Contact to Update: ")
            new_phone = input("Enter New Phone Number (Press Enter to Skip): ")
            new_email = input("Enter New Email (Press Enter to Skip): ")
            new_address = input("Enter New Address (Press Enter to Skip): ")
            manager.update_contact(name, new_phone or None, new_email or None, new_address or None)

        elif choice == '5':
            name = input("Enter the Name of the Contact to Delete: ")
            manager.delete_contact(name)

        elif choice == '6':
            print("\nExiting Contact Management System. Goodbye!")
            break

        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()

