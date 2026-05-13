# Expense Tracker Application

A simple command-line Expense Manager built using Python and SQLite.
This project demonstrates how to use a database with Python, apply object-oriented design, and perform basic CRUD operations.

---

## Features

- Add new expense
- View all expenses
- Store data using SQLite database
- Use a model class (Expense) for clean structure
- Persistent storage (data saved even after closing the app)
- Simple CLI-based interaction

---

## Tech Stack

- Python 3
- JSON (for data storage)
- File Handling
- CLI (Command Line Interface)
- SQLite3

---

## Project Structure

```bash
expense-manager/
│
├── src/
│   ├── main.py
│   ├── database/
│   │   └── expense.db
│   └── models/
│       └── expense.py
│
├── README.md
└── requirements.txt
```

## How It Works

- User interacts through a CLI menu
- User can:
    - Add an expense
    - View all expenses
- Each expense includes:
    - Amount
    - Category
    - Description
    - Date
- Data is stored in an SQLite database (expense.db)
- The Expense model is used to:
    - Structure expense data
    - Convert objects into tuples for database insertion
    - Format output for display

## How to Run:

1. Clone the Repository:

```bash
git clone https://github.com/Saurav-T/Python-Mini-Projects
```

2. Navigate to Project Folder:

```bash
cd Python-Mini-Projects/beginner-projects/expense-tracker
```

3. Run the Program:

```bash
python src/main.py
```

## Screenshots

### Question

![Question](assets/screenshots/question.png)

### Leaderboard

![Leaderboard](assets/screenshots/leaderboard.png)

### Quiz App Flow

![Quiz App Flow](assets/gifs/input.gif)

## Future Improvements

- Cross-platform timer using threading
- GUI version (Tkinter / PyQt)
- Difficulty levels
- Database integration (SQLite)
- REST API version using Flask

## Learning Outcomes

- File handling in Python
- Working with JSON
- Functions and modular code
- CLI application design

### Author

- Saurav Tamrakar
- GitHub: [Saurav-T](https://github.com/Saurav-T)
