import os

from audioplayer import AudioPlayer
from save_wav import saywav_to_file

def play_wav(wavfile):
    AudioPlayer(wavfile).play(block=True)
