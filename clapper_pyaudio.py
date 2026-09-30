#!/usr/bin/python

import time
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

    timer = 0
    timer_max_threshold = 0.002
    timer_min_threshold = 0.000
    clap_amp_threshold = 32600
    could_be_clap = False
    really_could_be_clap = False
    while True:
    
        # TODO:just have it sleep more instead of all of this weird timer stuff
        # you don't need to be sampling when your waiting
        # TODO: maybe do something with the average where 
        # if the average is high then it is probably not a clap
        # because it is sustained...
    
        # Read data from device
        data = s.read(_CHUNK)
        if audioop.max(data, 2) > clap_amp_threshold:
            timer += 0.001
            # Print the maximum of the absolute value of all samples in a fragment.
            display_amplitude(data)
        elif not really_could_be_clap and could_be_clap:
            really_could_be_clap = True
                
        if timer > 0 and not could_be_clap:
            could_be_clap = True
    
        # maybe add sustain flag meaning it wont read claps for a bit of
        if timer > timer_max_threshold:
            could_be_clap = False
            timer = 0
            print("entered")
    
                
        if timer_max_threshold > timer > timer_min_threshold and really_could_be_clap and could_be_clap:
            print("clap")
            could_be_clap = False
            really_could_be_clap = False
            timer = 0
                

        time.sleep(.001)


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