import sqlite3

def normalize_text(text):
    words = text.split()
    text_normalized = " ".join(words)
    return text_normalized


note_text = input("Введите заметку: ")
note_text_normalized = normalize_text(note_text)

if not note_text_normalized:
    print("Введена пустая строка")
else:
    connection = sqlite3.connect("notes.db")
    connection.execute(""" 
                    CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    text TEXT
                    ) 
                    """)

    connection.execute("INSERT INTO notes (text) VALUES (?)", (note_text_normalized,))
    connection.commit()

    cursor = connection.execute("SELECT id, text FROM notes")
    notes = cursor.fetchall()
    connection.close()

    for note_id, text in notes:
        print(f"{note_id}. {text}")