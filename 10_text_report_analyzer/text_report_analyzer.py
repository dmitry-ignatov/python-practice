from pathlib import Path
BASE_DIR = Path(__file__).parent
file_path = BASE_DIR / "input.txt"


def get_longest_smallest_word(words):
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    smallest_word = words[0]
    for word in words:
        if len(word) < len(smallest_word):
            smallest_word = word
    return longest_word, smallest_word

def line_count(file):
    count = 0
    for line in file:
        count += 1
    return count

try:
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
        file.seek(0)
        if not text:
            print("В файле нет текста")
        else:
            words = text.split()

            long_small_word = get_longest_smallest_word(words)
            count = line_count(file)
            

            print(f"Количество символов: {len(text)}")
            print(f"Количество слов: {len(words)}")
            print(f"Количество символов без пробелов: {len("".join(words))}")
            print(f"Самое длинное слово: {long_small_word[0]}")
            print(f"Самое короткое слово: {long_small_word[1]}")
            print(f"Количество строк: {count}")

except FileNotFoundError:
    print("Файл не найден")










    