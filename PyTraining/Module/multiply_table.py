__author__ = 'dleclair'
"""module multiply_table"""

import os

def table(nb, max=10):
    """Print the multiply table"""
    i = 0
    while i < max:
        print(i + 1, " x ", nb, " = ", (i + 1) * nb)
        i += 1

# table(nb, max=10) test
if __name__ == "__main__":
    table(2)
    os.system("pause")