import time
import random
import os


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
        pass
        #if not self.playing:


def get_music():
    directory = "C://Users/gb_mo/Documents/Work/Coding/Haroldv4/songs"
    return random.choice(os.listdir(directory))


def main():
    print(weekday())
    h = Harold()
    print(h.music)


if __name__ == "__main__":
    main()
