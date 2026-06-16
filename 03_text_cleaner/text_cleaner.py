

def normalize_spaces(text):
    words = text.split()
    text_normalized = " ".join(words)
    return text_normalized


def get_texts():

    texts = []
    texts_lower = []

    while True:

        text = input("Введите текст: ")
        text_normalized = normalize_spaces(text)
        check_text = text_normalized.lower()
        
        if check_text == "stop":
            break
        elif not text_normalized:
            print("Нужно ввести текст")
        elif check_text in texts_lower:
            print("Такая строка уже есть")
        else:
            texts_lower.append(check_text)
            texts.append(text_normalized)
    return texts


def show_texts(texts):
    if not texts:
        print("Строки не добавлены")
    else:
        for index, text in enumerate(texts, start=1):
            print(f"{index}. {text}")
        print(f"\nКоличество строк: {len(texts)}")


def sort_texts(texts):
    texts.sort(key=str.lower)


texts = get_texts()
sort_texts(texts)
show_texts(texts)