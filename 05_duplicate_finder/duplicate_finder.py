from pathlib import Path
import hashlib


def get_hash(file_path):
    with file_path.open("rb") as file:
        file_data = file.read()

    hash_object = hashlib.sha256()
    hash_object.update(file_data)
    result = hash_object.hexdigest()
    return result

path = input("Введите путь к папке: ")
folder_path = Path(path)

if not folder_path.exists():
    print("Такого пути нет")
elif not folder_path.is_dir():
    print("Путь не является папкой")
else:
    print()
    files_by_size = {}
    
    for file_path in folder_path.iterdir():

        if file_path.is_file():
            file_size = file_path.stat().st_size

            if file_size not in files_by_size:
                files_by_size[file_size] = []
            files_by_size[file_size].append(file_path)

    duplicates_found = False
    for file_size, file_paths in files_by_size.items():
        if len(file_paths) >= 2:

            files_by_hash = {}
            for file_path in file_paths:
                file_hash = get_hash(file_path)

                if file_hash not in files_by_hash:
                    files_by_hash[file_hash] = []
                files_by_hash[file_hash].append(file_path.name)

            for _, file_names in files_by_hash.items():
                if len(file_names) >= 2:
                    duplicates_found = True
                    print(f"{', '.join(file_names)} - дубликаты")
   
    print()
    if not duplicates_found:
        print("Одинаковые файлы не найдены")

                    

