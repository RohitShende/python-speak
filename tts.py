import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-70)

def say(msg):
    engine.say(msg)
    engine.runAndWait()

# say("lets get going bro")
