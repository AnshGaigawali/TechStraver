contacts = {}

def validate_phone_number(phone_number):
    return phone_number.isdigit() and len(phone_number) == 10

def validate_email(email):
    return '@' in email

def add_contact(name, phone_number, email):
    global contacts
    if name not in contacts:
        if validate_phone_number(phone_number) and validate_email(email):
            contacts[name] = {'phone_number': phone_number, 'email': email}
            contacts = dict(sorted(contacts.items()))  
            print("Contact '" + name + "' added successfully.")
        else:
            print("Invalid phone number or email format.")
    else:
        print("Contact '" + name + "' already exists.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print("Contact '" + name + "' deleted successfully.")
    else:
        print("Contact '" + name + "' does not exist.")

def get_contact_info(name):
    contact_info = contacts.get(name)
    if contact_info:
        print("Name: " + name)
        print("Phone Number: " + contact_info['phone_number'])
        print("Email: " + contact_info['email'])
    else:
        print("Contact '" + name + "' does not exist.")

def display_all_contacts():
    if contacts:
        print("All Contacts:")
        for name, contact_info in contacts.items():
            print("Name: " + name)
            print("Phone Number: " + contact_info['phone_number'])
            print("Email: " + contact_info['email'])
            print("--------------------")
    else:
        print("Contact book is empty.")

def menu():
    print("Menu:")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Get Contact Info")
    print("4. Display All Contacts")
    print("5. Exit")

while True:
    menu()
    ch = input("Enter your choice: ")

    if ch=='1':
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        add_contact(name, phone_number, email)
    elif ch=='2':
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif ch=='3':
        name = input("Enter name to get info: ")
        get_contact_info(name)
    elif ch=='4':
        display_all_contacts()
    elif ch=='5':
        print("-----Exiting-----")
        break
    else:
        print("Invalid choice")
