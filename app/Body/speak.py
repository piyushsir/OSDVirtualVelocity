import pyttsx3

def speak(Text):
    eng=pyttsx3.init("sapi5")
    voices=eng.getProperty('voices')
    eng.setProperty('voices',voices[1].id)
    eng.getProperty('rate')
    eng.setProperty('rate','155')
    print("")
    print(f'you : {Text}')
    print("")
    eng.say(Text)
    eng.runAndWait()
