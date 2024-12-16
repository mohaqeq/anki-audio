import sqlite3

from .model import NOTE_QUERY, Note

conn = sqlite3.connect("./collection.anki2")
cursor = conn.cursor()

update = """
UPDATE notes
SET flds = ?
WHERE id = ?
"""

# get all notes from frequency table
cursor.execute(NOTE_QUERY)
notes = [Note(*row) for row in cursor.fetchall()]

for note in notes:
    fields = note.note_fields
    note_data = fields.split('\x1f')
    note_data[-1] = f'[sound:{note.note_id}.mp3]'
    note.note_fields = "\x1f".join(note_data)
    # We make the update to the deck itself.
    cursor.execute(update, (note.note_fields, note.note_id))

conn.close()
