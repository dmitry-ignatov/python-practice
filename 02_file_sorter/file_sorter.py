

def get_category(data):

    data_lower = data.lower()
    
    if data_lower.endswith(".png") or data_lower.endswith(".jpg"):
        return "image"
        
    elif data_lower.endswith(".mp3") or data_lower.endswith(".wav"):
        return "audio"
        
    elif data_lower.endswith(".pdf") or data_lower.endswith(".txt"):
        return "document"      

    elif data_lower.endswith(".zip") or data_lower.endswith(".rar"):
        return "archive"
        
    else:
        return "unknown"


def get_files():

    files = []

    while True:

        name = input("Введите имя файла: ")
        if name == "":
            print("Пустое имя файла нельзя добавить")

        elif name.lower() == "stop":
            break

        else:
            files.append(name)

    return files


def sort_files(files):

    categories = {    
        "image": [],
        "audio": [],
        "document": [],
        "archive": [],
        "unknown": []
    }

    for file in files:

        category = get_category(file)
        categories[category].append(file)

    return categories


def show_results(files, categories):

    print()
    for category, file_list in categories.items():
        if not file_list:
            print(f"{category}: Файлов нет")
        else:
            print(f"{category}: {", ".join(file_list)}")         

    print(f"\nTotal files: {len(files)}")
    for category, file_list in categories.items():
        print(f"Count of {category}: {len(file_list)}")


files = get_files()

if not files:
    print("\nФайлы не добавлены\n")
    
else:
    categories = sort_files(files)
    show_results(files, categories)

    
