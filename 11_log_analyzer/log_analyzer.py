from pathlib import Path



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
        level = input("Введите нужный уровень (0 - пропуск): ")
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
        message = input("Введите текст сообщения для поиска (0 - пропуск): ")
        message_normalize = message.strip().lower()
        if not message_normalize:
            print("Введите текст")
        elif message_normalize == "0":
            return None
        else:
            return message_normalize


def parse_log_line(line):
    
    parts = line.strip().split(" | ", 2)
    if len(parts) < 3:
        return None
    line_dict = {
        "datetime": parts[0],
        "level": parts[1],
        "message": parts[2]
    }
    return line_dict


def filter_by_level(log_entries, level):
    log_list = []
    for item in log_entries:
        if item["level"] == level:
            log_list.append(item)
    return log_list


def search_by_text(log_entries, search_text):
    log_list = []
    for item in log_entries:
        if search_text in item["message"].lower():
            log_list.append(item)
    return log_list


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


def show_entries(log_entries, corrupted_count, level, search_text):

    count = count_levels(log_entries)
    for key, value in count.items():
        print(f"{key}: {value}")
    print(f"Количество корректных строк: {len(log_entries)}")
    print(f"Количество поврежденных строк: {corrupted_count}")

    if level is not None:
        filtered_level = filter_by_level(log_entries, level)
        if not filtered_level:
            print(f"Записей по выбранному уровню '{level}' нет")
        else:
            print(f"Записи по выбранному уровню '{level}':")
            for note in filtered_level:
                for key, value in note.items():
                    print(f"{key}: {value}", end= " | ")
                print()

    if search_text is not None:
        found_entries = search_by_text(log_entries, search_text)
        if not found_entries:
            print(f"Записей по введенному тексту для поиска '{search_text}' нет")
        else:
            print("Записи найденные по введенному тексту: ")
            for note in found_entries:
                for key, value in note.items():
                    print(f"{key}: {value}", end= " | ")
                print()



path = get_path()
result = read_file(path)
if result is not None:
    log_entries, corrupted_count = result
    level = input_level()
    search_text = input_message()
    show_entries(log_entries, corrupted_count, level, search_text)