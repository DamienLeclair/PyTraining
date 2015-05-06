__author__ = 'dleclair'
try:
    value = input("Enter an interger :");
    integer = int(value)
    # print(value, "is an integer")
# except:
#     print(value, "is not an integer")
# except ValueError:
#     print(value, "is not an integer")
except ValueError as ex:
    print(ex)
else:
    print(value, "is an integer")
finally:
    print("End of try block")