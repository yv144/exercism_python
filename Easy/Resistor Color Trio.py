# Convert color codes, as used on resistors, to a human-readable label.

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

prefix = {
    1e0: "",
    1e3: "kilo",
    1e6: "mega",
    1e9: "giga"
}

def value(colors):
    data = colors[:2]
    return int(str(clrs[data[0]])+str(clrs[data[1]]))

def label(colors):
    power = clrs[colors[2]]
    val = value(colors)
    total = val*pow(10,power)
    
    numerical,pr = 0,""
    for trehshold,name in prefix.items():
        if total >= trehshold:
            numerical = total / trehshold
            pr  = name 
    return f"{int(numerical)} {pr}ohms"
