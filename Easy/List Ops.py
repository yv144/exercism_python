# Implement basic list operations.

def append(list1, list2):
    return list1 + list2

def concat(lists):
    base = []
    for item in lists:
        base += item
    return base

def filter(function, list):
    base = []
    for item in list:
        if function(item):
            base += item
    return base

x = filter(lambda x: x % 2 == 1, [1, 2, 3, 5])

def length(list):
    pass


def map(function, list):
    pass


def foldl(function, list, initial):
    pass


def foldr(function, list, initial):
    pass


def reverse(list):
    pass
