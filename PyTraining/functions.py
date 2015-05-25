__author__ = 'dleclair'

# -----------------------------
# Classical function definition
# -----------------------------

def print_table(nb, max=10):
    """Here is the doc of the function
    Here is the seconde line of the doc"""
    i = 0
    while i < max:
        print(i + 1, " x ", nb, " = ", (i + 1) * nb)
        i += 1

def square(value):
    return value * value

print_table(2)
print_table(3, 5)
help(print_table)

print(square(3))

# --------------------------
# Lambda function definition
# --------------------------

square_lambda = lambda x : x * x

print("square_lambda(3) = ", square_lambda(3))

# Using modules

import math
print("math.sqrt(9) = ",math.sqrt(9))

import math as mathematic
print("mathematic.sqrt(9) = ",mathematic.sqrt(9))

from math import *
print("sqrt(9) = ",sqrt(9))
