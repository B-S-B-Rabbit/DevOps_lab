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
    try:
        tasks.pop(int(task) - 1)
    except IndexError:
        return "IndexError"
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
    psevdo_choice = ["1", "Hello, world", "3", "2", "1", "4"]
    count = 0
    while True:
        print("Enter your choice: %s" % psevdo_choice[count])
        choice = psevdo_choice[count]
        count += 1
        if choice == "1":
            print("Enter task: %s" % psevdo_choice[count])
            task = psevdo_choice[count]
            count += 1
            add_task(task, todo_file)
            print("The task was successfully added")
        elif choice == "2":
            print("Here your list of tasks:")
            list_tasks(todo_file)
            print("Enter the number of task to remove from this list: %s" % psevdo_choice[count])
            task = psevdo_choice[count]
            count += 1
            remove_task(task, todo_file)
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
