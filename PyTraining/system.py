__author__ = 'dleclair'

# -------------
# Standard flow
# -------------

import sys

print(sys.stdin)
print(sys.stdout)
print(sys.stderr)

sys.stdout.write("a test\n")

# file = open('Temp/output.txt', 'w')
# sys.stdout = file
# print("something")
# file.close()
# sys.stdout = sys.__stdout__

import os
print(os.getcwd())  # get the current working directory

# -------
# Signals (like messages in C#)
# -------

import signal

print("signal.SIGINT = {}".format(signal.SIGINT))

import sys

def close_program(signal, frame):
    print("closing program")
    sys.exit(0)


signal.signal(signal.SIGINT, close_program)  # connecting signal.SIGINT to close_program when it is received

# print("entering in infinite loop")
# while True:
#     continue

# --------------------------
# Retrieve console arguments
# --------------------------

print (sys.argv)


