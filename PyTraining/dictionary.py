__author__ = 'dleclair'

my_dictionary = dict()
print(type(my_dictionary))

my_dictionary = {}
my_dictionary["user"] = "dleclair"
my_dictionary["password"] = "secret"
print(my_dictionary)

echiquier = {}
echiquier['a', 1] = "tour blanche"  # En bas à gauche de l'échiquier
echiquier['b', 1] = "cavalier blanc"  # À droite de la tour
echiquier['c', 1] = "fou blanc"  # À droite du cavalier
echiquier['d', 1] = "reine blanche"  # À droite du fou
# ... Première ligne des blancs
echiquier['a', 2] = "pion blanc"  # Devant la tour
echiquier['b', 2] = "pion blanc"  # Devant le cavalier, à droite du pion

placard = {"chemise": 3, "pantalon": 6, "tee-shirt": 7}

my_set = {"user", "password"}  # this is not a dictionary but a set
print(type(my_set))

placard = {"chemise": 3, "pantalon": 6, "tee shirt": 7}
del placard["chemise"]

# function pointer
print_2 = print
print_2("print message")


def error():
    print("Error")


def warning():
    print("warning")


log = {
    "error": error,
    "warning": warning
}

log["error"]()

for key in my_dictionary.keys():
    print(key)

for value in my_dictionary.values():
    print(value)

for key, value in my_dictionary.items():
    print("key = {}, value = {}".format(key, value))

# Named parameters
def n_parameters_func(**parameters):
    print("parameters : {}".format(parameters))

n_parameters_func(a=1, b=2)