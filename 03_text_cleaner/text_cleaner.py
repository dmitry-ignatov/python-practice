

def get_texts():

    texts = []
    texts_low = []

    while True:

        text = input("Введите текст: ")
        
        clean_text = text.strip()
        check_text = clean_text.lower()
        
        if check_text == "stop":
            break
        elif not clean_text:
            print("Нужно ввести текст")
        elif check_text in texts_low:
            print("Такая строка уже есть")
        else:
            texts_low.append(check_text)
            texts.append(clean_text)
    return texts


def show_texts(texts):
    if not texts:
        print("Строки не добавлены")
    else:
        print(", ".join(texts))
        print(f"\nКоличество строк: {len(texts)}")

texts = get_texts()
show_texts(texts)