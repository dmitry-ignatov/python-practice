def calculate_total(expenses):
    total_exp = 0
    for exp in expenses:
        total_exp += exp
    return total_exp

def calculate_average(expenses):
    av_exp = calculate_total(expenses)/len(expenses)
    return av_exp


def find_biggest_expense(expenses):
    big_exp = expenses[0]
    for exp in expenses:
        if exp > big_exp:
            big_exp = exp
    return big_exp

def find_smallest_expense(expenses):
    small_exp = expenses[0]
    for exp in expenses:
        if exp < small_exp:
            small_exp = exp
    return small_exp

def count_above_average(expenses):
    exp_count = 0
    av = calculate_average(expenses)
    for exp in expenses:
        if exp > av:
            exp_count += 1
    return exp_count




expenses = []

def show_expenses(expenses):
    print("\nВсе расходы:")
    schet = 0
    for exp in expenses:
        schet += 1
        print(f"Расход {schet}: {exp}")

while True:
    print("\n1 — Добавить расход")
    print("2 — Показать статистику")
    print("3 — Показать все расходы")
    print("4 — Очистить все расходы")
    print("5 — Удалить расход")
    print("6 — Изменить расход")
    print("0 — Выйти\n")

    try:
        command = int(input("Введите команду: "))
    except ValueError:
        print("\nНеверное значение, введите число\n")
        continue

    if command == 1:
        try:
            expenses.append(int(input("\nВведите расход: ")))
        except ValueError:   
            print("\nНеверное значение, введите число") 
            continue

    elif command == 2 and expenses == []:
        print("\nВы не ввели расход")
    elif command == 2:
        print(f"\nОбщая сумма: {calculate_total(expenses)}")
        print(f"Средний расход: {calculate_average(expenses)}")
        print(f"Самый большой расход: {find_biggest_expense(expenses)}")
        print(f"Самый маленький расход: {find_smallest_expense(expenses)}")
        print(f"Расходов выше среднего: {count_above_average(expenses)}")

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
        if del_exp >= len(expenses) or del_exp < 0:
            print("\nНеверный номер расхода")
        else:
            expenses.pop(del_exp)
            print("Расход удален")

    elif command == 6 and expenses == []:
        print("\nРасходы не введены")
    elif command == 6:
        show_expenses(expenses)
        try:
            change_exp = int(input("\nВведите номер расхода для изменения: ")) - 1 
        except ValueError:
            print("\nНеверное значение, введите число")
            continue
        if change_exp >= len(expenses) or change_exp < 0:
            print("\nНеверный номер расхода")
        else:
            try:
                new_exp = int(input("\nВведите новый расход: ")) 
            except ValueError:
                print("\nНеверное значение, введите число")
                continue
            expenses[change_exp] = new_exp
            print("Расход изменен")     

    elif command == 0:
        break
    else:
        print("\nВведена неверная команда")