files = [
    "photo.jpg",
    "song.mp3",
    "document.pdf",
    "archive.zip",
    "unknown.xyz",
    "song2.wav"
]

img = []
aud = []
doc = []
arc = []
unk = []

for file in files:
   
    if file.endswith(".png") or file.endswith(".jpg"):
        print(f"{file} — image\n")
        img.append(file)
        
    elif file.endswith(".mp3") or file.endswith(".wav"):
        print(f"{file} — audio\n")
        aud.append(file)
        
    elif file.endswith(".pdf") or file.endswith(".txt"):
        print(f"{file} — document\n")
        doc.append(file)      

    elif file.endswith(".zip") or file.endswith(".rar"):
        print(f"{file} — archive\n")
        arc.append(file)
        
    else:
        print(f"{file} — unknown\n")
        unk.append(file)
        


print(f"Images: {img}")
print(f"Audio: {aud}")
print(f"Documents: {doc}")
print(f"Archives: {arc}")
print(f"Unknown: {unk}")