import json
from json import JSONDecodeError

ACCOUNTS = "data/accounts.json"
def menu():
    print("\n===== BANKING SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")

def load_accounts():
    try:
        with open(ACCOUNTS, 'r') as f:
            return json.load(f)
    except (JSONDecodeError, FileNotFoundError) :
        return []
    
def save_accounts(accounts):
    with open(ACCOUNTS, 'w') as f:
        json.dump(accounts, f, indent=4)

def create_account():
    data = load_accounts()
    try:
        name = input("Enter an account name: ")
        initial_balance = float(input("Enter initial balance: "))

        data.append({
            "name": name,
            "balance": initial_balance,
            "transactions": [f"Account created with {initial_balance}"]
        })

        save_accounts(data)
        print("Account created successfully!")
    except ValueError:
        print("Enter a valid value.") 

   
def deposit():
    data = load_accounts()
    name = input("Enter account name: ")

    for acc in data:
        if acc["name"].lower() == name.lower():
            amount = float(input("Enter deposit amount: "))

            acc["balance"] += amount
            acc["transactions"].append(f"Deposited {amount}")

            save_accounts(data)
            print("Deposit successful!")
            return

    print("Account not found.")

def withdraw():
    data = load_accounts()
    name = input("Enter account name: ")

    for acc in data:
        if acc["name"].lower() == name.lower():
            amount = float(input("Enter withdraw amount: "))

            if amount > acc["balance"]:
                print("Insufficient balance!")
                return

            acc["balance"] -= amount
            acc["transactions"].append(f"Withdrew {amount}")

            save_accounts(data)
            print("Withdrawal successful!")
            return

    print("Account not found.")

def check_balance():
    data = load_accounts()
    name = input("Enter account name: ")

    for acc in data:
        if acc["name"].lower() == name.lower():
            print(f"Balance: {acc['balance']}")
            return

    print("Account not found.")

def history():
    data = load_accounts()
    name = input("Enter account name: ")

    for acc in data:
        if acc["name"].lower() == name.lower():
            print("\n--- Transactions ---")
            for t in acc["transactions"]:
                print(t)
            return

    print("Account not found.")

def main():
    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            history()
        elif choice == "6":
            break
        else:
            print("Invalid choice")

main()

