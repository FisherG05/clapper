#!/usr/bin/python

import pyaudio
import wave
import audioop


_CHUNK = 1024
_SAMPLE_FORMAT = pyaudio.paInt16
_CHANNELS = 1
_FS = 44100
_SECONDS = 3
_FILENAME = "output.wav"

"""



"""
def clapper():

    # initalize the pyaudio interface
    p, s = create_pyaudio_interface()
    frames = []
    print("Recording")

    # records the input for 3 seconds
    try:
        frames = read_input(p, s)
        print("Finished recording")
    except Exception as err:
        print(err)

    # closes all connections
    finally:
        p.close(s)
        p.terminate()
    
    try:
        write_to_wav_file(p, frames)
        print("Finished writing to .wav file")
    except Exception as err:
        print(err)


"""



"""
def create_pyaudio_interface():
    # creates an interface for pyaudio
    p = pyaudio.PyAudio()

    # creates stream
    s = p.open(format=_SAMPLE_FORMAT,
                channels=_CHANNELS,
                rate=_FS,
                frames_per_buffer=_CHUNK,
                input=True)

    return p, s


"""



"""
def read_input(p, s):
    # initializes array for storing the the input
    frames = []

    # reads the input
    for i in range(0, int(_FS / _CHUNK * _SECONDS)):
            data = s.read(_CHUNK)
            frames.append(data)
            display_amplitude(data)
    
    # returns frames
    return frames


"""



"""
def display_amplitude(data):
    print(audioop.max(data, 2))


"""



"""
def write_to_wav_file(p, frames):
    wf = wave.open(_FILENAME, 'wb')
    wf.setnchannels(_CHANNELS)
    wf.setsampwidth(p.get_sample_size(_SAMPLE_FORMAT))
    wf.setframerate(_FS)
    wf.writeframes(b''.join(frames))
    wf.close()



if __name__ == "__main__":
    clapper()