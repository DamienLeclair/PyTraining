__author__ = 'dleclair'

import random
import sys
import time

# --------------------
# un-threaded approach
# --------------------

# i = 0
# while i < 20:
#     sys.stdout.write("1")
#     sys.stdout.flush()
#     wait = 0.2
#     wait += random.randint(1, 60) / 100
#     time.sleep(wait)
#     i += 1


# -----------------
# Thread approach
# -----------------

from threading import Thread, RLock

class CharDisplayer(Thread):

    def __init__(self, char):
        Thread.__init__(self)
        self.char = char

    def run(self):
        i = 0
        while i < 20:
            sys.stdout.write(self.char)
            sys.stdout.flush()
            wait = 0.2
            wait += random.randint(1, 60) / 100
            time.sleep(wait)
            i += 1


# thread_1 = CharDisplayer("1")
# thread_2 = CharDisplayer("2")

# thread_1.start()
# thread_2.start()
#
# thread_1.join()
# thread_2.join()


# ----------------------
# Thread synchronisation
# ----------------------

lock = RLock()

class WordDisplayer(Thread):

    def __init__(self, word):
        Thread.__init__(self)
        self.word = word

    def run(self):
        i = 0
        while i < 20:
            with lock:
                for char in self.word:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    wait = 0.2
                    wait += random.randint(1, 60) / 100
                    time.sleep(wait)
            i += 1

thread_1 = WordDisplayer("duck")
thread_2 = WordDisplayer("TURTLE")

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()