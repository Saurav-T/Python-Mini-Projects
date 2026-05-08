import random
import string

def menu():
    print("\n===== Password Generator and Manager =====")
    print("1. Generate Password")
    print("2. Exit")

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password

def main():
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            try:
                length = int(input("Enter the required password length: "))
                if length <= 0:
                    print("Password length must be greater than 0")
                else:
                    password = generate_password(length)
                    print(f"Generated Password: {password}")
            except ValueError:
                print("Enter a valid number")
        elif choice == "2":
            print("Closing..")
            break
        else:
            print("Enter a valid choice.")

main()


