from pydub import AudioSegment
from pydub.playback import play
 
import RPi.GPIO as GPIO
import time
import tm1637
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
BUTTON_PIN = 27
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

song = AudioSegment.from_wav('Music1.wav')

while 1>0:
    if GPIO.input(BUTTON_PIN) == GPIO.LOW:
        play(song)  