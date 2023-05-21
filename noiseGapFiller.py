import numpy as np
import sounddevice as sd
import pydub
from pydub.playback import play
from threading import Thread, Event
from time import sleep
from pydub import AudioSegment
import io

# load the audio file of the AC sound
ac_sound = pydub.AudioSegment.from_file("ACNoise.wav")
ac_sound_arr = np.array(ac_sound.get_array_of_samples())
sample_rate = ac_sound.frame_rate

class ContinuousPlay(Thread):
    def __init__(self, sound_arr, sample_rate):
        super().__init__()
        self.sound_arr = sound_arr
        self.sample_rate = sample_rate
        self.stop_event = Event()
        self.stream = sd.OutputStream(samplerate=self.sample_rate, channels=1)

    def run(self):
        self.stream.start()
        while not self.stop_event.is_set():
            self.stream.write(self.sound_arr.astype(np.float32))

    def stop(self):
        self.stop_event.set()
        self.stream.stop()

continuous_player = None

def audio_callback(indata, frames, time, status):
    global continuous_player
    volume_norm = np.linalg.norm(indata)*10
    print("Volume:", volume_norm)
    if volume_norm < 1.5:
        if continuous_player is None or not continuous_player.is_alive():
            continuous_player = ContinuousPlay(ac_sound_arr, sample_rate)
            continuous_player.start()
    else:
        if continuous_player is not None:
            continuous_player.stop()
            continuous_player.join()  # Wait for the thread to finish
            continuous_player = None

with sd.InputStream(callback=audio_callback):
    while True:
        sleep(10)