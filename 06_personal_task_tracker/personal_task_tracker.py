
def normalize_spaces(text):
    words = text.split()
    text_normalized = " ".join(words)
    return text_normalized

tasks = []


while True:

    print("1. Добавить задачу\n2. Показать задачи\n3. Отметить задачу выполненной\n0. Выход\n")

    try:
        command = int(input("Выберите команду: "))
    except ValueError:
        print("Неверное значение введите число\n")
        continue

    if command > 3 or command < 0:
        print("Такой команды нет\n")
        continue


    elif command == 1:
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
                break


    elif command == 2 and not tasks:
        print("Задачи не введены")
    elif command == 2:
        
        for index, task in enumerate(tasks, start=1):
            if task["done"]:
                status = "[x]"
            else:
                status = "[ ]"
            print(f"{index}. {status} {task['title']} ")
        print()


    elif command == 3 and not tasks:
        print("Задачи не введены")
    elif command == 3:

        for index, task in enumerate(tasks, start=1):
            if task["done"]:
                status = "[x]"
            else:
                status = "[ ]"
            print(f"{index}. {status} {task['title']} ")
        while True:
            try:
                task_number = int(input("Выберите номер задачи: "))
            except ValueError:
                print("Неверное значение введите число\n")
                continue

            if task_number > len(tasks) or task_number <= 0:
                print("Номера такой задачи нет")
            else:
                tasks[task_number - 1]["done"] = True
                print("Выбранная задача отмечена\n")
                break

    elif command == 0:
        break