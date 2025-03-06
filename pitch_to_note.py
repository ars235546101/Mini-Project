import numpy as np

# Function to map frequency to nearest note
def frequency_to_note(frequency):
    # Standard notes and their frequencies (A4 = 440 Hz)
    NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    OCTAVE_MULTIPLIER = 2  # Each octave doubles the frequency

    # Calculate the nearest note
    if frequency == 0:
        return "No note detected"

    # Find the nearest note and octave
    note_index = int(round(np.log2(frequency / 440) * 12))  # 12 notes per octave
    octave = (note_index // 12) + 4  # A4 is the reference note
    note = NOTES[note_index % 12]

    return f"{note}{octave}"

# Test with detected frequency
detected_frequency = 100.50  # Replace with your detected frequency
nearest_note = frequency_to_note(detected_frequency)
print(f"Detected Frequency: {detected_frequency:.2f} Hz → Nearest Note: {nearest_note}")