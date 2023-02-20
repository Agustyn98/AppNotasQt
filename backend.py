import sqlite3
import time
import os
import platform
import getpass


class NotesDB:
    def __init__(self):
        db_name = "notes.db"
        dir_path = NotesDB.get_dir_path()
        db_path = os.path.join(dir_path, db_name)
        self.create_config()
        print(f"connecting to database at: {db_path}")
        self.conn = sqlite3.connect(db_path)
        # Create a new, in-memory database
        self.cursor = self.conn.cursor()

        self.cursor.execute("PRAGMA synchronous = OFF;")
        self.conn.execute("PRAGMA temp_store = 2;")
        self.conn.execute("PRAGMA journal_mode = OFF")
        self.conn.execute("PRAGMA cache_size = 50000")
        self.conn.commit()

        self.create_table()

    app_dir = ""

    @staticmethod
    def get_dir_path() -> str:
        app_dir_name = "appnotas"
        home = os.path.expanduser("~")
        current_os = platform.system()

        if current_os == "Windows":
            NotesDB.app_dir = os.path.join(home, "AppData", "Local", app_dir_name)
        elif current_os == "Darwin":
            username = getpass.getuser()
            NotesDB.app_dir = os.path.join(
                home, "Library", "Application Support", app_dir_name
            )
        else:
            username = getpass.getuser()
            NotesDB.app_dir = os.path.join(home, f".{app_dir_name}")

        if not os.path.exists(NotesDB.app_dir):
            os.makedirs(NotesDB.app_dir)

        return NotesDB.app_dir

    config_path = ""

    @staticmethod
    def create_config():
        config_filename = "config"
        NotesDB.config_path = os.path.join(NotesDB.app_dir, config_filename)
        if not os.path.exists(NotesDB.config_path):
            with open(NotesDB.config_path, "w") as f:
                f.write(
                    "textbox_font_size:18\nui_font_size:18\nwindow_size:900x700\nwindow_center:true\n"
                )

        # print(f' CREATED CONFIG AT {self.config_path}')
        return NotesDB.config_path

    def _query_pragma(self):
        cursor = self.conn.execute("PRAGMA cache_size")
        cache_size = cursor.fetchone()[0]
        print(f"Current cache size is {cache_size} pages")

        cursor = self.conn.execute("PRAGMA temp_store")
        temp_store = cursor.fetchone()[0]
        print(f"Current temp_store is {temp_store}")

        cursor = self.conn.execute("PRAGMA journal_mode")
        journal_mode = cursor.fetchone()[0]
        print(f"Current journal mode is {journal_mode}")

        cursor = self.conn.execute("PRAGMA synchronous")
        synchronous_mode = cursor.fetchone()[0]
        print(f"Current synchronous mode is {synchronous_mode}")

    def create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                content TEXT,
                created INTEGER,
                last_modified INTEGER,
                pinned INTEGER
            );
            """
        )
        self.conn.commit()

    def add_note(self, title="New Note", content="", pinned=0):
        current_timestamp = int(time.time())
        self.cursor.execute(
            """
            INSERT INTO notes (title, content, created, last_modified, pinned)
            VALUES (?,?,?,?,?);
            """,
            (title, content, current_timestamp, current_timestamp, pinned),
        )
        self.conn.commit()

    def get_list_of_notes(self):
        self.cursor.execute(
            """
            SELECT id, title, created, last_modified, pinned
            FROM notes
            ORDER BY pinned DESC, last_modified DESC
            """
        )
        return self.cursor.fetchall()

    def get_note_by_id(self, id):
        self.cursor.execute(
            """
            SELECT id, title, content, created, last_modified, pinned
            FROM notes
            WHERE id=?;
            """,
            (id,),
        )
        return self.cursor.fetchone()


    def update_note(self, id, content):
        #current_timestamp = int(time.time())
        self.cursor.execute(
            """
            UPDATE notes
            SET content=?, last_modified=STRFTIME('%s')
            WHERE id=?;
            """,
            (content, id),
        )
        self.conn.commit()
    

    def update_note_title(self, id, title):
        current_timestamp = int(time.time())
        self.cursor.execute(
            """
            UPDATE notes
            SET title=?, last_modified=?
            WHERE id=?;
            """,
            (title, current_timestamp, id),
        )
        self.conn.commit()
    

    def update_note_pin(self, id, pin):
        self.cursor.execute(
            """
            UPDATE notes
            SET pinned=?
            WHERE id=?;
            """,
            (pin, id),
        )
        self.conn.commit()


    def delete_note(self, id):
        self.cursor.execute(
            """
            DELETE FROM notes
            WHERE id=?;
            """,
            (id,),
        )
        self.conn.commit()

    def delete_all_notes(self):
        self.cursor.execute(
            """
            DELETE FROM notes;
            """
        )
        self.conn.commit()

    def search_notes(self, word):
        self.cursor.execute(
            """
            SELECT id, title, created, last_modified, pinned
            FROM notes
            WHERE title LIKE ? OR content LIKE ?
            ORDER BY pinned DESC, last_modified DESC;
            """,
            ("%" + word + "%", "%" + word + "%"),
        )
        return self.cursor.fetchall()


if __name__ == "__main__":
    db = NotesDB("notes.db")

    db.get_dir_path()
    quit()
    # add a new note
    db.add_note("Test note", "This is a test note", 1)
    db.add_note("Test note 2", "2", 0)
    l = db.get_list_of_notes()
    print(l)
    print("Now querying info...")
    db._query_pragma()
    # retrieve a list of all notes
    list_of_notes = db.get_list_of_notes()
    print("List of notes:", list_of_notes)

    # retrieve a note by id
    note = db.get_note_by_id(list_of_notes[0][0])
    print("Note by id:", note)

    # update a note
    db.update_note(list_of_notes[0][0], "Updated title", "Updated content", 0, 1)
    updated_note = db.get_note_by_id(list_of_notes[0][0])
    print("Updated note:", updated_note)

    # delete a note
    db.delete_note(list_of_notes[0][0])
    list_of_notes = db.get_list_of_notes()
    print("List of notes after deleting one:", list_of_notes)

    # delete all notes
    db.delete_all_notes()
    list_of_notes = db.get_list_of_notes()
    print("List of notes after deleting all:", list_of_notes)

    # search notes
    db.add_note("Test note 1", "This is a test note 1", 0, 0)
    db.add_note("Test note 2", "This is a test note 2", 1, 1)
    notes = db.search_notes("note")
    print("Notes found by search:", notes)
