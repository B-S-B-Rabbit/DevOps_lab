import json
import os
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

    # Создаем временный файл с задачами
    tasks_data = ["Task 1", "Task 2", "Task 3"]
    with open(todo_file, "w") as f:
        json.dump(tasks_data, f)

    # Загружаем задачи из временного файла
    tasks = load_tasks(todo_file)
    assert tasks == tasks_data


def test_save_tasks(todo_file):
    """Тест для функции save_tasks()."""
    tasks_data = ["Task 1", "Task 2", "Task 3"]

    # Сохраняем задачи во временный файл
    save_tasks(tasks_data, todo_file,)

    # Проверяем, что данные сохранены корректно
    with open(todo_file, "r") as f:
        saved_tasks = json.load(f)

    assert saved_tasks == tasks_data


def test_add_task(todo_file):
    """Тест для функции add_task()."""
    task = "New Task"

    # Добавляем задачу
    add_task(task, todo_file)

    # Проверяем, что задача добавлена
    tasks = load_tasks(todo_file)
    assert task in tasks


def test_remove_task(todo_file):
    """Тест для функции remove_task()."""
    tasks_data = ["Task 1", "Task 2", "Task 3"]

    # Создаем временный файл с задачами
    with open(todo_file, "w") as f:
        json.dump(tasks_data, f)

    task_to_remove = 2

    # Удаляем задачу
    remove_task(task_to_remove, todo_file)

    # Проверяем, что задача удалена
    tasks = load_tasks(todo_file)
    assert task_to_remove not in tasks


def test_list_tasks(todo_file, capsys):
    """Тест для функции list_tasks()."""
    tasks_data = ["Task 1", "Task 2", "Task 3"]

    # Создаем временный файл с задачами
    with open(todo_file, "w") as f:
        json.dump(tasks_data, f)

    # Выводим список задач
    list_tasks(todo_file)

    # Проверяем вывод
    captured = capsys.readouterr()
    assert captured.out == "1. Task 1\n2. Task 2\n3. Task 3\n"


def test_remove_task_raises_index_error(todo_file):
    """Test for the remove_task() function with IndexError."""
    tasks_data = ["Task 1", "Task 2", "Task 3"]

    with open(todo_file, "w") as f:
        json.dump(tasks_data, f)

    task_to_remove = 4
    assert remove_task(task_to_remove, todo_file) == "IndexError"


if __name__ == "__main__":
    pytest.main()
