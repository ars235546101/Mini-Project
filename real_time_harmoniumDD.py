import sounddevice as sd
import numpy as np
from scipy import signal
import aubio

# Parameters
sample_rate = 44100
buffer_size = 512  # Sounddevice buffer
aubio_buffer_size = buffer_size // 2  # Aubio la half buffer pahije
hop_size = aubio_buffer_size // 2  # Aubio la quarter hop pahije

# Initialize pitch detector
pitch_detector = aubio.pitch("default", aubio_buffer_size, hop_size, sample_rate)
pitch_detector.set_unit("Hz")
pitch_detector.set_tolerance(0.8)

# Function to map frequency to nearest note
def frequency_to_note(frequency):
    NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    if frequency == 0:
        return "No note detected"
    note_index = int(round(np.log2(frequency / 440) * 12))
    octave = (note_index // 12) + 4
    note = NOTES[note_index % 12]
    return f"{note}{octave}"

# Function to generate harmonium sound
def generate_harmonium_sound(frequency, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    sawtooth_wave = 0.5 * signal.sawtooth(2 * np.pi * frequency * t)
    square_wave = 0.3 * signal.square(2 * np.pi * frequency * t, duty=0.5)
    harmonium_sound = sawtooth_wave + square_wave
    harmonium_sound /= np.max(np.abs(harmonium_sound))
    return harmonium_sound

# Callback function for real-time audio processing
def audio_callback(indata, frames, time, status):
    if status:
        print("Error:", status)
    
    # Convert input to float32 and trim it to aubio_buffer_size
    samples = np.mean(indata, axis=1).astype(np.float32)
    samples = samples[:hop_size]  # **Exact 128 pathavtoy**

    # Detect frequency
    frequency = pitch_detector(samples)[0]

    if frequency > 0:
        print(f"Detected Frequency: {frequency:.2f} Hz → Nearest Note: {frequency_to_note(frequency)}")
        
        # Generate and play harmonium sound
        harmonium_sound = generate_harmonium_sound(frequency, 1, sample_rate)
        sd.play(harmonium_sound, sample_rate)

# Start real-time audio stream
try:
    with sd.InputStream(callback=audio_callback, channels=1, samplerate=sample_rate, blocksize=buffer_size):
        print("Real-time harmonium synthesis started. Press Ctrl+C to stop.")
        while True:
            sd.sleep(1000)
except KeyboardInterrupt:
    print("\nProgram exited safely.")
