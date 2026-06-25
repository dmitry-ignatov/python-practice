from pathlib import Path

path = input("Введите путь к папке: ")
folder_path = Path(path)

if not folder_path.exists():
    print("Такого пути нет")
elif not folder_path.is_dir():
    print("Путь не является папкой")
else:
    files = {}
    
    for item in folder_path.iterdir():

        if item.is_file():
            file_size = item.stat().st_size

            if file_size not in files:
                files[file_size] = []
            files[file_size].append(item)

    duplicates_found = False
    for file_size, file_paths in files.items():
        if len(file_paths) >= 2:
            print(f"Размер файлов: {file_size} байт")
            print("Кандидаты на дубликаты:")
            for file_path in file_paths:
                print(file_path.name)
            duplicates_found = True
            print()
    if not duplicates_found:
        print("Файлы с одинаковым размером не найдены")

                    

