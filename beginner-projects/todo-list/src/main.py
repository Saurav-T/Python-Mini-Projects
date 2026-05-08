import json

FILE = "data/tasks.json"
def load_tasks():
    try:
        with open(FILE, 'r') as f:
            return json.load(f)
    except:
        return []
    
def save_tasks(tasks):
    with open(FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def view_tasks(tasks):
    if not tasks:
        print("No Tasks Found.")
        return
    else:
        print("Your Tasks")
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['title']} [{status}]")

def add_tasks(tasks):
    title = input("Enter a new task: ")
    tasks.append({
        "title": title,
        "done": False
    })
    print("Task Added")

def mark_done(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as DONE: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]['done'] = True
            print("Task marked as done.")
        else:
            print("Invalid index.")
    except:
        print("Enter a valid number.")

def mark_undone(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as NOT DONE: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]['done'] = False
            print("Task marked as undone.")
        else:
            print("Invalid index.")
    except:
        print("Enter a valid number.")

def delete_tasks(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the index of the task to be deleted: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"Task Removed: {removed['title']}")
        else:
            print("Invalid Index.")
    except:
        print("Enter a valid number.")

def menu():
    print("\n===== TO-DO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Mark Task Done")
    print("5. Mark Task Undone")
    print("6. Exit")

def main():
    tasks = load_tasks()

    while True:
        menu()
        choice = input("Enter a choice: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_tasks(tasks)
            save_tasks(tasks)
        elif choice == "3":
            delete_tasks(tasks)
            save_tasks(tasks)
        elif choice == "4":
            mark_done(tasks)
            save_tasks(tasks)
        elif choice == "5":
            mark_undone(tasks)
            save_tasks(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("Closing..")
            break
        else:
            print("Enter a valid choice")

main()


