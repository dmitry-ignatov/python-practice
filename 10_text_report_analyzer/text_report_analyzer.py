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


def get_top3_words(words):
    duplicate_words = {}
    for word in words:
        words_count = words.count(word)
        if words_count >= 2:
            duplicate_words[word] = words_count

    if duplicate_words:
        keys = list(duplicate_words.keys())
        values = list(duplicate_words.values())

        top1_word = keys[0]
        top1_word_count = values[0]
        top2_word = None
        top3_word = None
        for word, count in zip(keys, values):
            if count > top1_word_count:
                top1_word_count = count
                top1_word = word
        keys.remove(top1_word)
        values.remove(top1_word_count)

        if len(duplicate_words.keys()) >= 2:
            top2_word = keys[0]
            top2_word_count = values[0]
            for word, count in zip(keys, values):
                if count > top2_word_count:
                    top2_word_count = count
                    top2_word = word
            keys.remove(top2_word)
            values.remove(top2_word_count)

        if len(duplicate_words.keys()) >= 3:
            top3_word = keys[0]
            top3_word_count = values[0]
            for word, count in zip(keys, values):
                if count > top3_word_count:
                    top3_word_count = count
                    top3_word = word

        return top1_word, top2_word, top3_word, duplicate_words
    
def get_unique_words_count(words, result):
    duplicate_words = result[3]
    local_words = words.copy()
    for word in duplicate_words.keys():
        while word in local_words:
            local_words.remove(word)
    unique_words_count = len(local_words)
    return unique_words_count


def show_report(text, words, long_small_word, count, top, unique_words_count):
    print(f"Количество символов: {len(text)}")
    print(f"Количество слов: {len(words)}")
    print(f"Количество символов без пробелов: {len(''.join(words))}")
    print(f"Самое длинное слово: {long_small_word[0]}")
    print(f"Самое короткое слово: {long_small_word[1]}")
    print(f"Количество строк: {count}")
    if top:
        if top[1] is None:
            print(f"топ-1 самое частое слово: {top[0]}")
        elif top[2] is None:
            print(f"топ-2 самых частых слов: Топ 1: {top[0]}, Топ 2: {top[1]}")
        else:
            print(f"топ-3 самых частых слов: Топ 1: {top[0]}, Топ 2: {top[1]}, Топ 3: {top[2]}")
    print(f"Количество уникальных слов: {unique_words_count}")

try:
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
        file.seek(0)
        words = text.split()
        if not words:
            print("В файле нет текста")
        else:
            long_small_word = get_longest_smallest_word(words)
            count = line_count(file)
            top = get_top3_words(words)
            unique_words_count = get_unique_words_count(words, top)
            show_report(text, words, long_small_word, count, top, unique_words_count)

except FileNotFoundError:
    print("Файл не найден")
