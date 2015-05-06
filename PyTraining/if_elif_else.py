__author__ = 'dleclair'

import os

value = input("Enter a number : ")
number = int(value)

print(type(value))
print(type(number))

if number > 0:
    print("{} is positive".format(number))
elif number < 0:
    print("{} is negative".format(number))
elif 1 > value > -1 and type(value) is int:
    number("{} is null".format(number))
# else:
#     print("{} is null".format(value))

print("4 % 3 = {}".format(4 % 3))
os.system("pause")
