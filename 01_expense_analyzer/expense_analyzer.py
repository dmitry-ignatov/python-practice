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

while True:
    print()
    print("1 — Добавить расход")
    print("2 — Показать статистику")
    print("3 — Показать все расходы")
    print("4 — Очистить все расходы")
    print("0 — Выйти")
    print()
    try:
        command = int(input("Введите команду: "))
    except:
        print()
        print("Неверное значение, введите число")
        continue
    if command == 1:
        print()
        try:
            expenses.append(int(input("Введите расход: ")))
        except:
            print()   
            print("Неверное значение, введите число") 
            continue
    elif command == 2 and expenses == []:
        print()
        print("Вы не ввели расход")
    elif command == 2:
        print()
        print(f"Общая сумма: {calculate_total(expenses)}")
        print(f"Средний расход: {calculate_average(expenses)}")
        print(f"Самый большой расход: {find_biggest_expense(expenses)}")
        print(f"Самый маленький расход: {find_smallest_expense(expenses)}")
        print(f"Расходов выше среднего: {count_above_average(expenses)}")
    elif command == 3 and expenses == []:
        print()
        print("Расходы не введены")
    elif command == 3:
        print("Все расходы:")
        schet = 0
        for exp in expenses:
            schet += 1
            print(f"Расход {schet}: {exp}")
    elif command == 4 and expenses == []:
        print()
        print("Расходы не введены")
    elif command == 4:
        expenses.clear()
        print()
        print("Все расходы очищены")
    
    elif command == 0:
        break
    else:
        print("Введена неверная команда")