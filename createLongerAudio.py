from pydub import AudioSegment

def loop_audio(input_filename, output_filename, duration_hours):
    # Load the input audio file
    original_sound = AudioSegment.from_file(input_filename)

    # Calculate how many times we need to loop the sound to reach the desired duration
    times_to_repeat = round((duration_hours * 60 * 60) / (len(original_sound) / 1000))

    # Loop the sound
    looped_sound = original_sound * times_to_repeat

    # Save the looped sound to a file
    looped_sound.export(output_filename, format="wav")

# Call the function
loop_audio("ACNoiseLoopable.wav", "one_hour.wav", 1)