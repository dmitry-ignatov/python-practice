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
        

def read_file(path):
    try:
        with open(path, "r", encoding= "utf-8") as file:
            count = 0
            for line in file:
                count += 1
        return count
    except UnicodeDecodeError:
        print("Файл не удалось прочитать в нужной кодировке")
    except PermissionError:
        print("Нет доступа к файлу")
    except OSError:
        print("Не удалось прочитать файл")


def show_line_count(count):
    print(f"Количество прочитанных строк: {count}")


path = get_path()
count = read_file(path)
if count is not None:
    show_line_count(count)