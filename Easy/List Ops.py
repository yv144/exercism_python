# Implement basic list operations.

def append(list1, list2) -> list:
    return list1 + list2

def concat(lists) -> list:
    base = []
    for item in lists:
        base += item
    return base

def filter(function, list) -> list:
    base = []
    for item in list:
        if function(item): 
            base += [item]
    return base

def length(list) -> int:
    count  = 0
    for _ in list:
        count += 1
    return count

def map(function, list) -> list:
    return [function(item) for item in list]
        
def foldl(function, list, initial) -> float|int:
    for item in list:
        initial = function(initial,item)
    return initial

def foldr(function, list, initial) -> float|int:
    for item in list[::-1]:
        initial = function(initial,item)
    return initial

def reverse(list) -> list:
    return list[::-1]