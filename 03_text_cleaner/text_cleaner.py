

def get_texts():

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
    return texts


def show_texts(texts):
    if not texts:
        print("Строки не добавлены")
    else:
        print(", ".join(texts))
        print(f"Количество строк: {len(texts)}")

texts = get_texts()

show_texts(texts)