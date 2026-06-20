from pathlib import Path


def show_path_info(path, folder_path):
    print(f"\nВы выбрали путь: {path}")

    if not folder_path.exists():
        print("Такого пути нет")
    elif folder_path.is_file():
        print("Это файл, а не папка")
    elif folder_path.is_dir():
        print("Содержимое папки: ")
        file_count = 0
        folder_count = 0
        for index, item in enumerate(folder_path.iterdir(), start=1):
            if item.is_file():
                file_count += 1
                print(f"{index}. {item.name} — файл")
            elif item.is_dir():
                folder_count += 1
                print(f"{index}. {item.name} — папка")
        print(f"\nФайлов: {file_count}\nПапок: {folder_count}")


path = input("Введите путь к папке: ")
folder_path = Path(path)

show_path_info(path, folder_path)

