

texts = []

while True:

    text = input("Введите текст: ")
    clean_text = text.strip()

    if clean_text.lower() == "stop":
        break
    elif not clean_text:
        print("Нужно ввести текст")
    else:
        texts.append(clean_text)

if not texts:
    print("Строки не добавлены")
else:
    print(texts)