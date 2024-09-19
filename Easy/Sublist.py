# Determine if a list in a sublist of another list


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


def check(A,B,shift=0) -> list[bool]:
    _test = []
    for index, element in enumerate(A):
        _test.append(element == B[index+shift])
    return _test

def sublist(A: list[int], B: list[int]) -> int:
    if len(A) == len(B):
        if len(A) ==0:
            return EQUAL
        else:
            return EQUAL if all(check(A,B)) else UNEQUAL

    elif len(A)!=len(B):
        if len(A) ==0:
            return SUBLIST
        
        if len(A)<len(B):
            lst1 = A
            lst2 = B
            mode = "normal"
        else:
            lst1 = B
            lst2 = A
            mode = "reversed"


        for shift in range(len(lst2)-len(lst1)+1):
            states = check(lst1,lst2,shift)
            if all(states):
                if mode == "normal":
                    return SUBLIST
                else:
                    return SUPERLIST
        return UNEQUAL

# x = sublist([1, 2, 3],[2, 3])
# print(x)
