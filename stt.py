from faster_whisper import WhisperModel
import os

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

def speech_to_text(audio_path):
    # Safety check
    if audio_path is None:
        return ""

    if not isinstance(audio_path, str):
        raise ValueError(f"Expected file path, got {type(audio_path)}")

    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    segments, _ = model.transcribe(audio_path)
    text = " ".join(segment.text for segment in segments)
    return text
