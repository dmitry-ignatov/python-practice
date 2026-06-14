

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


def sort_files(data):

    
    categories = {    
        "image": [],
        "audio": [],
        "document": [],
        "archive": [],
        "unknown": []
    }

    print()

    for file in data:

        category = get_category(file)
        print(f"{file} — {category}")

        categories[category].append(file)
    return categories


files = get_files()

if not files:
    print("\nФайлы не добавлены\n")
    
else:
    categories = sort_files(files)

    print(f"\nImages: {categories['image']}")
    print(f"Audio: {categories['audio']}")
    print(f"Documents: {categories['document']}")
    print(f"Archives: {categories['archive']}")
    print(f"Unknown: {categories['unknown']}")

    print(f"\nTotal files: {len(files)}")
    print(f"Images count: {len(categories['image'])}")
    print(f"Audio count: {len(categories['audio'])}")
    print(f"Documents count: {len(categories['document'])}")
    print(f"Archives count: {len(categories['archive'])}")
    print(f"Unknown count: {len(categories['unknown'])}")
