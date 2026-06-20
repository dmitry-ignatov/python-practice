from pathlib import Path


def get_category(extension):
    if extension == ".png" or extension == ".jpg":
        return "image"
    
    elif extension == ".mp3" or extension == ".wav":
        return "audio"
    
    elif extension == ".pdf" or extension == ".txt":
        return "document"

    elif extension == ".zip" or extension == ".rar":
        return "archive"
    
    else:
        return "unknown"
    

def show_path_info(path, folder_path):
    print(f"\nВы выбрали путь: {path}")

    if not folder_path.exists():
        print("Такого пути нет")
    elif folder_path.is_file():
        print("Это файл, а не папка")
    elif folder_path.is_dir():
        print("Содержимое папки: ")

        categories = {
            "image": [],
            "audio": [],
            "document": [],
            "archive": [],
            "unknown": []
        }
        file_count = 0
        folder_count = 0
        
        for index, item in enumerate(folder_path.iterdir(), start=1):
            if item.is_file():
                extension = item.suffix.lower()
                category = get_category(extension)
                categories[category].append(item.name)
                file_count += 1
                print(f"{index}. {item.name} — файл, расширение: {extension}, категория: {category}")
                
            elif item.is_dir():
                folder_count += 1
                print(f"{index}. {item.name} — папка")
        print(f"\nФайлов: {file_count}\nПапок: {folder_count}")
        print(f"\nКатегории файлов: ")
        for category_name, file_list in categories.items():
            print(f"{category_name}, количество: {len(file_list)}")
            for file_name in file_list:
                print(f"- {file_name}")
            print("")


path = input("Введите путь к папке: ")
folder_path = Path(path)

show_path_info(path, folder_path)

