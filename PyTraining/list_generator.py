__author__ = 'dleclair'


def my_gen():
    yield 1
    yield 2
    yield 3


for val in my_gen():
    print(val)


def interval(inf, sup):
    inf += 1
    while inf < sup:
        yield inf
        inf += 1


for val in interval(5, 10):
    print(val)

generator = interval(5, 20)
for val in generator:
    if val > 17:
        generator.close()  # loop interruption
    else:
        print(val)

# -------------------------------------
# send some value during the generation
# -------------------------------------


def interval_2(inf, sup):
    inf += 1
    while inf < sup:
        received_value = (yield inf)
        if received_value is not None:
            inf = received_value
        inf += 1


generator_2 = interval(10, 25)
for val in generator:
    if val == 15:
        generator.send(20)
    print(val)