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
    Website: {info['website']}
    Username: {info['username']}
    Password: {info['password']}""")


def save_passwords(passwords):
    with open(FILE, 'w') as f:
        json.dump(passwords, f, indent=4)


def save_password(passwords, password=None):
    website = input("Website: ")
    username = input("Username: ")
    if password == None:
        password = input("Password: ")

    passwords.append({
        "website": website,
        "username": username,
        "password": password
    })

    save_passwords(passwords)


def menu():
    print("\n===== Password Generator and Manager =====")
    print("1. Generate Password")
    print("2. Save Generated Password")
    print("3. Save Manual Credentials")
    print("4. View Passwords")
    print("5. Check Password Strength")
    print("6. Delete Password")
    print("7. Exit")


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


def delete_password(passwords):
    view_passwords(passwords)
    try:
        index = int(input("Enter position to delete: "))
        if 1 <= index <= len(passwords):
            removed = passwords.pop(index - 1)
            save_passwords(passwords)
            print(
                f"Removed password as position {index} for {removed['website']}.")
        else:
            print("Invalid index")
    except ValueError:
        print("Enter a valid number")


def check_strength(password):
    has_upper = False
    has_lower = False
    has_digits = False
    has_special = False

    special_characters = string.punctuation

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digits = True
        elif ch in special_characters:
            has_special = True

    score = 0
    missing = []

    if len(password) >= 8:
        score += 1
    else:
        missing.append("Minimum 8 characters")

    if has_upper:
        score += 1
    else:
        missing.append("Uppercase Letters")

    if has_lower:
        score += 1
    else:
        missing.append("Lowercase Letters")

    if has_digits:
        score += 1
    else:
        missing.append("Digits")

    if has_special:
        score += 1
    else:
        missing.append("Special Characters")

    print(f"Strength: {score}/5")

    if score <= 2:
        print("Weak Password.")
    elif score <= 4:
        print("Medium Password.")
    else:
        print("Strong Password")

    if missing:
        print(f"Missing: {', '.join(missing)}")


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
                    print("Password length must be greater than 0.")
                else:
                    current_password = generate_password(length)
                    print(f"Generated Password: {current_password}")
            except ValueError:
                print("Enter a valid number.")
        elif choice == "2":
            if current_password:
                save_password(passwords, current_password)
                print("Password Saved Successfully.")
                current_password = None
            else:
                print("No generated password found. Generate one first.")
        elif choice == "3":
            save_password(passwords)
            print("Credentials saved successfully.")
        elif choice == "4":
            view_passwords(passwords)
        elif choice == "5":
            check_password = input("Enter a password to check it's strength: ")
            check_strength(check_password)
        elif choice == "6":
            delete_password(passwords)
        elif choice == "7":
            break
        else:
            print("Enter a valid choice.")


main()
