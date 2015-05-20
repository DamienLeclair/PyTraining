__author__ = 'dleclair'

import os

# change current directory
#os.chdir("dir/subdir")

# open file and read
my_file = open("file.txt", "r")
print(type(my_file))
content = my_file.read()
print(content)
my_file.close()

# write in a file
my_file = open("file.txt", "w")
my_file.write("hello world")
my_file.close()

# using block
with open("file.txt", "r") as my_file:
    print("Is my_file closed = {}".format(my_file.closed))

print("Is my_file closed = {}".format(my_file.closed))