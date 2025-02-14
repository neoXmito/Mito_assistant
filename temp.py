import pyttsx3

engine = pyttsx3.init()
engine.say("Catherine")
engine.runAndWait()

from gtts import gTTS
import os

tts = gTTS(text="Catherine", lang="en")
tts.save("wake_word.mp3")
os.system("wake_word.mp3")  # Play the file
