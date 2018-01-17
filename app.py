import stt
import tts

correctness = 0
total = 0

tts.say("Hi, I am a timepass bot. Talk to me..")

while True:
    tts.say("Say Something..")
    audio = stt.listen()
    text = stt.recognize(audio)
    tts.say("You Said, " + text)
    print("You Said, " + text)
    tts.say("Did I gave you the right Answer ? Say Yes, if I did, else say No")
    audio = stt.listen()
    text = stt.recognize(audio)
    if text.lower() == "yes":
        correctness += 1
    total += 1
    tts.say("Do You wish to test me more ? Say Yes or No")
    audio = stt.listen()
    text = stt.recognize(audio)
    if text.lower() == "no":
        tts.say("For your Information I was " + str((correctness * 100) / total) + " percent correct. Bye Bye. See You Again")
        break
    else:
        tts.say("I am Happy that you wish to play with me.")
