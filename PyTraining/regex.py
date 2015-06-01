__author__ = 'dleclair'

import re

print(re.search(r"abc", "abcdef"))

if re.match(r"abc*", "abcc") is not None:
    print("Match succeded")

phone_regex = r"^0[0-9]([ .-][0-9]{2}){4}$"
print(re.match(phone_regex, "06.07.08.09.10"))

# -----------------
# group replacement
# -----------------

print(
    re.sub(r"(ab)", r" \1 ", "abcdef")
)

# ------------
# named groups
# ------------

text = """
    name='Task1', id=8
    name='Task2', id=31
    name='Task3', id=127
"""

regex = r"id=(?P<id>[0-9]+)"
replace = r"id[\g<id>]"

print(re.sub(regex, replace, text))

# --------------------
# compiled expressions
# --------------------



