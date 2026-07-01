import sqlite3



def normalize_text(text):
    words = text.split()
    text_normalized = " ".join(words)
    return text_normalized


connection = sqlite3.connect("notes.db")
connection.execute(""" 
                    CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    text TEXT
                    ) 
                    """)
connection.commit()

while True:

    print("1. Добавить заметку\n2. Показать заметки\n0. Выход\n")
    try:
        command = int(input("Введите команду: "))
    except ValueError:
        print("Введите номер команды\n")
        continue

    if command > 2 or command < 0:
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
        cursor = connection.execute("SELECT id, text FROM notes")
        notes = cursor.fetchall()
        if not notes:
            print("Заметок пока нет\n")
        else:
            for note_id, text in notes:
                print(f"{note_id}. {text}")
            print()

    
    elif command == 0:
        connection.close()
        break