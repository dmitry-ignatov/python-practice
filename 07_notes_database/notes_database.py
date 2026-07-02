import sqlite3



def normalize_text(text):
    words = text.split()
    text_normalized = " ".join(words)
    return text_normalized


def show_notes(connection):
    cursor = connection.execute("SELECT id, text FROM notes")
    notes = cursor.fetchall()
    empty_notes = False
    if not notes:
        print("Заметок пока нет\n")
        empty_notes = True
        return empty_notes
    else:
        print("Текущие заметки: ")
        for note_id, text in notes:
            print(f"{note_id}. {text}")
        print()
        return False


connection = sqlite3.connect("notes.db")
connection.execute(""" 
                    CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    text TEXT
                    ) 
                    """)
connection.commit()

while True:

    print("1. Добавить заметку\n2. Показать заметки\n3. Удалить заметку\n0. Выход\n")
    try:
        command = int(input("Введите команду: "))
    except ValueError:
        print("Введите номер команды\n")
        continue

    if command > 3 or command < 0:
        print("Такой команды нет\n")


    elif command == 1:
        note_text = input("Введите заметку: ")
        note_text_normalized = normalize_text(note_text)

        if not note_text_normalized:
            print("Введена пустая строка\n")
        else:
            print()
            connection.execute("INSERT INTO notes (text) VALUES (?)", (note_text_normalized,))
            connection.commit()


    elif command == 2:
        show_notes(connection)
    
    elif command == 3:
        empty_notes = show_notes(connection)

        if not empty_notes:
            while True:
                try:
                    note_id = int(input("Введите номер заметки для удаления: "))
                    if note_id <= 0:
                        print("Неверный номер заметки")
                        continue
                    cursor = connection.execute("DELETE FROM notes WHERE id = ?", (note_id,))
                    if cursor.rowcount == 0:
                        print("Неверный номер заметки")
                    else:
                        connection.commit()
                        print("Заметка удалена\n")
                        break
                except ValueError:
                    print("\nВведите число\n")
                    continue


    elif command == 0:
        connection.close()
        break