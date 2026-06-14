

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


files = []


while True:

    name = input("Введите имя файла: ")
    if name == "":
        print("Пустое имя файла нельзя добавить")
    elif name.lower() == "stop":
        break
    else:
        files.append(name)
    
categories = {    
    "image": [],
    "audio": [],
    "document": [],
    "archive": [],
    "unknown": []
}

print()

for file in files:

    category = get_category(file)
    print(f"{file} — {category}")

    categories[category].append(file)
        
   
        


print(f"\nImages: {categories['image']}")
print(f"Audio: {categories['audio']}")
print(f"Documents: {categories['document']}")
print(f"Archives: {categories['archive']}")
print(f"Unknown: {categories['unknown']}")