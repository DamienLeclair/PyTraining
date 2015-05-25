__author__ = 'dleclair'

# ------------------
# list instanciation
# ------------------
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

# -------------
# concatenation
# -------------
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

# ------------
# del key word
# ------------
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

# ----------------
# list enumeration
# ----------------
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

# ------------------
# tuple introduction
# ------------------
empty_tuple = ()
empty_tuple = (1,)
empty_tuple = (1, 2,)


def integer_division(a, b):
    i_p = a // b
    modulo = a % b
    return i_p, modulo


i_p, modulo = integer_division(5, 3)
print("[{},{}]".format(i_p, modulo))

# --------------
# string to list
# --------------
string = "hello world and sunshine"
splitted_string = string.split(' ')
print(splitted_string)

# --------------
# list to string
# --------------
array = ['hello', 'world', 'and', 'sunshine']
joined_string = ' '.join(array)
print(joined_string)


def print_float(float_value, nb_decimal):

    if type(float_value) is not float:
        raise TypeError("float_value must be a type of float")
    if type(nb_decimal) is not int:
        raise TypeError("nb_decimal must be a type of int")

    str_value = str(float_value)
    entire_part, float_part = str_value.split('.')

    print(",".join([entire_part, float_part[:nb_decimal]]))

print_float(3.99999999999999, 2)


def n_parameters_func(*parameters):
    print("parameters : {}".format(parameters))

n_parameters_func('a', 'b', 'c', 'd')
abc_list = ['a', 'b', 'c']
n_parameters_func(*abc_list)

# list comprehensions
list1 = [0, 1, 2, 3, 4, 5]
list2 = [nb * nb for nb in list1]
print(list2)

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [nb for nb in list1 if nb % 2 == 0]
print(list2)