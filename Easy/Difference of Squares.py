# Find the difference between the square of the sum and 
# the sum of the squares of the first N nautral numers

def square_of_sum(number: int) -> int:
    total = 0
    for number in range(1,number+1):
        total += number
    return total**2

def sum_of_squares(number: int) -> int:
    total = 0
    for number in range (1,number+1):
        total += number**2
    return total

def difference_of_squares(number: int) -> int:
    return square_of_sum(number) - sum_of_squares(number)
