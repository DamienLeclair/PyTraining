__author__ = 'dleclair'

# list instanciation
list1 = list()
print(type(list1))

list2 = []
print(type(list2))

int_list = [1, 2, 3, 4]
print(int_list)

object_list = [1, 3.5, "string", []]  # we can store different types of objects in a list
print(object_list[1])

int_list.append(56)
int_list.insert(2, 0)
print(int_list)

# concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1 += list2
print(list1)

# del key word
var = 1
print(var)
del var
# print(var)

list1 = [1, 2, 3]
del list1[1]  # take the index
print(list1)

list1 = [1, 2, 3]
list1.remove(3)  # take the element
print(list1)

# list enumeration
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i, elt in enumerate(list1):
    print("Index {0} : value {1}".format(i, elt))

for elt in enumerate(list1):
    print(elt)

list2 = [
    [1, 'a'],
    [4, 'd'],
    [7, 'g'],
    [26, 'z']
]  # list of tuples

for nb, char in list2:
    print("[{};{}]".format(nb, char))

# tuple introduction
empty_tuple = ()
empty_tuple = (1,)
empty_tuple = (1, 2,)


def integer_division(a, b):
    i_p = a // b
    modulo = a % b
    return i_p, modulo

i_p, modulo = integer_division(3, 2)
print("[{},{}]".format(i_p, modulo))

