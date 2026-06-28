from pathlib import Path
import hashlib


def get_path():

    path = input("Введите путь к папке: ")
    folder_path = Path(path)
    print()
    return folder_path


def get_hash(file_path):

    try:
        with file_path.open("rb") as file:        
            hash_object = hashlib.sha256()
            while True:
                file_data = file.read(65536)

                if not file_data:
                    break
                hash_object.update(file_data)

            result = hash_object.hexdigest()
            return result
    except OSError:
        print(f"Не удалось прочитать файл: {file_path.name}")
        return None


def get_files_by_size(folder_path):

    files_by_size = {}
    for file_path in folder_path.rglob("*"):

        if file_path.is_file():
            try:
                file_size = file_path.stat().st_size
            except OSError:
                print(f"Не удалось получить размер файла: {file_path.name}")
                continue

            if file_size not in files_by_size:
                files_by_size[file_size] = []
            files_by_size[file_size].append(file_path)
    return files_by_size


def get_files_by_hash(file_paths):
   
    files_by_hash = {}
    for file_path in file_paths:
        file_hash = get_hash(file_path)
        if file_hash is None:
            continue

        if file_hash not in files_by_hash:
            files_by_hash[file_hash] = []
        files_by_hash[file_hash].append(file_path)
    return files_by_hash
    

def get_duplicates(files_by_size, folder_path):

    duplicates_found = False
    count_of_groups = 0
    count_of_extra_copies = 0
    print(f"Проверяемая папка: {folder_path}\n")
    for file_paths in files_by_size.values():
        if len(file_paths) >= 2:
            
            files_by_hash = get_files_by_hash(file_paths)

            for duplicate_paths in files_by_hash.values():
                if len(duplicate_paths) >= 2:
                    count_of_groups += 1
                    duplicates_found = True
                    print(f"{count_of_groups}. Дубликаты:\n")
                    
                    for duplicate_path in duplicate_paths:
                        print(f"{duplicate_path.name} (путь - {duplicate_path.relative_to(folder_path)})")
                    count_of_extra_copies += len(duplicate_paths) - 1
                    print()

    if duplicates_found:
        print(f"Всего групп дубликатов: {count_of_groups}\nВсего лишних копий: {count_of_extra_copies}\n")

    else:
        print("Одинаковые файлы не найдены")


def main():

    folder_path = get_path()
    if not folder_path.exists():
        print("Такого пути нет")
    elif not folder_path.is_dir():
        print("Путь не является папкой")
    else:   
        files_by_size = get_files_by_size(folder_path)
        get_duplicates(files_by_size, folder_path)


if __name__ == "__main__":
    main()
                    

