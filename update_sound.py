"""
If you modify files manually in the media directory. These changes won't be
propagated automatically. We need a database update for these changes to be
synched to the server.
"""

import hashlib
import os
import sqlite3
import time
from pathlib import Path

conn = sqlite3.connect("./anki_dir/collection.media.db2")
cursor = conn.cursor()

media_files = os.walk(Path("./anki_dir/collection.media"))

WEEK = 3600 * 24 * 7


def calculate_anki_checksum(file_path):
    """Calculate Anki-style checksum for media files"""
    # Anki uses first 8 digits of MD5 hash
    with open(file_path, "rb") as f:
        file_hash = hashlib.sha1(f.read()).hexdigest()
    return file_hash


update = """
UPDATE media
SET mtime = ?,
    csum = ?,
    dirty = 1
WHERE fname = ?;
"""


for path, _, files in media_files:
    for _file in files:
        filepath = Path(path) / Path(_file)
        modified_time = os.path.getmtime(filepath)
        past_week = time.time() - WEEK
        if modified_time > past_week:
            checksum = calculate_anki_checksum(filepath)
            cursor.execute(update, (int(modified_time), checksum, _file))
            conn.commit()
            print(f"File {_file} updated")
