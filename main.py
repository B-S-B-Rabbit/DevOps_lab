import json
import os


def load_tasks(todo_file):
    tasks = []
    if os.path.exists(todo_file):
        with open(todo_file, "r") as f:
            tasks = json.load(f)
    return tasks


def save_tasks(tasks, todo_file):
    with open(todo_file, "w") as f:
        json.dump(tasks, f)


def add_task(task, todo_file):
    tasks = load_tasks(todo_file)
    tasks.append(task)
    save_tasks(tasks, todo_file)


def remove_task(task, todo_file):
    tasks = load_tasks(todo_file)
    tasks.pop(int(task) - 1)
    save_tasks(tasks, todo_file)


def list_tasks(todo_file):
    tasks = load_tasks(todo_file)
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def main(todo_file):
    print("Todo List")
    print("1. Add task")
    print("2. Remove task")
    print("3. List tasks")
    print("4. Exit")

    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter task: ")
            add_task(task, todo_file)
            print("The task was successfully added")
        elif choice == "2":
            print("Here your list of tasks:")
            list_tasks(todo_file)
            task = input("Enter the number of task to remove from this list: ")
            remove_task(task,todo_file)
            print("The task was successfully removed")
        elif choice == "3":
            list_tasks(todo_file)
        elif choice == "4":
            print("Exit")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    td = "todo.json"
    main(td)
