contacts = {}

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print(f" Contact '{name}' added successfully!")

def view_contacts():
    if not contacts:
        print(" No contacts found.")
    else:
        print("\n Contact List:")
        for name, details in contacts.items():
            print(f"- {name} | {details['phone']}")

def search_contact():
    search = input("Enter Name or Phone to Search: ")
    found = False
    for name, details in contacts.items():
        if search.lower() == name.lower() or search == details['phone']:
            print("\n🔍 Contact Found:")
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            found = True
            break
    if not found:
        print("❌ Contact not found.")

def update_contact():
    name = input("Enter the Name of the contact to update: ")
    if name in contacts:
        print("Enter new details (leave blank to keep old value):")
        phone = input(f"Phone ({contacts[name]['phone']}): ") or contacts[name]['phone']
        email = input(f"Email ({contacts[name]['email']}): ") or contacts[name]['email']
        address = input(f"Address ({contacts[name]['address']}): ") or contacts[name]['address']

        contacts[name] = {"phone": phone, "email": email, "address": address}
        print(f"✅ Contact '{name}' updated successfully!")
    else:
        print("❌ Contact not found.")

def delete_contact():
    name = input("Enter the Name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"🗑️ Contact '{name}' deleted successfully!")
    else:
        print("❌ Contact not found.")

# Main Menu
while True:
    print("\n===== Contact Book Menu =====")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print(" Exiting Contact Book. Goodbye!")
        break
    else:
        print(" Invalid choice! Please select between 1-6.")
