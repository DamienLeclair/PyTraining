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

