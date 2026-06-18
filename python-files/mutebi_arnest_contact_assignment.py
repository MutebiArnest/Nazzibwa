
contacts = []

def valid_phone(phone):
    for char in phone:
        if not (char.isdigit() or char == "-"):
            return False
    return True

def valid_email(email):
    if email == "":
        return True  
    return "@" in email and "." in email


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    if not valid_phone(phone):
        print("Error: Phone number should contain only digits and hyphens.")
        return
    if not valid_email(email):
        print("Error: Invalid email address.")
        return
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    print("Contact added successfully!")


def view_contact():
    name = input("Enter the contact name: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Contact Details")
            print("Name :", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            return
    print("Contact not found.")

def update_contact():
    name = input("Enter the contact name to update: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            new_phone = input("Enter new phone: ")
            if not valid_phone(new_phone):
                print("Error: Invalid phone number.")
                return
            new_email = input("Enter new email: ")
            if not valid_email(new_email):
                print("Error: Invalid email.")
                return
            contact["phone"] = new_phone
            contact["email"] = new_email
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter the contact name to delete: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def search_contacts():
    keyword = input("Enter name, phone, or email to search: ").lower()
    found = False
    print("Search Results")
    for contact in contacts:
        if (
            keyword in contact["name"].lower()
            or keyword in contact["phone"].lower()
            or keyword in contact["email"].lower()
        ):
            print("Name :", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            found = True
    if not found:
        print("No matching contacts found.")

def list_all_contacts():
    if len(contacts) == 0:
        print("No contacts available.")
        return
    print("All Contacts")
    for contact in contacts:
        print("Name :", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])

def main():
    while True:
        print(" Contact Manager Menu")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")
        choice = input("Choose an option (1-7): ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            search_contacts()
        elif choice == "6":
            list_all_contacts()
        elif choice == "7":
            print("Thank you for using Contact Manager!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")
main()