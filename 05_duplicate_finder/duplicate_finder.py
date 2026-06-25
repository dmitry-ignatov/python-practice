from pathlib import Path

path = input("Введите путь к папке: ")
folder_path = Path(path)

if not folder_path.exists():
    print("Такого пути нет")
elif not folder_path.is_dir():
    for item in folder_path.iterdir():
        if item.is_file():
            print(f"{item.name}, {item.stat().st_size}")