import sqlite3

def init_db():
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    # Создаем таблицу для заметок, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    ''')
    conn.commit()
    return conn

def add_note_to_db(note, conn):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO notes (content) VALUES (?)', (note,))
    conn.commit()

def read_notes_from_db(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM notes')
    notes = cursor.fetchall()
    return notes

def OpenWrite(inc):
    # Записываем заметку в текстовый файл
    with open("input.txt", 'a+') as file:
        file.write(inc + '\n')

def ReadFile():
    # Читаем и выводим содержимое текстового файла
    with open("input.txt", 'r') as file:
        content = file.read()
        print("-----------Вывод-----------\n")
        print("-> ", content)

if __name__ == "__main__":
    print("-----------Заметки-----------\n")
    AdStr = input("Введите текст для добавления: ")

    # Инициализируем базу данных
    conn = init_db()

    # Добавляем заметку в базу данных
    add_note_to_db(AdStr, conn)

    # Записываем заметку в текстовый файл
    OpenWrite(AdStr)

    # Читаем заметки из базы данных
    notes = read_notes_from_db(conn)
    print("-----------Заметки из базы данных-----------\n")
    for note in notes:
        print(f"ID: {note[0]}, Заметка: {note[1]}")

    # Читаем и выводим содержимое текстового файла
    ReadFile()

    # Закрываем соединение с базой данных
    conn.close()