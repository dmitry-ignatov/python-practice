
files = []


while True:

    name = input("Введите имя файла: ")
    if name == "":
        print("Пустое имя файла нельзя добавить")
    elif name.lower() == "stop":
        break
    else:
        files.append(name)

    
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
    
        
    
img = []
aud = []
doc = []
arc = []
unk = []

print()

for file in files:

    category = get_category(file)
    print(f"{file} — {category}")

    if category == "image":           
        img.append(file)
        
    elif category == "audio":        
        aud.append(file)
        
    elif category == "document":        
        doc.append(file)      

    elif category == "archive":        
        arc.append(file)
        
    else:        
        unk.append(file)
        


print(f"\nImages: {img}")
print(f"Audio: {aud}")
print(f"Documents: {doc}")
print(f"Archives: {arc}")
print(f"Unknown: {unk}")