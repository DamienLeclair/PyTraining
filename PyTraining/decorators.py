__author__ = 'dleclair'

# ----------------
# Simple decorator
# ----------------


def my_decorator(function):
    print("my_decorator called")
    return function


@my_decorator
def my_function():
    print("my_func called")


my_function()


def obsolete(function):
    def to_obsolete():
        raise RuntimeError("Function {} is obsolete".format(function))
    return to_obsolete


# @obsolete
def my_function():
    pass

my_function()

# -------------------------
# Decorator with parameters
# -------------------------

import time_lib


def elapsed_time(sec_count):

    def decorator(function):

        def calculate_elapsed_time(*not_named_params, **named_params):
            start = time_lib.time()
            result = function(*not_named_params, **named_params)  # keep parameters of the called function
            stop = time_lib.time()
            elapsed = stop - start

            if elapsed > sec_count:
                print("Function {} takes more than {} sec to execute".format(
                    function, sec_count
                ))

            return result

        return calculate_elapsed_time
    return decorator


@elapsed_time(2.5)
@my_decorator  # It's possible to chain decorators
def wait():
    input("Press enter")


wait()

# --------------------
# Decorator on a class
# --------------------


def singleton(cls):
    instances = {}
    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return get_instance()


@singleton
class Test:
    pass

a = Test()
b = Test()

print(a is b)