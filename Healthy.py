from gtts import gTTS
from playsound import playsound
import time
speech=gTTS("Good morning, welcome to office")
speech.save("hello.mp3")
speech=gTTS("time to do eye exercise")
speech.save("eye.mp3")
speech=gTTS("time to drink water")
speech.save("water.mp3")
speech=gTTS("time to do physical exercise")
speech.save("physical.mp3")
def play_audio(tc):
    playsound(tc)
now=time.strftime('%H:%M:%S')
if(now<='09:10:00'):
        play_audio("hello.mp3")
if(now>='09:00:00' and now<='17:00:00'):
    while(now>='09:00:00' and now<='17:00:00'):
        time.sleep(1800)
        play_audio("eye.mp3")
        time.sleep(900)
        play_audio("water.mp3")
        time.sleep(2100)
        play_audio("physical.mp3")
        time.sleep(5)
        now=time.strftime('%H:%M:%S')
        continue