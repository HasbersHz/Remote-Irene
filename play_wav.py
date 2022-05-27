import os

from audioplayer import AudioPlayer
from saywav import saywav

def play_wav(wavfile):
    AudioPlayer(wavfile).play(block=True)
