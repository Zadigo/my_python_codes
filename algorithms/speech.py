import speech_recognition
from speech_recognition import Recognizer

speech_recognizer = Recognizer()

with speech_recognition.Microphone() as source:
    audio = speech_recognizer.listen(source)

    try:
        text = speech_recognizer.recognize_google(audio)
        print(text)
    except:
        pass
