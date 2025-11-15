import json
import os
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

TASK_FILE = "tasks.json"


def load_tasks():
    """Load tasks from JSON file. Create file if not exist."""
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, "w") as f:
            json.dump([], f)

    with open(TASK_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    """Save updated tasks to file."""
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task():
    tasks = load_tasks()
    title = input(Fore.CYAN + "Enter task description: ").strip()

    if not title:
        print(Fore.RED + "Task cannot be empty!")
        return

    task = {
        "id": len(tasks) + 1,
        "task": title,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    tasks.append(task)
    save_tasks(tasks)
    print(Fore.GREEN + "Task added successfully!")


def view_tasks():
    tasks = load_tasks()

    if not tasks:
        print(Fore.YELLOW + "No tasks found!")
        return

    print(Fore.MAGENTA + "\nYour Tasks:")
    print("-" * 40)

    for t in tasks:
        print(
            Fore.CYAN
            + f"ID: {t['id']} | {t['task']} (Added on {t['created_at']})"
        )

    print("-" * 40)


def remove_task():
    tasks = load_tasks()
    view_tasks()

    if not tasks:
        return

    try:
        task_id = int(input(Fore.CYAN + "Enter task ID to remove: "))
    except ValueError:
        print(Fore.RED + "Invalid input! Enter a number.")
        return

    updated_tasks = [t for t in tasks if t["id"] != task_id]

    if len(updated_tasks) == len(tasks):
        print(Fore.YELLOW + "Task ID not found!")
        return

    # Reassign IDs
    for i, task in enumerate(updated_tasks, 1):
        task["id"] = i

    save_tasks(updated_tasks)
    print(Fore.GREEN + "Task removed successfully!")


def clear_all_tasks():
    confirm = input(Fore.RED + "Are you sure? (yes/no): ").lower()

    if confirm == "yes":
        save_tasks([])
        print(Fore.GREEN + "All tasks cleared!")
    else:
        print(Fore.YELLOW + "Cancelled.")


def menu():
    while True:
        print(Fore.BLUE + "\n====== TO-DO LIST MENU ======")
        print(Fore.WHITE + """
1. Add Task  
2. View Tasks  
3. Remove Task  
4. Clear All Tasks  
5. Exit  
""")

        choice = input(Fore.GREEN + "Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            clear_all_tasks()
        elif choice == "5":
            print(Fore.YELLOW + "Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice! Try again.")


if __name__ == "__main__":
    menu()
