password = input("Введите пароль: ")


def password_len(password):
    if len(password) < 7:
        len_password = "короткий"
        return len_password
    elif len(password) > 7 and len(password) < 15:
        len_password = "нормальный"
        return len_password
    else:
        len_password = "длинный"
        return len_password


def small_or_big_letter(password):
    small_letter = False
    big_letter = False
    if any(char.isupper() for char in password):
        big_letter = True
    elif any(char.islower() for char in password):    
        small_letter = True
    return small_letter, big_letter


def is_there_digit(password):
    if any(char.isdigit for char in password):
        return "есть"
    else:
        return "нет"