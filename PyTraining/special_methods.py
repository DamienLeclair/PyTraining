__author__ = 'dleclair'

# ----------------------------------------------------
# Special methods for editing and accessing the object
# ----------------------------------------------------


class Character:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # destructor
    # def __del__(self):
    #     print("this object has been deleted")

    # to represent the object instance
    def __repr__(self):
        return "first_name = {}, last_name = {}".format(self.first_name, self.last_name)

    # like ToString in CSharp
    # if __str__ is not defined, python call __repr__
    def __str__(self):
        return "I'm {} {}".format(self.first_name, self.last_name)

    # if the attribute called doesn't exist, this method is called instead
    def __getattr__(self, item):
        print("Attribute {} doesn't exist".format(item))

    # this method is called when the user modify an attribute value
    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)  # call the base class
        print("{} attribute changed".format(key))

    def __delattr__(self, item):
        raise AttributeError("Impossible to delete an attribute from a class")


me = Character("Damien", "Leclair")
print(me)

str_me = str(me)
print(str_me)

print(me.size)

me.first_name = "Dam"

# -----
# bonus
# -----
# print(getattr(me, "first_name"))
# setattr(me, "first_name", "Damien")
# print(getattr(me, "first_name"))
# delattr(me, "first_name")
# print(hasattr(me, "last_name"))

# -----------------
# Methods container
# -----------------


class ZDict:
    def __init__(self):
        self._dictionary = {}

    def __getitem__(self, index):
        return self._dictionary[index]

    def __setitem__(self, index, value):
        self._dictionary[index] = value

    def __delitem__(self, index):
        del self._dictionary[index]

    # def __contains__(self, item):

    def __len__(self):
        return self._dictionary.__len__()


class TimeSpan:
    def __init__(self, min=0, sec=0):
        self.min = min
        self.sec = sec

    def __str__(self):
        return "{0:02}:{1:02}".format(self.min, self.sec)

    def __add__(self, other):
        result = TimeSpan(self.min, self.sec)
        result.sec += other

        if result.sec >= 60:
            result.min += result.sec // 60
            result.sec %= 60

        return result

    # def __sub__(self, other):
    # ...

    # called when writing 4 + TimeSpan instead of TimeSpan + 4
    # redirect add
    def __radd__(self, other):
        return self + other

    # incrementation add
    def __iadd__(self, other):
        self.sec += other

        if self.sec >= 60:
            self.min += self.sec // 60
            self.sec %= 60

        return self

    # == operator
    def __eq__(self, other):
        return self.sec == other.sec and self.min == other.min

    # >
    def __gt__(self, other):
        self_sec = self.sec + self.min * 60
        other_sec = other.sec + other.min * 60

        return self_sec > other_sec


t1 = TimeSpan(3, 5)
print(t1)
print(t1 + 30)
print(30 + t1)
t1 += 20
print(t1)


# Useful methods for pickle
