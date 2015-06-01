__author__ = 'dleclair'

string = "test"
string_iterator = iter(string)
print(next(string_iterator))
print(next(string_iterator))


class RevStr(str):
    """ Reverse string
    """

    def __iter__(self):
        return ItRevStr(self)


class ItRevStr:
    """ Reverse string iterator
    """

    def __init__(self, string):
        self.string = string
        self.position = len(string)

    def __next__(self):

        if self.position == 0:
            raise StopIteration
        self.position -= 1
        return self.string[self.position]


string = RevStr("Hello")
for char in string:
    print(char)