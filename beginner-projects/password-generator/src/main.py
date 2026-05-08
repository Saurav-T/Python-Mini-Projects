import random
import string
import json

FILE = "data/passwords.json"


def load_passwords():
    try:
        with open(FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def view_passwords(passwords):
    if not passwords:
        print("No Passwords Saved Yet.")
        return
    else:
        for i, info in enumerate(passwords, start=1):
            print(f"""{i}.
                \tWebsite: {info['website']}
                \tUsername: {info['username']}
                \tPassword: {info['password']}""")


def save_passwords(passwords):
    with open(FILE, 'w') as f:
        json.dump(passwords, f, indent=4)


def add_password(passwords, password):
    website = input("Website: ")
    username = input("Username: ")

    passwords.append({
        "website": website,
        "username": username,
        "password": password
    })

    save_passwords(passwords)


def menu():
    print("\n===== Password Generator and Manager =====")
    print("1. Generate Password")
    print("2. Save Password")
    print("3. View Passwords")
    print("4. Exit")


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


def main():
    passwords = load_passwords()
    current_password = None
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            try:
                length = int(input("Enter the required password length: "))
                if length <= 0:
                    print("Password length must be greater than 0")
                else:
                    current_password = generate_password(length)
                    print(f"Generated Password: {current_password}")
            except ValueError:
                print("Enter a valid number")
        elif choice == "2":
            if current_password:
                add_password(passwords, current_password)
                print("Password Saved Successfully")
            else:
                print("No generated password found. Generate one first.")
        elif choice == "3":
            view_passwords(passwords)
        elif choice == "4":
            print("Closing..")
            break
        else:
            print("Enter a valid choice.")


main()
