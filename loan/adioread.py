import pyttsx3

def audioread(statement):
    speaker = pyttsx3.init()
    speaker.say(statement)
    speaker.runAndWait()