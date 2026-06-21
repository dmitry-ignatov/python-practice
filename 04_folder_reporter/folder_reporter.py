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


def normalize_spaces(text):
    words = text.split()
    text_normalized = " ".join(words)
    return text_normalized


def get_filename():
    filename = input("Введите имя файла для сохранения: ")
    filename_normalized = normalize_spaces(filename)
    if not filename_normalized:
        filename = "report.txt"
        return filename
    elif not filename_normalized.lower().endswith(".txt"):
        filename_normalized = filename_normalized + ".txt"
        return filename_normalized
    return filename_normalized


def save_file(texts, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for text in texts:
            file.write(f"{text}\n")
    print(f"\nТекст сохранен в {filename}")


def get_lower_name(item):
    return item.name.lower()


def get_report(path, folder_path):
    report_lines = []
    report_lines.append(f"Выбранный путь: {path}")
    report_lines.append("")
    report_lines.append("Содержимое папки:")

    categories = {
        "image": [],
        "audio": [],
        "document": [],
        "archive": [],
        "unknown": []
    }

    file_count = 0
    folder_count = 0
    try:       
        for index, item in enumerate(sorted(folder_path.iterdir(), key=get_lower_name), start=1):
            if item.is_file():
                extension = item.suffix.lower()
                category = get_category(extension)
                categories[category].append(item.name)
                file_count += 1
                report_lines.append(f"{index}. {item.name} — файл, расширение: {extension}, категория: {category}")
                
            elif item.is_dir():
                folder_count += 1
                report_lines.append(f"{index}. {item.name} — папка")
        
        report_lines.append("")
        report_lines.append(f"Файлов: {file_count}")
        report_lines.append(f"Папок: {folder_count}")
        report_lines.append("")
        report_lines.append("Категории файлов:")
        for category_name, file_list in categories.items():
            report_lines.append(f"{category_name}, количество: {len(file_list)}")
            for file_name in file_list:
                report_lines.append(f"- {file_name}")
            report_lines.append("")
        print("\n".join(report_lines))
        return report_lines
    except PermissionError:
        print("Нет доступа к содержимому папки")


def show_path_info(path, folder_path):
    if not folder_path.exists():
        print("Такого пути нет")
    elif folder_path.is_file():
        print("Это файл, а не папка")
    elif folder_path.is_dir():
        texts = get_report(path, folder_path)
        return texts


def main():
    path = input("Введите путь к папке: ")
    folder_path = Path(path)

    texts = show_path_info(path, folder_path)
    if texts:
        filename = get_filename()
        save_file(texts, filename)


if __name__ == "__main__":
    main()

