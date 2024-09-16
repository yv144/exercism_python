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

tolerance = {
    'Grey' : "0.05%",
    'Violet' : "0.1%",
    'Blue' : "0.25%",
    'Green' : "0.5%",
    'Brown' : "1%",
    'Red' : "2%",
    'Gold' : "5%",
    'Silver' : "10%"
}

prefix = {
    1e0: "",
    1e3: "kilo",
    1e6: "mega",
    1e9: "giga"
}

def value(colors:list) -> int:
    data = colors[:2]
    return int(str(clrs[data[0]])+str(clrs[data[1]]))

def label(colors:list,correction=None) -> str:
    power = clrs[colors[2]]
    val = value(colors) if correction==None else int(str(value(colors)) + str(correction))
    total = val*pow(10,power)
    
    numerical,pr = 0,""
    for trehshold,name in prefix.items():
        if total >= trehshold:
            numerical = total / trehshold
            pr  = name 

    if round(numerical) == round(numerical,1):
        return f"{int(numerical)} {pr}ohms"
    else:
        return f"{numerical} {pr}ohms"

def resistor_label(data: list) -> str:
    if len (data) == 1:
        return label(['black',data[0],'black'])
    precision = tolerance[data[-1].capitalize()]
    if len (data) == 4:
        return f"{label(data)} ±{precision}"
    if len (data) == 5:
        correction_needed = clrs[data[2]]
        data.pop(2)
        return f"{label(data,correction=correction_needed)} ±{precision}"
