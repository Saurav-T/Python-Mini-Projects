import json

FILE = "data/contacts.json"
def menu():
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Update Contact")
    print("6. Exit")

def load_contacts():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []
    
def save_contacts(contacts):
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact():
    contacts = load_contacts()
    name = input("Enter Contact Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")
    contacts.append({
        "name" : name,
        "phone" : phone,
        "email" : email
    })

    save_contacts(contacts)
    print("Contact Saved Successfully!")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return
    else:
        for i, c in enumerate(contacts, start=1):
            print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")

def search_contact():
    contacts = load_contacts()
    query = input("Enter a name to search: ").lower()
    found = False
    for c in contacts:
        if query in c['name'].lower():
            print(f"Found: {c['name']} | {c['phone']} | {c['email']}")
            found = True

    if not found:
        print("No contact found.")

def delete_contact():
    contacts = load_contacts()
    name = input("Enter name of contact to delete: ")
    new_contacts = [c for c in contacts if c['name'] != name]

    if len(new_contacts) == len(contacts):
        print("Contact not found.")
    else:
        print("Contact deleted sucessfully.")
        save_contacts(new_contacts)

def update_contact():
    contacts = load_contacts()

    name = input("Enter name of contact to update: ").strip().lower()

    found = False

    for c in contacts:
        if c["name"].strip().lower() == name:
            found = True

            print("Contact found!")

            c["phone"] = input("Enter new phone number: ").strip()
            c["email"] = input("Enter new email: ").strip()

            save_contacts(contacts)
            print("Contact updated successfully.")
            return

    print("No contact found.")
    

def main():
    while True:
        menu()
        choice = input("Enter Choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            update_contact()
        elif choice == "6":
            print("Closing....")
            break
        else:
            print("Enter a valid choice")

main()
