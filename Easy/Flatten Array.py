# Take a nested list adn return a single list with all values except nil/null.

def flatten(iterable:list[int|None|list]) -> list:
    output = []
    for step in iterable:
        if type(step) == int:
            output.append(step)
        if type(step) == list:
            output.extend(flatten(step))
    return output
