
files = []


while True:

    name = input("Введите имя файла: ")
    if name == "":
        print("Пустое имя файла нельзя добавить")
    elif name == "stop":
        break
    else:
        files.append(name)

    

    
img = []
aud = []
doc = []
arc = []
unk = []

print()

for file in files:

    if file.endswith(".png") or file.endswith(".jpg"):
        print(f"{file} — image")
        img.append(file)
        
    elif file.endswith(".mp3") or file.endswith(".wav"):
        print(f"{file} — audio")
        aud.append(file)
        
    elif file.endswith(".pdf") or file.endswith(".txt"):
        print(f"{file} — document")
        doc.append(file)      

    elif file.endswith(".zip") or file.endswith(".rar"):
        print(f"{file} — archive")
        arc.append(file)
        
    else:
        print(f"{file} — unknown")
        unk.append(file)
        


print(f"\nImages: {img}")
print(f"Audio: {aud}")
print(f"Documents: {doc}")
print(f"Archives: {arc}")
print(f"Unknown: {unk}")