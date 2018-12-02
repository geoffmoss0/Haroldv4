import time
import random
import os
from pygame import mixer
import vlc


def weekday() -> bool:
    """
    :return: whether or not it is a weekday
    """
    return time.localtime(time.time())[6] < 5


class Harold:
    def __init__(self):
        self.playing = False
        self.music = get_music()

    def run(self):
        if not self.playing:
            pass
            mixer.init()
            mixer.music.load(self.music)
            mixer.music.play()


def get_music():
    directory = "C://Users/gb_mo/Documents/Work/Coding/Haroldv4/songs"
    return os.path.join(directory, random.choice(os.listdir(directory)))
