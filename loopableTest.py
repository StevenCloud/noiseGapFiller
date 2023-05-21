from pydub import AudioSegment
from pydub.playback import play
import pyaudio
import numpy as np

# Load audio file
audio = AudioSegment.from_file("ACNoiseLoopable.wav")

# Convert audio file to numpy array
data = np.array(audio.get_array_of_samples())

# Open PyAudio
p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(audio.sample_width),
                channels=audio.channels,
                rate=audio.frame_rate,
                output=True)

# Play audio in a loop
while True:
    stream.write(data.tobytes())

# Close PyAudio
stream.stop_stream()
stream.close()
p.terminate()