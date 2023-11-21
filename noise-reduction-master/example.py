# !/usr/bin/env python3
import noisereduction as nr
import os
full_path = os.path.realpath(__file__)
path, filename =os.path.split(full_path)
os.chdir(path)

WAV_FILE = os.getcwd() + '/example/noisefunkguitare'


noise_begin, noise_end = 0, 1

noised_audio = nr.Wiener(WAV_FILE, noise_begin, noise_end)
noised_audio.wiener()
noised_audio.wiener_two_step()
