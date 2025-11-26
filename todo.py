#!/usr/bin/env python3

"""
Simple Console-based To-Do List App
Internship Task 2 – To-Do List Application
"""

TASK_FILE = "tasks.txt"


def load_tasks():
    """Read tasks from file; return as list of strings."""
    tasks = []
    try:
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    tasks.append(line)
    except FileNotFoundError:
        # file nahi hai to empty list return kar do
        pass
    return tasks


def save_tasks(tasks):
    """Write all tasks back to file."""
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        for t in tasks:
            f.write(t + "\n")


def add_task():
    tasks = load_tasks()
    task = input("Enter new task: ").strip()
    if not task:
        print("Task cannot be empty!")
        return
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")


def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    print("\nYour Tasks:")
    print("-" * 30)
    for i, t in enumerate(tasks, start=1):
        print(f"{i}. {t}")
    print("-" * 30)


def remove_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to remove.")
        return

    view_tasks()
    try:
        index = int(input("Enter task number to remove: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Removed task: {removed}")
    else:
        print("Invalid task number.")


def clear_all_tasks():
    confirm = input("Are you sure you want to delete ALL tasks? (yes/no): ").lower()
    if confirm == "yes":
        save_tasks([])
        print("All tasks cleared.")
    else:
        print("Cancelled.")


def main():
    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Clear All Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            clear_all_tasks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
