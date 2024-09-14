# Determine if a number is an Armstrong number.

def is_armstrong_number(number:int)->bool:
    digits = list(str(number))
    total = 0
    for digit in digits:
        total += int(digit)**len(digits)
    return total == number
