import whisper
from pathlib import Path

def transcribe(file_path: str):
    model = whisper.load_model('tiny')
    path = Path(file_path)

    result = model.transcribe(str(path))
    return result