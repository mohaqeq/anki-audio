import sqlite3

import torch
from model import NOTE_QUERY, Note
from TTS.api import TTS

conn = sqlite3.connect("./collection.anki2")
cursor = conn.cursor()


cursor.execute(NOTE_QUERY)
notes = [Note(*row) for row in cursor.fetchall()]

# only a test here
# notes = [notes[0]]
device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

print(f"Total entries: {len(notes)}")
for num, note in enumerate(notes):
    print(f"{num}: {note.german_word}")
    tts.tts_to_file(
        text=f"{note.german_word}. {note.german_sentence}",
        speaker="Filip Traverse",
        language="de",
        file_path=f"./audio/{note.note_id}.wav",
        split_sentences=False
    )
