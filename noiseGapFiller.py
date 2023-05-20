import numpy as np
import sounddevice as sd
import pydub
from pydub.playback import play
from time import sleep

# load the audio file of the AC sound
ac_sound = pydub.AudioSegment.from_file("ac_sound.mp3")

def audio_callback(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    print("Volume:", volume_norm)
    if volume_norm < 65:
        play(ac_sound)

with sd.InputStream(callback=audio_callback):
    while True:
        sleep(10)