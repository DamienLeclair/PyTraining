__author__ = 'dleclair'

# -----------
# upper lower
# -----------
print("LOWER".lower())
print("upper".upper())

# -----------------
# str instanciation
# -----------------
string = str()

# ----------
# str format
# ----------
print("Hello I'm {0}".format("Damien"))
print("My last name is {last_name}".format(last_name="Leclair"))
age = 29
print("I'm " + str(age) + " years old")

# ----------------------
# getting chars of a str
# ----------------------
hello = "Hello World"
i = 0
while i < len(hello):
    print(hello[i])
    i += 1

print(hello[0:2])
print(hello[2:len(hello)])
print(hello[:2])
print(hello[2:])
