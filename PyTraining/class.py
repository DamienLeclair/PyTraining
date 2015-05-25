__author__ = 'dleclair'


# ----------------------
# Properties definition
# ----------------------

class Character:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = 30
        self.birth_city = "Paris"


me = Character("Damien", "Leclair")

print(me.last_name)


class Counter:
    object_count = 0  # class attribute

    def __init__(self):
        Counter.object_count += 1


print(Counter.object_count)
a = Counter()
print(a.object_count)
b = Counter()
print(a.object_count)

# ------------------
# Methods definition
# ------------------


class BlackBoard:
    def __init__(self):
        self.content = ""

    def write(self, message):
        if message != "":
            self.content += (message + "\n")

    def read(self):
        print(self.content)

    def clean(self):
        self.content = ""


my_board = BlackBoard()
print(my_board.content)
my_board.write("Hello World")
my_board.read()
my_board.clean()
my_board.read()

# ------------
# Class method
# ------------


class Counter2:
    object_count = 0

    def __init__(self):
        Counter2.object_count += 1

    def how_many(cls):
        print("{} objects created".format(cls.object_count))

    how_many = classmethod(how_many)


print(Counter2.how_many())
c = Counter2()
print(Counter2.how_many())
d = Counter2()
print(Counter2.how_many())


# -------------
# Static method
# -------------

class Test:
    def display():
        print("Display something")

    display = staticmethod(display)


# -------------
# Introspection
# -------------

class Test2:
    def __init__(self):
        self.my_attribute = "ok"

    def display(self):
        print("my attibute is {}".format(self.my_attribute))


my_test2 = Test2()
my_test2.display()
print(dir(my_test2))
my_test2.__dict__["my_attribute"] = "nok"  # this is the dictionary of class attributes
my_test2.display()
