


def password_len(password):
    if len(password) < 8:
        len_password = "короткий"
        score = 0
        return [len_password, score]
    elif len(password) >= 8 and len(password) < 12:
        len_password = "нормальный"
        score = 2
        return [len_password, score]
    else:
        len_password = "длинный"
        score = 3
        return [len_password, score]


def small_or_big_letter(password):
    big_letter = "нет"
    small_letter = "нет"
    score = 0
    if any(char.isupper() for char in password):
        big_letter = "есть"
        score += 1
    if any(char.islower() for char in password):    
        small_letter = "есть"
        score += 1
    return [big_letter, small_letter, score]


def is_there_digit(password):
    if any(char.isdigit() for char in password):
        score = 1
        return ["есть", score]
    else:
        score = 0
        return ["нет", score]
    

def is_spec_letter(password):
    if any(not char.isalnum() and not char.isspace() for char in password):
        score = 2
        return ["есть", score]
    else:
        score = 0
        return ["нет", score]
    

def is_there_spaces(password):
    if any(char.isspace() for char in password):
        score = 0
        return ["есть", score]
    else:
        score = 1
        return ["нет", score]


password = input("Введите пароль: ")
letters_len = password_len(password)
letters_size = small_or_big_letter(password)  
letters_digit = is_there_digit(password)
letters_spec = is_spec_letter(password)
letters_space =is_there_spaces()

score_sum = int(letters_len[1] + letters_size[2] + letters_digit[1] + letters_spec[1] + letters_space[1])
if score_sum <= 3:
    assess = "слабый пароль"
elif score_sum >= 4 and score_sum <= 6:
    assess = "средний пароль"
elif score_sum >= 7 and score_sum <= 10:
    assess = "сильный пароль"

print(f"""Результат проверки:
Длина: {letters_len[0]}
Большие буквы: {letters_size[0]}
Маленькие буквы: {letters_size[1]}
Цифры: {letters_digit[0]}
Спецсимволы: {letters_spec[0]}
Пробелы: {letters_space[0]}""")
print(f"\nОценка: {assess}\n")