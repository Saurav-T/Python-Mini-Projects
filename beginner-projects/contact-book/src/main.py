import json

FILE = "data/contacts.json"
def menu():
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

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

def main():
    while True:
        menu()
        choice = input("Enter Choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            print("Feature in Development.")
        elif choice == "4":
            print("Feature in Development.")
        elif choice == "5":
            print("Closing....")
            break
        else:
            print("Enter a valid choice")

main()
