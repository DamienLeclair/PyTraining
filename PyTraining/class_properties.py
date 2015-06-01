__author__ = 'dleclair'


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = 30
        self._birth_city = "Paris"

    def _get_birth_city(self):
        return self._birth_city

    def _set_birth_city(self, value):
        self._birth_city = value

    birth_city = property(_get_birth_city, _set_birth_city)

me = Person("Damien", "Leclair")
print(me.birth_city)
me.birth_city = "Evry"
print(me.birth_city)