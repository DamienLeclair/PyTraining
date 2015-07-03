__author__ = 'dleclair'

import os
import pickle

# change current directory
#os.chdir("dir/subdir")

# ------------------
# open file and read
# ------------------
my_file = open("file.txt", 'r')
print(type(my_file))
content = my_file.read()
print(content)
my_file.close()

# ---------------
# write in a file
# ---------------
my_file = open("Temp/file.txt", 'w')
my_file.write("hello world")
my_file.close()

# -----------
# using block
# -----------
with open("Temp/file.txt", 'r') as my_file:
    print("Is my_file closed = {}".format(my_file.closed))

print("Is my_file closed = {}".format(my_file.closed))

user = {
    "first_name": "Damien",
    "last_name": "Leclair"
}

with open("Temp/data", 'wb') as file:
    my_pickler = pickle.Pickler(file)
    my_pickler.dump(user)

with open("Temp/data", 'wb') as file:
    my_unpickler = pickle.Unpickler(file)
    user_data = my_unpickler.load()
    print(user_data)

# The argument mode points to a string beginning with one of the following
# sequences (Additional characters may follow these sequences.):
#
#  ``r''   Open text file for reading.  The stream is positioned at the
#          beginning of the file.
#
#  ``r+''  Open for reading and writing.  The stream is positioned at the
#          beginning of the file.
#
#  ``w''   Truncate file to zero length or create text file for writing.
#          The stream is positioned at the beginning of the file.
#
#  ``w+''  Open for reading and writing.  The file is created if it does not
#          exist, otherwise it is truncated.  The stream is positioned at
#          the beginning of the file.
#
#  ``a''   Open for writing.  The file is created if it does not exist.  The
#          stream is positioned at the end of the file.  Subsequent writes
#          to the file will always end up at the then current end of file,
#          irrespective of any intervening fseek(3) or similar.
#
#  ``a+''  Open for reading and writing.  The file is created if it does not
#          exist.  The stream is positioned at the end of the file.  Subse-
#          quent writes to the file will always end up at the then current
#          end of file, irrespective of any intervening fseek(3) or similar.

