__author__ = 'dleclair'

# ----------------------
# Sort simple collection
# ----------------------

names = ["Jacques", "Laure", "André", "Victoire", "Albert", "Sophie"]
names.sort()  # sort method modify directly the list instance
print(names)

names = ["Jacques", "Laure", "André", "Victoire", "Albert", "Sophie"]
sorted_names = sorted(names)  # sorted method create a new instance of the sorted list
print(names)
print(sorted_names)

print(sorted([1, 8, -2, 15, 9]))
print(sorted(["1", "8", "-2", "15", "9"]))

# ------------
# Sort a tuple
# ------------

students = [
    ("Clément", 14, 16),
    ("Charles", 12, 15),
    ("Oriane", 14, 18),
    ("Thomas", 11, 12),
    ("Damien", 12, 15),
]

print(sorted(students))
print(sorted(students, key=lambda column: column[2]))

# ----------------------------
# Sort a collection of objects
# ----------------------------


class Student:
    def __init__(self, name, age, average):
        self.name = name
        self.age = age
        self.average = average

    def __repr__(self):
        return "<Student {} (age={}, average={}>".format(self.name, self.age, self.average)


students = [
    Student("Clément", 14, 16),
    Student("Charles", 12, 15),
    Student("Oriane", 14, 18),
    Student("Thomas", 11, 12),
    Student("Damien", 12, 15),
]

print(sorted(students, key=lambda s: s.average))
print(sorted(students, key=lambda s: s.average, reverse=True))

# ---------
# operator library
# ---------

students = [
    ("Clément", 14, 16),
    ("Charles", 12, 15),
    ("Oriane", 14, 18),
    ("Thomas", 11, 12),
    ("Damien", 12, 15),
]

from operator import itemgetter

print(sorted(students, key=itemgetter(2)))

students = [
    Student("Clément", 14, 16),
    Student("Charles", 12, 15),
    Student("Oriane", 14, 18),
    Student("Thomas", 11, 12),
    Student("Damien", 12, 15),
]

from operator import attrgetter

print(sorted(students, key=attrgetter("average")))  # sort on one criteria
print(sorted(students, key=attrgetter("average", "age")))  # sort on two criteria

# -------------
# Sort chaining
# -------------


class InventoryRow:

    def __init__(self, product, price, quantity):
        self.product = product
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return "<Inventory row {} ({}x{})>".format(
            self.product, self.quantity, self.price
        )


inventory = [
    InventoryRow("red apple", 1.2, 19),
    InventoryRow("orange", 1.4, 24),
    InventoryRow("red banana", 0.9, 21),
    InventoryRow("pear", 1.2, 24)
]

# sort on quantity and price
inventory.sort(key=attrgetter("quantity"), reverse=True)
print(sorted(inventory, key=attrgetter("price")))