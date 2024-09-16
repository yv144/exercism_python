# Convert color codes, as used on resistors, to a numeric value.

clrs = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}


def value(colors):
    data = colors[:2]
    return int(str(clrs[data[0]])+str(clrs[data[1]]))