


def get_password_len(password):
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


def check_letters_size(password):
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


def is_simple_password(password):
    score = 1
    simple_passwords = ["password", "qwerty", "qwerty123", "123456", "12345678", "111111", "admin", "admin123", "пароль", "йцукен"]
    for simple_password in simple_passwords:
        if simple_password == password.lower():
            score = 0
            return ["да", score]
    return ["нет", score]


def get_score_sum(letters_len, letters_size, letters_digit, letters_spec, letters_space, simple_password):
    
    score_sum = letters_len[1] + letters_size[2] + letters_digit[1] + letters_spec[1] + letters_space[1] + simple_password[1]
    if score_sum <= 3:
        assess = "слабый пароль"
    elif score_sum >= 4 and score_sum <= 6:
        assess = "средний пароль"
    elif score_sum >= 7 and score_sum <= 10:
        assess = "сильный пароль"
    return [assess, score_sum]


def recommendations(letters_len, letters_size, letters_digit, letters_spec, letters_space, simple_password):

    if letters_len[0] == "короткий":
        print("- Увеличьте длину пароля")
    elif letters_len[0] == "нормальный":
        print("- Немного увеличьте длину пароля")
    
    if letters_size[0] == "нет":
        print("- Добавьте хотя бы одну большую букву")
    if letters_size[1] == "нет":
        print("- Добавьте хотя бы одну маленькую букву")

    if letters_digit[0] == "нет":
        print("- Добавьте хотя бы одну цифру")
    
    if letters_spec[0] == "нет":
        print("- Добавьте хотя бы один спецсимвол")

    if letters_space[0] == "есть":
        print("- Уберите пробел")
    
    if simple_password[0] == "да":
        print("- Избегайте простых паролей")


def get_results(letters_len, letters_size, letters_digit, letters_spec, letters_space, simple_password, assess):
    print(f"""Результат проверки:
Длина: {letters_len[0]}
Большие буквы: {letters_size[0]}
Маленькие буквы: {letters_size[1]}
Цифры: {letters_digit[0]}
Спецсимволы: {letters_spec[0]}
Пробелы: {letters_space[0]}
Простой пароль: {simple_password[0]}""")

    print(f"\nОценка: {assess[0]}\n")

    if assess[1] != 10:
        print("Рекомендации:")
        recommendations(letters_len, letters_size, letters_digit, letters_spec, letters_space, simple_password)


def main():

    password = input("Введите пароль: ")
    letters_len = get_password_len(password)
    letters_size = check_letters_size(password)  
    letters_digit = is_there_digit(password)
    letters_spec = is_spec_letter(password)
    letters_space = is_there_spaces(password)
    simple_password = is_simple_password(password)
    assess = get_score_sum(letters_len, letters_size, letters_digit, letters_spec, letters_space, simple_password)
    get_results(letters_len, letters_size, letters_digit, letters_spec, letters_space, simple_password, assess)


if __name__ == "__main__":
    main()
