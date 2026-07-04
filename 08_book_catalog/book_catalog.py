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


def insert_book(connection):
    while True:
        book_name = input("Введите название книги: ")
        book_name_normalized = normalize_text(book_name)
        if not book_name_normalized:
            print("Введиет название\n")
            continue
        else:
            break
    while True:
        author_name = input("Введите имя автора: ")
        author_name_normalized = normalize_text(author_name)
        if not author_name_normalized:
            print("Введиет имя\n")
            continue
        else:
            break
    while True:
        try:
            book_status_number = int(input("Выберите номер статуса (1 - Запланировано, 2 - Читаю, 3 - Прочтено): "))
            if book_status_number == 1:
                book_status = "Запланировано"
                break
            elif book_status_number == 2:
                book_status = "Читаю"
                break
            elif book_status_number == 3:
                book_status = "Прочтено"
                break
            else:
                print("Введите нужный номер статуса\n")
                continue
        except ValueError:
            print("Введите нужный номер статуса\n")
            continue

    connection.execute("INSERT INTO books (title, author, status) VALUES (?, ?, ?)",(book_name_normalized, author_name_normalized, book_status))
    connection.commit()
    print("Книга добавлена\n")


def show_books(connection):
    cursor = connection.execute("SELECT id, title, author, status FROM books ORDER BY id ASC")
    books = cursor.fetchall()
    if not books:
        print("Книг в каталоге нет\n")
        return
    else:
        print("Книги в каталоге:")
        for id, title, author, status in books:
            print(f"{id}. {title}, Автор: {author}, Статус: {status}")
        print()
        return True


def get_book_id(connection, prompt):
    while True:
        try:
            book_number = int(input(f"Введите номер книги для {prompt}: "))
            if book_number <= 0:
                print("Неверный номер книги\n")
                continue
            cursor = connection.execute("SELECT id FROM books WHERE id = ?", (book_number,))
            book_id = cursor.fetchone()
            if not book_id:
                print("Книги с таким номер нет в каталоге\n")
                continue
            return book_number
        except ValueError:
            print("Введите число\n")
            continue


def delete_book(connection):
    while True:
        empty_catalog = show_books(connection)
        if empty_catalog is None:
            break
        else:
            book_number = get_book_id(connection, "удаления")
            connection.execute("DELETE FROM books WHERE id = ?", (book_number,))
            connection.commit()
            print("Книга удалена\n")
            break


def search_book(connection):
    while True:
        search_text = input("Введите название книги, имя автора или статус: ")
        search_text_normalized = normalize_text(search_text)
        if not search_text_normalized:
            print("Введите текст\n")
            continue
        else:
            break
    cursor = connection.execute("SELECT id, title, author, status FROM books ORDER BY id ASC")
    books = cursor.fetchall()
    if not books:
        print("Книг не найдено\n")
    else:
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



connection = create_table()

while True:
    show_menu()

    try:
        command = int(input("Введите команду: "))
    except ValueError:
        print("Введите число\n")
        continue

    if command > 7 or command < 0:
        print("Неверный номер команды\n")


    elif command == 1:
        insert_book(connection)
    

    elif command == 2:
        show_books(connection)


    elif command == 3:
        delete_book(connection)


    elif command == 4:
        search_book(connection)


    elif command == 0:
        connection.close()
        break