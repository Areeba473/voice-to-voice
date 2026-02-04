import gradio as gr
from stt import speech_to_text
from llm import llm_response
from tts import text_to_speech

def voice_to_voice(audio):
    user_text = speech_to_text(audio)
    ai_text = llm_response(user_text)
    ai_audio = text_to_speech(ai_text)
    return ai_text, ai_audio

theme = gr.themes.Soft(
    primary_hue="blue",
    secondary_hue="gray",
    neutral_hue="slate",
)

app = gr.Interface(
    fn=voice_to_voice,
    inputs=gr.Audio(type="filepath", label="🎤 Speak"),
    outputs=[
        gr.Textbox(label="📝 AI Response"),
        gr.Audio(label="🔊 AI Voice")
    ],
    title="Voice to Voice AI",
    description="Whisper → Groq → Google TTS",
    theme=theme
)

app.launch()
