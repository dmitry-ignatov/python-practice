from pathlib import Path


def show_path_info(path, folder_path):
    print(f"\nВы выбрали путь: {path}")

    if not folder_path.exists():
        print("Такого пути нет")
    elif folder_path.is_file():
        print("Это файл, а не папка")
    elif folder_path.is_dir():
        print("Содержимое папки: ")
        for item in folder_path.iterdir():
            print(item)


path = input("Введите путь к папке: ")
folder_path = Path(path)

show_path_info(path, folder_path)

