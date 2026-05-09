import sqlite3
from models.expense import Expense
def menu():
    print("\n===== Expense Manager =====")
    print("1. Add Expense")
    print("2. Show Expense")
    print("3. Exit")

conn = sqlite3.connect("src/database/expense.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    category TEXT,
    description TEXT,
    date TEXT          
    )
""")

conn.commit()
def add_expense(cursor):
    try:
        amount = float(input("Enter the expense amount: "))
        category = input("Enter the category of expense: ")
        description = input("Enter the description of expense: ")
        date = input("Enter the date of expense (YYYY-MM-DD): ")

        expense = Expense(amount, category, description, date)

        cursor.execute("""
        INSERT INTO expenses (amount, category, description, date)
        VALUES (?,?,?,?)
        """, expense.to_tuple())

        conn.commit()

        print("Expense added successfully.")
    except ValueError:
        print("Enter a valid input.")

def show_expenses(cursor):
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    for row in rows:
        expense = Expense(row[1], row[2], row[3], row[4])
        print(expense)

def main():
    while True:
        menu()
        choice = input("Enter a choice: ")
        if choice == "1":
            add_expense(cursor)
        elif choice == "2":
            show_expenses(cursor)
        elif choice == "3":
            print("Closing..")
            break
        else:
            print("Enter a valid choice.")

main()

