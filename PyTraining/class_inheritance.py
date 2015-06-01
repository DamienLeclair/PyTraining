__author__ = 'dleclair'

# ------------------
# Simple inheritance
# ------------------


class A:
    pass  # used to bypass the implementation


class B(A):
    pass


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return "{} {}".format(
            self.first_name, self.last_name
        )


class SpecialAgent(Person):
    def __init__(self, first_name, last_name, regimental):
        Person.__init__(self, first_name, last_name)
        self.regimental = regimental

    def __repr__(self):
        return "Agent {}, Regimental {}".format(self.first_name, self.regimental)


# --------------
# Useful methods
# --------------

print(issubclass(SpecialAgent, Person))
print(issubclass(SpecialAgent, object))
print(issubclass(Person, object))
print(issubclass(Person, SpecialAgent))

agent = SpecialAgent("Damien", "Leclair", "007")
print(isinstance(agent, SpecialAgent))
print(isinstance(agent, Person))

# --------------------
# Multiple inheritance
# --------------------


class C(A, B):
    pass