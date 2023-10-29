"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def list_in_list(list_one, list_two):
    if len(list_two) < len(list_one):
        return False
    length_one = len(list_one)
    diff = len(list_two) - len(list_one)
    for i in range(diff + 1):
        compare_list = list_two[i:i + length_one]
        if list_one == compare_list:
            return True

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if list_in_list(list_one, list_two) or list_one == []:
        return SUBLIST
    if list_in_list(list_two, list_one) or list_two == []:
        return SUPERLIST
    return UNEQUAL
