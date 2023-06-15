import json
import pytest

from main import load_tasks, save_tasks, add_task, remove_task, list_tasks


@pytest.fixture
def todo_file(tmpdir):
    """Фикстура для создания временного файла todo.json."""
    todo_file = tmpdir.join("todo1.json")
    return str(todo_file)


def test_load_tasks(todo_file):
    """Тест для функции load_tasks()."""
    tasks = load_tasks(todo_file)
    assert tasks == []

    tasks_data = ["Task 1", "Task 2", "Task 3"]
    with open(todo_file, "w") as f:
        json.dump(tasks_data, f)

    tasks = load_tasks(todo_file)
    assert tasks == tasks_data


def test_save_tasks(todo_file):
    """Тест для функции save_tasks()."""
    tasks_data = ["Task 1", "Task 2", "Task 3"]

    save_tasks(tasks_data, todo_file,)

    with open(todo_file, "r") as f:
        saved_tasks = json.load(f)

    assert saved_tasks == tasks_data


def test_add_task(todo_file):
    """Тест для функции add_task()."""
    task = "New Task"

    add_task(task, todo_file)

    tasks = load_tasks(todo_file)
    assert task in tasks


def test_remove_task(todo_file):
    """Тест для функции remove_task()."""
    tasks_data = ["Task 1", "Task 2", "Task 3"]

    with open(todo_file, "w") as f:
        json.dump(tasks_data, f)

    task_to_remove = 2

    remove_task(task_to_remove, todo_file)

    tasks = load_tasks(todo_file)
    assert task_to_remove not in tasks


def test_list_tasks(todo_file, capsys):
    """Тест для функции list_tasks()."""
    tasks_data = ["Task 1", "Task 2", "Task 3"]

    with open(todo_file, "w") as f:
        json.dump(tasks_data, f)

    list_tasks(todo_file)

    captured = capsys.readouterr()
    assert captured.out == "1. Task 2\n2. Task 2\n3. Task 3\n"


def test_remove_task_raises_index_error(todo_file):
    """Test for the remove_task() function with IndexError."""
    tasks_data = ["Task 1", "Task 2", "Task 3"]

    with open(todo_file, "w") as f:
        json.dump(tasks_data, f)

    task_to_remove = 4
    assert remove_task(task_to_remove, todo_file) == "IndexError"


if __name__ == "__main__":
    pytest.main()
