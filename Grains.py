# Calculate the number of grains of wheat on a chessboard given that the number on each square doubles.

def square(number):
    if number > 64 or number <1:
        raise ValueError("square must be between 1 and 64")
    
    current = 0.5
    for square in range(number):
        current = current*2
    return int(current)

def total():
    cumulative = 0
    for value in range(1,65):
        cumulative += square(value)
    return cumulative

print(total())
# print(square(64))