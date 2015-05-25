__author__ = 'dleclair'

# --------------------------
# Catching exceptions sample
# --------------------------
try:
    value = input("Enter an integer : ");
    integer = int(value)
    print(value, "is an integer")

# Catch only ValueError
except ValueError:
    print(value, "is not an integer")

# Add a variable on ValueError exception
except ValueError as ex:
    print(ex)

# pass is used to keep empty an exception or function
# it's not recommended to use it
except ValueError as ex:
    pass

# Catch all exceptions
except:
    print(value, "is not an integer")

# Do the job if no error occurred
# it's not recommended to use it
else:
    print(value, "is an integer")

# classical finally block
finally:
    print("End of try block")

# ------------------
# Assertion sample
# ------------------
try:
    value = input("Enter a positive integer : ")
    integer = int(value)
    assert integer >= 0
    print(value, " is a positive integer")
except ValueError:
    print(value, "is not an integer")
except AssertionError:
    print(value, "is not positive")


# ------------------
# Raise an exception
# ------------------
try:
    value = input("Enter a positive integer : ")
    integer = int(value)
    if integer < 0:
        raise ValueError("{0} is not a positive integer".format(integer))
    print(value, " is a positive integer")
except ValueError as ex:
    print(ex)
except AssertionError:
    print(value, "is not positive")