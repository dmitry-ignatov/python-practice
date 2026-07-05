import sqlite3


def normalize_text(text):
    words = text.split()
    text_normalized = " ".join(words)
    return text_normalized


def create_table():
    connection = sqlite3.connect("books.db")
    connection.execute("""CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT, 
                    author TEXT, 
                    status TEXT)
                    """)
    connection.commit()
    return connection


def show_menu():
    print("""1. Добавить книгу\n2. Показать все книги\n3. Удалить книгу
4. Найти книгу\n5. Изменить статус книги\n6. Показать статистику\n7. Очистить каталог\n0. Выход\n""")


def get_command():
    try:
        command = int(input("Введите команду: "))
        return command
    except ValueError:
        print("Введите число\n")
        return

def get_book_status():
    while True:
        try:
            book_status_number = int(input("Выберите номер статуса (1 - Запланировано, 2 - Читаю, 3 - Прочтено): "))
            if book_status_number == 1:
                book_status = "Запланировано"
                return book_status
            elif book_status_number == 2:
                book_status = "Читаю"
                return book_status
            elif book_status_number == 3:
                book_status = "Прочтено"
                return book_status
            else:
                print("Введите нужный номер статуса\n")
                continue
        except ValueError:
            print("Введите нужный номер статуса\n")
            continue


def insert_book(connection):
    while True:
        book_name = input("Введите название книги: ")
        book_name_normalized = normalize_text(book_name)
        if not book_name_normalized:
            print("Введите название\n")
            continue
        else:
            break
    while True:
        author_name = input("Введите имя автора: ")
        author_name_normalized = normalize_text(author_name)
        if not author_name_normalized:
            print("Введите имя\n")
            continue
        else:
            break

    book_status = get_book_status()

    connection.execute("INSERT INTO books (title, author, status) VALUES (?, ?, ?)", (book_name_normalized, author_name_normalized, book_status))
    connection.commit()
    print("Книга добавлена\n")


def show_books(connection, search_check):
    cursor = connection.execute("SELECT id, title, author, status FROM books ORDER BY id ASC")
    books = cursor.fetchall()
    if not books:
        print("Книг в каталоге нет\n")
        return
    else:
        if search_check:
            return True
        print("Книги в каталоге:")
        for id, title, author, status in books:
            print(f"{id}. {title}, Автор: {author}, Статус: {status}")
        print()
        return True


def get_book_id(connection, prompt):
    while True:
        try:
            book_number = int(input(f"Введите номер книги для {prompt} (0 - Вернуться назад): "))
            if book_number < 0:
                print("Неверный номер книги\n")
                continue
            elif book_number == 0:
                print()
                return
            cursor = connection.execute("SELECT id FROM books WHERE id = ?", (book_number,))
            book_id = cursor.fetchone()
            if not book_id:
                print("Книги с таким номером нет в каталоге\n")
                continue
            return book_number
        except ValueError:
            print("Введите число\n")
            continue


def delete_book(connection):
    search_check = False
    empty_catalog = show_books(connection, search_check)
    if empty_catalog is None:
        return
    else:
        book_number = get_book_id(connection, "удаления")
        if book_number is None:
            return
        connection.execute("DELETE FROM books WHERE id = ?", (book_number,))
        connection.commit()
        print("Книга удалена\n")
        return


def search_book(connection):
    search_check = True     # Добавляю проверку чтобы при поиске не выводился список книг лишний раз
    empty_catalog = show_books(connection, search_check)
    while True:
        if empty_catalog is None:
            return
        search_text = input("Введите название книги, имя автора или статус (0 - Вернуться назад): ")
        if search_text == "0":
            print()
            return
        search_text_normalized = normalize_text(search_text)
        if not search_text_normalized:
            print("Введите текст\n")
            continue
        else:
            break
    cursor = connection.execute("SELECT id, title, author, status FROM books ORDER BY id ASC")
    books = cursor.fetchall()
    found_books = []
    search_text_normalized_lower = search_text_normalized.lower()
    for id, title, author, status in books:
        if search_text_normalized_lower in title.lower() or search_text_normalized_lower in author.lower() or search_text_normalized_lower in status.lower():
            found_books.append((id, title, author, status))
    if not found_books:
        print("Книги не найдены\n")
    else:
        print("Найденные книги:")
        for id, title, author, status in found_books:
            print(f"{id}. {title}, Автор: {author}, Статус: {status}")
        print()


def change_book_status(connection):
    search_check = False
    empty_catalog = show_books(connection, search_check)
    if empty_catalog is None:
        return
    book_number = get_book_id(connection, "изменения")
    if book_number is None:
        return
    book_status = get_book_status()
    connection.execute("UPDATE books SET status = ? WHERE id = ?", (book_status, book_number))
    connection.commit()
    print(f"Статус книги изменен на '{book_status}'\n")


def show_statistics(connection):
    cursor = connection.execute("SELECT id, title, author, status FROM books")
    books = cursor.fetchall()
    if not books:
        print("Книг в каталоге нет\n")
        return
    planned_count = 0
    reading_count = 0
    finished_count = 0
    for _, _, _, status in books:
        if status == "Запланировано":
            planned_count += 1
        elif status == "Читаю":
            reading_count += 1
        elif status == "Прочтено":
            finished_count += 1
    print(f"Всего книг: {len(books)}")
    print(f"Книг со статусом 'Запланировано': {planned_count}")
    print(f"Книг со статусом 'Читаю': {reading_count}")
    print(f"Книг со статусом 'Прочтено': {finished_count}\n")


def delete_all_books(connection):
    while True:
        answer = input("Вы действительно хотите очистить весь каталог? y/n: ")
        answer_normalized_lower = normalize_text(answer).lower()
        if answer_normalized_lower == "y":
            connection.execute("DELETE FROM books")
            connection.commit()
            print("Все книги удалены\n")
            return
        elif answer_normalized_lower == "n":
            print("Действие отменено\n")
            return
        else:
            print("Введите y или n\n")
            continue


def main():
    connection = create_table()

    while True:
        show_menu()

        command = get_command()
        if command is None:
            continue


        elif command > 7 or command < 0:
            print("Неверный номер команды\n")


        elif command == 1:
            insert_book(connection)
        

        elif command == 2:
            search_check = False
            show_books(connection, search_check)


        elif command == 3:
            delete_book(connection)


        elif command == 4:
            search_book(connection)


        elif command == 5:
            change_book_status(connection)


        elif command == 6:
            show_statistics(connection)


        elif command == 7:
            delete_all_books(connection)


        elif command == 0:
            connection.close()
            break



if __name__ == "__main__":
    main()