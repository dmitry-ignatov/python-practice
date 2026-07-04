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
    print("""1. Добавить книгу\n2. Показать все книги\n3. Изменить книгу\n4. Удалить книгу
5. Найти книгу\n6. Изменить статус книги\n7. Показать статистику\n8. Очистить каталог\n0. Выход""")


connection = create_table()

while True:
    show_menu()

    try:
        command = int(input("Введите команду: "))
    except ValueError:
        print("Введите число\n")
        continue

    if command > 8 or command < 0:
        print("Неверный номер команды\n")


    elif command == 1:
        book_name = input("Введите название книги: ")
        book_name_normalized = normalize_text(book_name)
        author_name = input("Введите имя автора: ")
        author_name_normalized = normalize_text(author_name)

        connection.execute("INSERT INTO books (title, author) VALUES (?, ?)",(book_name_normalized, author_name_normalized))
        connection.commit()
        print()
    

    elif command == 2:
        cursor = connection.execute("SELECT id, title, author FROM books ORDER BY id ASC")
        books = cursor.fetchall()
        if not books:
            print("Книг в каталоге нет")
        else:
            for id, title, author in books:
                print(f"{id}. {title}, Автор: {author}")
            print()

    
    elif command == 0:
        connection.close()
        break