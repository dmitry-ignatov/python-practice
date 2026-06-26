from pathlib import Path
import hashlib


def get_path():

    path = input("Введите путь к папке: ")
    folder_path = Path(path)
    print()
    return folder_path


def get_hash(file_path):

    with file_path.open("rb") as file:
        file_data = file.read()

    hash_object = hashlib.sha256()
    hash_object.update(file_data)
    result = hash_object.hexdigest()
    return result


def get_files_by_size(folder_path):

    files_by_size = {}
    for file_path in folder_path.iterdir():

        if file_path.is_file():
            file_size = file_path.stat().st_size

            if file_size not in files_by_size:
                files_by_size[file_size] = []
            files_by_size[file_size].append(file_path)
    return files_by_size


def get_files_by_hash(file_paths):
   
    files_by_hash = {}
    for file_path in file_paths:
        file_hash = get_hash(file_path)

        if file_hash not in files_by_hash:
            files_by_hash[file_hash] = []
        files_by_hash[file_hash].append(file_path.name)
    return files_by_hash
    

def get_duplicates(files_by_size):

    duplicates_found = False
    for file_paths in files_by_size.values():
        if len(file_paths) >= 2:
            files_by_hash = get_files_by_hash(file_paths)

            for file_names in files_by_hash.values():
                if len(file_names) >= 2:
                    duplicates_found = True
                    print(f"{', '.join(file_names)} - дубликаты")

    print()
    if not duplicates_found:
        print("Одинаковые файлы не найдены")

def main():

    folder_path = get_path()
    if not folder_path.exists():
        print("Такого пути нет")
    elif not folder_path.is_dir():
        print("Путь не является папкой")
    else:   
        files_by_size = get_files_by_size(folder_path)
        get_duplicates(files_by_size)


if __name__ == "__main__":
    main()
                    

