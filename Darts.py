# Calculate the points scored in a single toss of a Darts game.

def score(x: float, y: float) -> int:
    r = (x**2+y**2)**0.5
    if r<=1:
        sc = 10
    if r > 1:
        sc = 5
    if r > 5:
        sc = 1
    if r > 10:
        sc = 0
    return sc 
