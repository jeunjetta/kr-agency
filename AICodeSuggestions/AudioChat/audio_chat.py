from speech_recognition_util import recognize_speech_from_microphone
from text_to_speech_util import convert_text_to_speech

def audio_chat():
    text = recognize_speech_from_microphone()
    if text:
        convert_text_to_speech("You said: " + text)
    else:
        convert_text_to_speech("I didn't catch that. Could you please repeat?")
