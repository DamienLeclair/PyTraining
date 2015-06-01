__author__ = 'dleclair'

class MyException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


raise MyException("Every things is broken")