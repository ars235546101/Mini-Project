import pyaudio
import wave
from array import array
from struct import pack

def record(outputfile):
    CHUNK=1024
    FORMAT=pyaudio.paInt16
    CHANNELS=1
    RATE=44100
    DURATION=5

    p=pyaudio.PyAudio()
    stream=p.open(format=FORMAT, 
                  channels=CHANNELS,
                  rate=RATE,
                  input=True,
                  frames_per_buffer=CHUNK)
    print("Recording...")
    frames=[]
    for i in range(0, int(RATE/CHUNK *DURATION)):
        data=stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf=wave.open(outputfile, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

record('output.wav')