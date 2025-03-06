import sounddevice as sd
import numpy as np
import aubio

duration = 5
sample_rate = 44100

def capture_audio(duration, sample_rate):
    print("Recording started...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
    sd.wait()
    print("Recording finished!")
    return audio_data.flatten()

audio_data = capture_audio(duration, sample_rate)

pitch_detector = aubio.pitch("default", 2048, 2048//2, sample_rate)
pitch_detector.set_unit("Hz")
pitch_detector.set_tolerance(0.8)

# Process audio data in chunks of 1024 samples
chunk_size = 1024
frequencies = []

for i in range(0, len(audio_data), chunk_size):
    chunk = audio_data[i:i + chunk_size]
    if len(chunk) == chunk_size:
        frequency = pitch_detector(chunk)[0]
        frequencies.append(frequency)

# Calculate average frequency
if frequencies:
    average_frequency = np.mean(frequencies)
    print(f"Detected Frequency: {average_frequency:.2f} Hz")
else:
    print("No frequency detected.")