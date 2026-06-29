
def normalize_spaces(text):
    words = text.split()
    text_normalized = " ".join(words)
    return text_normalized


def get_name(prompt):
    while True:
        task_name = input(prompt)
        if not task_name.strip():
            print("Введена пустая строка, введите название\n")
            continue
        return normalize_spaces(task_name)


def input_task(tasks):
    task_name = get_name("Введите название задачи: ")
    task_info = {}
    task_info["title"] = task_name
    task_info["done"] = False
    tasks.append(task_info)
    print()


def show_tasks(tasks):
    print("Текущие задачи:")
    for index, task in enumerate(tasks, start=1):
        if task["done"]:
            status = "[x]"
        else:
            status = "[ ]"
        print(f"{index}. {status} {task['title']} ")
    print()


def select_number(tasks):
    while True:
        try:
            task_number = int(input("Выберите номер задачи: "))
        except ValueError:
            print("Неверное значение введите число\n")
            continue

        if task_number > len(tasks) or task_number <= 0:
            print("Номера такой задачи нет")
        else:
            index = task_number - 1
            return index
    
    
def note_task(tasks):
    task_index = select_number(tasks)
    tasks[task_index]["done"] = True
    print("Выбранная задача отмечена\n")


def delete_task(tasks):
    task_index = select_number(tasks)
    tasks.pop(task_index)
    print("Выбранная задача удалена\n")


def edit_task(tasks):
    task_index = select_number(tasks)
    new_name = get_name("Введите новое название задачи: ")
    tasks[task_index]["title"] = new_name
    print("Название задачи изменено\n")


def count_tasks(tasks):
    done_count = 0
    not_done_count = 0 
    for task in tasks:
        if task["done"]:
            done_count += 1
        else:
            not_done_count += 1
    task_counts = [done_count, not_done_count]
    return task_counts


def show_statistics(tasks):
    task_counts = count_tasks(tasks)
    print(f"Всего задач: {len(tasks)}")
    print(f"Выполнено: {task_counts[0]}")
    print(f"Не выполнено: {task_counts[1]}\n")



tasks = []

while True:

    print("1. Добавить задачу\n2. Показать задачи\n3. Отметить задачу выполненной")
    print("4. Удалить задачу\n5. Изменить название задачи\n6. Показать статистику задач\n0. Выход\n")
    try:
        command = int(input("Выберите команду: "))
    except ValueError:
        print("Неверное значение введите число\n")
        continue

    if command > 6 or command < 0:
        print("Такой команды нет\n")
        continue


    elif command == 1:
        input_task(tasks)


    elif command == 2 and not tasks:
        print("Задачи не введены\n")
    elif command == 2:
        show_tasks(tasks)
        

    elif command == 3 and not tasks:
        print("Задачи не введены\n")
    elif command == 3:
        show_tasks(tasks)
        note_task(tasks)


    elif command == 4 and not tasks:
        print("Задачи не введены\n")
    elif command == 4:
        show_tasks(tasks)
        delete_task(tasks)


    elif command == 5 and not tasks:
        print("Задачи не введены\n")
    elif command == 5:
        show_tasks(tasks)
        edit_task(tasks)


    elif command == 6 and not tasks:
        print("Задачи не введены\n")
    elif command == 6:
        show_statistics(tasks)


    elif command == 0:
        break