__author__ = 'dleclair'


class Person():

    def __new__(cls, first_name, last_name, age, city):
        print("__new__ method has been called for class {}".format(cls))
        return object.__new__(cls, first_name, last_name, age, city)

    def __init__(self, first_name, last_name, age, city):
        print("__init__ method has been called")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city


person = Person("John", "Doe", 23, "NY")

