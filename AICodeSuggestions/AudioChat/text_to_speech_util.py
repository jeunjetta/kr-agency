from gtts import gTTS
import os

def convert_text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    filename = '/tmp/temp_audio.mp3'
    tts.save(filename)
    os.system(f"mpg321 {filename}")
