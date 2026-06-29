
def normalize_spaces(text):
    words = text.split()
    text_normalized = " ".join(words)
    return text_normalized


def input_task(tasks):
    while True:
        task_name = input("Введите название задачи: ")
        if not task_name.strip():
            print("Введена пустая строка, введите название\n")
            continue
        else:
            task_info = {}
            task_info["title"] = normalize_spaces(task_name)
            task_info["done"] = False
            tasks.append(task_info)
            print()
            return


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

        
tasks = []

while True:

    print("1. Добавить задачу\n2. Показать задачи\n3. Отметить задачу выполненной\n4. Удалить задачу\n0. Выход\n")

    try:
        command = int(input("Выберите команду: "))
    except ValueError:
        print("Неверное значение введите число\n")
        continue

    if command > 4 or command < 0:
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

    elif command == 0:
        break