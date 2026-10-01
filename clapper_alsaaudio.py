#!/usr/bin/python
## This is an example of a simple sound capture script.
##
## The script opens an ALSA pcm for sound capture. Set
## various attributes of the capture, and reads in a loop,
## Then prints the volume.
##
## To test it out, run it and shout at your microphone:

import alsaaudio, time, audioop

def clapper():
    # Open the device in nonblocking capture mode. The last argument (alsaaudio.PCM_NONBLOCK) could
    # just as well have been zero for blocking mode. Then we could have
    # left out the sleep call in the bottom of the loop

    # Set attributes: Mono, 8000 Hz, 16 bit little endian samples
    # inp.setchannels(1)
    # inp.setrate(8000)
    # inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)

    # The period size controls the internal number of frames per period.
    # The significance of this parameter is documented in the ALSA api.
    # For our purposes, it is suficcient to know that reads from the device
    # will return this many frames. Each frame being 2 bytes long.
    # This means that the reads below will return either 320 bytes of data
    # or 0 bytes of data. The latter is possible because we are in nonblocking
    # mode.
    # inp.setperiodsize(160)

    inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK, channels=1, rate=8000, format=alsaaudio.PCM_FORMAT_S16_LE, periodsize=160)

    timer = 0
    timer_max_threshold = 0.002
    timer_min_threshold = 0.000
    could_be_clap = False
    really_could_be_clap = False

    while True:

        # Read data from device
        l,data = inp.read()
        
        if l and audioop.max(data, 2) > 32767:
            timer += 0.001
            # Print the maximum of the absolute value of all samples in a fragment.
            print(audioop.max(data, 2))
        elif l and not really_could_be_clap and could_be_clap:
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

if __name__ == "__main__":
    clapper()
