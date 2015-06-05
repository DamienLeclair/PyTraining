__author__ = 'dleclair'

# ----
# math
# ----

import math

print(math.pow(5, 2))
print(math.ceil(2.3))
print(math.floor(5.8))
print(math.trunc(9.5))

# ---------
# fractions
# ---------

from fractions import Fraction

print(Fraction(1, 2))
print(Fraction("1/4"))
print(Fraction(-5, 30))
print(Fraction.from_float(0.5))

frac = Fraction(1, 10)
print(frac + frac + frac)

# ------
# random
# ------

import random

print(random.random())

print(random.randrange(5, 10, 2))
print(random.randint(1, 6))

list = ['a', 'b', 'k', 'p', 'i', 'w', 'z']
print(random.choice(list))

random.shuffle(list)
print (list)