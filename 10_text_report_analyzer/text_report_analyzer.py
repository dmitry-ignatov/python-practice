from pathlib import Path
BASE_DIR = Path(__file__).parent
file_path = BASE_DIR / "input.txt"
report_path = BASE_DIR / "report.txt"


def get_normalized_words(words):
    normalized_words = []
    for word in words:
        normalized_word = word.lower().strip(".,!?;:()[]\"«»")
        if not normalized_word:
            continue
        normalized_words.append(normalized_word)
    return normalized_words


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
    word_counts = {}
    top_words = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
        
    for word in word_counts:
        if word_counts[word] >= 2:
            duplicate_words[word] = word_counts[word]

    if duplicate_words:
        keys = list(duplicate_words.keys())
        values = list(duplicate_words.values())

        top1_word = keys[0]
        top1_word_count = values[0]
        for word, count in zip(keys, values):
            if count > top1_word_count:
                top1_word_count = count
                top1_word = word
        keys.remove(top1_word)
        values.remove(top1_word_count)
        top_words[top1_word] = top1_word_count

        if len(duplicate_words) >= 2:
            top2_word = keys[0]
            top2_word_count = values[0]
            for word, count in zip(keys, values):
                if count > top2_word_count:
                    top2_word_count = count
                    top2_word = word
            keys.remove(top2_word)
            values.remove(top2_word_count)
            top_words[top2_word] = top2_word_count

        if len(duplicate_words) >= 3:
            top3_word = keys[0]
            top3_word_count = values[0]
            for word, count in zip(keys, values):
                if count > top3_word_count:
                    top3_word_count = count
                    top3_word = word
            top_words[top3_word] = top3_word_count

        return top_words, word_counts
    return None, word_counts
    
    
def get_unique_words_count(result):
    unique_words_count = len(result[1])
    return unique_words_count


def get_report(text, normalized_words, long_small_word, count, top, unique_words_count):
    report = [f"Количество символов: {len(text)}",
    f"Количество слов: {len(normalized_words)}",
    f"Количество символов без пробелов: {len(''.join(text.split()))}",
    f"Самое длинное слово: {long_small_word[0]}",
    f"Самое короткое слово: {long_small_word[1]}",
    f"Количество строк: {count}"]
    if top[0] is not None:
        top_items = list(top[0].items())
        if len(top_items) == 1:
            report.append(f"топ-1 самое частое слово: {top_items[0][0]}, количество слов: {top_items[0][1]}")
        elif len(top_items) == 2:
            report.append(f"топ-2 самых частых слов: Топ 1: {top_items[0][0]}, количество слов: {top_items[0][1]}, "
                                                   f"Топ 2: {top_items[1][0]}, количество слов: {top_items[1][1]}")
        else:
            report.append(f"топ-3 самых частых слов: Топ 1: {top_items[0][0]}, количество слов: {top_items[0][1]}, "
                                                   f"Топ 2: {top_items[1][0]}, количество слов: {top_items[1][1]}, "
                                                   f"Топ 3: {top_items[2][0]}, количество слов: {top_items[2][1]}")
    else:
        report.append("Количество повторов: 0")
    report.append(f"Количество уникальных слов: {unique_words_count}")
    return report

    
def show_report(report):
    print("\n".join(report))


def save_report(report, report_path):
    with open(report_path, "w", encoding="utf-8") as file:
        file.write("\n".join(report))


try:
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
        file.seek(0)
        words = text.split()
        normalized_words = get_normalized_words(words)
        if not normalized_words:
            print("В файле нет текста")
        else:
            long_small_word = get_longest_smallest_word(normalized_words)
            count = line_count(file)
            top = get_top3_words(normalized_words)
            unique_words_count = get_unique_words_count(top)
            report = get_report(text, normalized_words, long_small_word, count, top, unique_words_count)
            show_report(report)
            save_report(report, report_path)

except FileNotFoundError:
    print("Файл не найден")
