import sqlite3
import time

class NotesDB:
    def __init__(self, db_file='notes.db'):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                content TEXT,
                created TEXT,
                last_modified TEXT,
                pinned INTEGER
            );
            '''
        )
        self.conn.commit()

    def add_note(self, title='-', content='-', pinned=0):
        current_timestamp = int(time.time())
        self.cursor.execute(
            '''
            INSERT INTO notes (title, content, created, last_modified, pinned)
            VALUES (?,?,?,?,?);
            ''',
            (title, content, current_timestamp, current_timestamp, pinned)
        )
        self.conn.commit()

    def get_list_of_notes(self):
        self.cursor.execute(
            '''
            SELECT id, title, created, last_modified, pinned
            FROM notes
            ORDER BY pinned DESC, last_modified DESC
            '''
        )
        return self.cursor.fetchall()

    def get_note_by_id(self, id):
        self.cursor.execute(
            '''
            SELECT id, title, content, created, last_modified, pinned
            FROM notes
            WHERE id=?;
            ''',
            (id,)
        )
        return self.cursor.fetchone()

    def update_note(self, id, title, content, pinned):
        current_timestamp = int(time.time())
        self.cursor.execute(
            '''
            UPDATE notes
            SET title=?, content=?, last_modified=?, pinned=?
            WHERE id=?;
            ''',
            (title, content, current_timestamp, pinned, id)
        )
        self.conn.commit()

    def delete_note(self, id):
        self.cursor.execute(
            '''
            DELETE FROM notes
            WHERE id=?;
            ''',
            (id,)
        )
        self.conn.commit()

    def delete_all_notes(self):
        self.cursor.execute(
            '''
            DELETE FROM notes;
            '''
        )
        self.conn.commit()

    def search_notes(self, word):
        self.cursor.execute(
            '''
            SELECT id, title, created, last_modified, pinned
            FROM notes
            WHERE title LIKE ? OR content LIKE ?;
            ''',
            ('%' + word + '%', '%' + word + '%')
        )
        return self.cursor.fetchall()



if __name__ == '__main__':
    db = NotesDB('notes.db')

    # add a new note
    db.add_note('Test note', 'This is a test note', 1)
    db.add_note('Test note 2', '2', 0)
    quit()
    # retrieve a list of all notes
    list_of_notes = db.get_list_of_notes()
    print('List of notes:', list_of_notes)

    # retrieve a note by id
    note = db.get_note_by_id(list_of_notes[0][0])
    print('Note by id:', note)

    # update a note
    db.update_note(list_of_notes[0][0], 'Updated title', 'Updated content', 0, 1)
    updated_note = db.get_note_by_id(list_of_notes[0][0])
    print('Updated note:', updated_note)

    # delete a note
    db.delete_note(list_of_notes[0][0])
    list_of_notes = db.get_list_of_notes()
    print('List of notes after deleting one:', list_of_notes)

    # delete all notes
    db.delete_all_notes()
    list_of_notes = db.get_list_of_notes()
    print('List of notes after deleting all:', list_of_notes)

    # search notes
    db.add_note('Test note 1', 'This is a test note 1', 0, 0)
    db.add_note('Test note 2', 'This is a test note 2', 1, 1)
    notes = db.search_notes('note')
    print('Notes found by search:', notes)

