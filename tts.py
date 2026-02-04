from gtts import gTTS
import uuid

def text_to_speech(text: str) -> str:
    filename = f"reply_{uuid.uuid4()}.mp3"
    tts = gTTS(text=text, lang="en")
    tts.save(filename)
    return filename
