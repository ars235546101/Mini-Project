import sounddevice as sd
import numpy as np

duration = 5
sample_rate = 44100

def capture_audio(duration, sample_rate):
    print("Recording started...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
    sd.wait()
    print("Recording finished!")
    return audio_data

audio_data = capture_audio(duration, sample_rate)

print("Playing back the recorded audio...")
sd.play(audio_data, sample_rate)
sd.wait()