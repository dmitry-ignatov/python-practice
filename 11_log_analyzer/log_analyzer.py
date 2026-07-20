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


def show_entries(log_entries, corrupted_count):
    for line in log_entries:
        print(line)
    print(f"Количество корректных строк: {len(log_entries)}")
    print(f"Количество поврежденных строк: {corrupted_count}")



path = get_path()
result = read_file(path)
if result is not None:
    log_entries, corrupted_count = result
    show_entries(log_entries, corrupted_count)