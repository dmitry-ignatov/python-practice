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


inp_exp = [int(input("Введите расход 1: ")),
     int(input("Введите расход 2: ")),
     int(input("Введите расход 3: ")),
     int(input("Введите расход 4: ")),
     int(input("Введите расход 5: ")),]




print(f"Общая сумма: {calculate_total(inp_exp)}")
print(f"Средний расход: {calculate_average(inp_exp)}")
print(f"Самый большой расход: {find_biggest_expense(inp_exp)}")
print(f"Самый маленький расход: {find_smallest_expense(inp_exp)}")
print(f"Расходов выше среднего: {count_above_average(inp_exp)}")