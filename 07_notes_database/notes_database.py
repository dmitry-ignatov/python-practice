import sqlite3



def normalize_text(text):
    words = text.split()
    text_normalized = " ".join(words)
    return text_normalized


def insert_note(connection):
    note_text = input("Введите заметку: ")
    note_text_normalized = normalize_text(note_text)

    if not note_text_normalized:
        print("Введена пустая строка\n")
    else:
        connection.execute("INSERT INTO notes (text) VALUES (?)", (note_text_normalized,))
        connection.commit()
        print("Заметка добавлена\n")


def show_notes(connection):
    cursor = connection.execute("SELECT id, text FROM notes")
    notes = cursor.fetchall()
    if not notes:
        print("Заметок пока нет\n")
        return True
    else:
        print("Текущие заметки: ")
        for note_id, text in notes:
            print(f"{note_id}. {text}")
        print()
        return False


def get_note_id(connection, prompt):
    note_id = int(input(f"Введите номер заметки для {prompt}: "))
    if note_id <= 0:
        print("Неверный номер заметки")
        return False
    note = connection.execute("SELECT id FROM notes WHERE id = ?", (note_id,))
    if note.fetchone() is None:
        print("Неверный номер заметки")
        return False
    else:
        return note_id


def delete_note(connection):
    empty_notes = show_notes(connection)

    if not empty_notes:
        while True:
            try:
                note_id = get_note_id(connection, "удаления")
                if not note_id:
                    continue
                connection.execute("DELETE FROM notes WHERE id = ?", (note_id,))
                connection.commit()
                print("Заметка удалена\n")
                break
            except ValueError:
                print("\nВведите число\n")
                continue


def update_note(connection):
    empty_notes = show_notes(connection)

    if not empty_notes:
        while True:
            try:
                note_id = get_note_id(connection, "изменения")
                if not note_id:
                    continue
                while True:
                    text = input("Введите новую заметку: ")
                    text_normalized = normalize_text(text)
                    if not text_normalized:
                        print("Введена пустая строка\n")
                        continue
                    else:
                        break
                connection.execute("UPDATE notes SET text = ? WHERE id = ?", (text_normalized, note_id))
                connection.commit()
                print("Заметка изменена\n")
                break
            except ValueError:
                print("\nВведите число\n")
                continue


connection = sqlite3.connect("notes.db")
connection.execute(""" 
                    CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    text TEXT
                    ) 
                    """)
connection.commit()

while True:

    print("1. Добавить заметку\n2. Показать заметки\n3. Удалить заметку\n4. Изменить заметку\n0. Выход\n")

    try:
        command = int(input("Введите команду: "))
    except ValueError:
        print("Введите номер команды\n")
        continue


    if command > 4 or command < 0:
        print("Такой команды нет\n")


    elif command == 1:
        insert_note(connection)


    elif command == 2:
        show_notes(connection)


    elif command == 3:
        delete_note(connection)


    elif command == 4:
        update_note(connection)


    elif command == 0:
        connection.close()
        break