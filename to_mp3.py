import os
from pathlib import Path

audio_dir = Path.cwd() / "audio"
result = next(audio_dir.iterdir())

for _file in audio_dir.iterdir():
    filename_w_parts = _file.parts[-1]
    filename = filename_w_parts.split('.')[0]
    os.system(f"sox ./audio/{filename}.wav -C 64 ./mp3/{filename}.mp3")
