import numpy as np
from scipy import signal
import sounddevice as sd

# Parameters
frequency = 100.50  # Replace with your detected frequency
duration = 3  # Duration of sound in seconds
sample_rate = 44100  # Sampling rate (44.1 kHz is standard)

# Generate sawtooth wave (harmonium-like sound)
t = np.linspace(0, duration, int(sample_rate * duration), False)
sawtooth_wave = 0.5 * signal.sawtooth(2 * np.pi * frequency * t)

# Generate square wave (add harmonics for richness)
square_wave = 0.3 * signal.square(2 * np.pi * frequency * t, duty=0.5)

# Combine waves to create harmonium sound
harmonium_sound = sawtooth_wave + square_wave

# Normalize audio to avoid clipping
harmonium_sound /= np.max(np.abs(harmonium_sound))

# Play the generated sound
print("Playing harmonium sound...")
sd.play(harmonium_sound, sample_rate)
sd.wait()