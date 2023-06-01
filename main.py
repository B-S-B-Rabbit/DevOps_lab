import json
import os

TODO_FILE = "todo.json"


def load_tasks():
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            tasks = json.load(f)
    return tasks


def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f)


def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)


def remove_task(task):
    tasks = load_tasks()
    tasks.pop(int(task) - 1)
    save_tasks(tasks)


def list_tasks():
    tasks = load_tasks()
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def main():
    print("Todo List")
    print("1. Add task")
    print("2. Remove task")
    print("3. List tasks")
    print("4. Exit")

    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
            print("The task was successfully added")
        elif choice == "2":
            print("Here your list of tasks:")
            list_tasks()
            task = input("Enter the number of task to remove from this list: ")
            remove_task(task)
            print("The task was successfully removed")
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
