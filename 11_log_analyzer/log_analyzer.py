from pathlib import Path
from datetime import datetime



def get_path():
    while True:
        input_path = input("Введите путь к файлу: ")
        input_path_normalize = input_path.strip()
        path = Path(input_path_normalize)

        if not input_path_normalize:
            print("Введите путь")
        elif not path.exists():
            print("Такого пути нет")
        elif not path.is_file():
            print("Введенный путь ведет к папке, а не файлу")
        elif path.suffix.lower() != ".log":
            print("Неверный формат файла")
        else:
            return path


def input_level():
    allowed_levels = ("ERROR", "WARNING", "INFO", "DEBUG")
    while True:
        level = input("Введите нужный уровень (0 - вернуться обратно): ")
        level_normalize = level.strip().upper()
        if not level_normalize:
            print("Введите уровень")
        elif level_normalize == "0":
            return None
        elif level_normalize not in allowed_levels:
            print("Такого уровня нет")
        else:
            return level_normalize


def input_message():
    while True:
        message = input("Введите текст сообщения для поиска (0 - вернуться обратно): ")
        message_normalize = message.strip().lower()
        if not message_normalize:
            print("Введите текст")
        elif message_normalize == "0":
            return None
        else:
            return message_normalize


def input_date():
    while True:
        try:
            date_text = input("Введите дату для поиска, формат ввода: ГГГГ-ММ-ДД (0 - вернуться обратно): ")
            date_text_normalize = date_text.strip()
            if not date_text_normalize:
                print("Введите дату")
            elif date_text_normalize == "0":
                return None
            else:
                search_date = datetime.strptime(
                    date_text_normalize,
                    "%Y-%m-%d"
                ).date()
                return search_date
        except ValueError:
            print("Введен неправильный формат или невозможная дата")


def parse_log_line(line):
    
    parts = line.strip().split(" | ", 2)
    if len(parts) < 3:
        return None
    try:
        parsed_datetime = datetime.strptime(
            parts[0],
            "%Y-%m-%d %H:%M:%S"
        )
    except ValueError:
        return None
    line_dict = {
        "datetime": parsed_datetime,
        "level": parts[1],
        "message": parts[2]
    }
    return line_dict


def show_search_results(log_list, prompt1, prompt2):
    if not log_list:
        print(prompt1)
    else:
        print(prompt2)
        for note in log_list:
            for key, value in note.items():
                print(f"{key}: {value}", end= " | ")
            print()


def search_by_level(log_entries, search_level):
    log_list = []
    for item in log_entries:
        if item["level"] == search_level:
            log_list.append(item)
    show_search_results(log_list, f"Записей по выбранному уровню '{search_level}' нет", 
                        f"Записи по выбранному уровню '{search_level}':")
    print()


def search_by_text(log_entries, search_text):
    log_list = []
    for item in log_entries:
        if search_text in item["message"].lower():
            log_list.append(item)
    show_search_results(log_list, f"Записей по введенному тексту '{search_text}' нет", 
                            "Записи найденные по введенному тексту: ")
    print()


def search_by_date(log_entries, search_date):
    log_list = []
    for item in log_entries:
        if search_date == item["datetime"].date():
            log_list.append(item)
    show_search_results(log_list, f"Записей по введенной дате '{search_date}' нет", 
                            "Записи найденные по введенной дате: ")
    print()


def count_levels(log_entries):
    result_dict = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
    }

    for item in log_entries:
        level = item["level"]
        if level in result_dict:
            result_dict[level] += 1
    return result_dict


def read_file(path):
    try:
        with open(path, "r", encoding= "utf-8") as file:
            log_entries = []
            corrupted_count = 0
            for line in file:
                line_dict = parse_log_line(line)
                if line_dict is None:
                    corrupted_count += 1
                else:
                    log_entries.append(line_dict)
        return log_entries, corrupted_count
    except UnicodeDecodeError:
        print("Файл не удалось прочитать в нужной кодировке")
    except PermissionError:
        print("Нет доступа к файлу")
    except OSError:
        print("Не удалось прочитать файл")


def show_statistics(log_entries, corrupted_count):

    count = count_levels(log_entries)
    for key, value in count.items():
        print(f"{key}: {value}")
    print(f"Количество корректных строк: {len(log_entries)}")
    print(f"Количество поврежденных строк: {corrupted_count}\n")


def show_menu():
    print(f"1. Поиск по уровню\n"
          f"2. Поиск по тексту\n" 
          f"3. Поиск по дате\n" 
          f"4. Показать статистику\n"
          f"0. Выход\n")


def executing_commands(log_entries, corrupted_count):
    while True:
        show_menu()
        command = input("Введите команду: ").strip()
        if not command:
            print(f"Введена пустая команда\n")

        elif command == "1":
            search_level = input_level()
            if search_level is not None:
                search_by_level(log_entries, search_level)

        elif command == "2":
            search_text = input_message()
            if search_text is not None:
                search_by_text(log_entries, search_text)

        elif command == "3":
            search_date = input_date()
            if search_date is not None:
                search_by_date(log_entries, search_date)

        elif command == "4":
            show_statistics(log_entries, corrupted_count)

        elif command == "0":
            break

        else:
            print(f"Введена неверная команда\n")



path = get_path()
result = read_file(path)
if result is not None:
    log_entries, corrupted_count = result
    executing_commands(log_entries, corrupted_count)
    