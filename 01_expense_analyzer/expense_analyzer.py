def calculate_total(data):
    total_exp = 0
    for exp in data:
        total_exp += exp
    return total_exp

def calculate_average(data):
    av_exp = calculate_total(data)/len(data)
    return av_exp


def find_biggest_expense(data):
    big_exp = data[0]
    for exp in data:
        if exp > big_exp:
            big_exp = exp
    return big_exp

def find_smallest_expense(data):
    small_exp = data[0]
    for exp in data:
        if exp < small_exp:
            small_exp = exp
    return small_exp

def count_above_average(data):
    exp_count = 0
    av = calculate_average(data)
    for exp in data:
        if exp > av:
            exp_count += 1
    return exp_count



expenses = []

def show_expenses(data):
    print("\nВсе расходы:\n")
    for index, exp in enumerate(data, start=1):
        print(f"Расход {index}: {exp}")

def is_index_not_valid(index, data):
    return index >= len(data) or index < 0

def show_menu():
    print("\n1 — Добавить расход")
    print("2 — Показать статистику")
    print("3 — Показать все расходы")
    print("4 — Очистить все расходы")
    print("5 — Удалить расход")
    print("6 — Изменить расход")
    print("7 — Сохранить расходы в файл")
    print("8 — Загрузить расходы из файла")
    print("0 — Выйти\n")

def get_statistics_text(data):
    text = ""
    text +=f"\nОбщая сумма: {calculate_total(data)}"
    text +=f"\nСредний расход: {calculate_average(data)}"
    text +=f"\nСамый большой расход: {find_biggest_expense(data)}"
    text +=f"\nСамый маленький расход: {find_smallest_expense(data)}"
    text +=f"\nРасходов выше среднего: {count_above_average(data)}"
    return text

def save_expenses(data):
    with open("expenses.txt", "w") as file:
        for exp in data:
            file.write(f"{exp}\n")
    with open("expenses_report.txt", "w") as file:
        file.write("Отчёт по расходам\n\n")
        for index, exp in enumerate(data, start=1):
            file.write(f"Расход {index}: {exp}\n")
        file.write(get_statistics_text(data))
    print("\nРасходы сохранены в expenses.txt и expenses_report.txt")

def load_expenses(data):
    temp_expenses = []
    try:
        with open("expenses.txt", "r") as file:                         
            for line in file:
                exp = int(line.strip())
                if exp <= 0:
                    raise ValueError
                else:
                    temp_expenses.append(exp)
            if not temp_expenses:
                print("\nФайл expenses.txt пустой")
            else:    
                data.clear()
                data.extend(temp_expenses)
                print("\nРасходы загружены из expenses.txt")
    except FileNotFoundError:
        print("\nФайл expenses.txt не найден")
    except ValueError:
        print("\nФайл expenses.txt содержит некорректные данные")


while True:
    show_menu()

    try:
        command = int(input("Введите команду: "))
    except ValueError:
        print("\nНеверное значение, введите число\n")
        continue

    if command == 1:
        try:
           new_exp = int(input("\nВведите расход: "))
           if new_exp <= 0:
                print("\nРасход должен быть больше нуля")
           else:
               expenses.append(new_exp)
        except ValueError:   
            print("\nНеверное значение, введите число") 
            continue

    elif command == 2 and expenses == []:
        print("\nВы не ввели расход")
    elif command == 2:
        print(get_statistics_text(expenses))

    elif command == 3 and expenses == []:
        print("\nРасходы не введены")
    elif command == 3:
        show_expenses(expenses)

    elif command == 4 and expenses == []:
        print("\nРасходы не введены")
    elif command == 4:
        expenses.clear()
        print("\nВсе расходы очищены")

    elif command == 5 and expenses == []:
        print("\nРасходы не введены")
    elif command == 5:
        show_expenses(expenses)
        try:
            del_exp = int(input("\nВведите номер расхода для удаления: ")) - 1         
        except ValueError:  
            print("\nНеверное значение, введите число")
            continue
        if is_index_not_valid(del_exp, expenses):
            print("\nНеверный номер расхода")
        else:
            expenses.pop(del_exp)
            print("\nРасход удален")

    elif command == 6 and expenses == []:
        print("\nРасходы не введены")
    elif command == 6:
        show_expenses(expenses)
        try:
            change_exp = int(input("\nВведите номер расхода для изменения: ")) - 1 
        except ValueError:
            print("\nНеверное значение, введите число")
            continue
        if is_index_not_valid(change_exp, expenses):
            print("\nНеверный номер расхода")
        else:
            try:
                new_exp = int(input("\nВведите новый расход: "))
                if new_exp <= 0:
                     print("\nРасход должен быть больше нуля")
                else:
                    expenses[change_exp] = new_exp
                    print("Расход изменен")
            except ValueError:
                print("\nНеверное значение, введите число")
                continue
             

    elif command == 7 and expenses == []:    
        print("\nРасходы не введены")
    elif command == 7:
        save_expenses(expenses)
    
    elif command == 8:
        load_expenses(expenses)       

    elif command == 0:
        break
    
    else:
        print("\nВведена неверная команда")