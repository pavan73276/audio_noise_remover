import numpy as np
import soundfile as sf
import sounddevice as sd
import os
full_path = os.path.realpath(__file__)
path, filename =os.path.split(full_path)
os.chdir(path)

# Specify the path to your float-encoded audio file
file_path = os.getcwd() + '/example/noisefunkguitare_wiener.wav'

# Read the float-encoded audio file
data, sample_rate = sf.read(file_path, dtype='float32')

# Play the audio using sounddevice
sd.play(data, sample_rate)
sd.wait()
