# Check if a given string is a valid ISBN-10 number.

import string

def is_valid(isbn:str) -> bool:

    isbn = [digit for digit in str(isbn).replace("-","")]
    
    if len(isbn)!=10:
        return False
    
    if isbn[-1] != "X" and isbn[-1] not in string.digits:
        return False

    for symbol in isbn[:-1]:
        if symbol not in string.digits:
            return False 

    isbn[-1] = 10 if isbn[-1] == "X" else isbn[-1]
    isbn = [int(digit) for digit in isbn]
    
    score = 0
    for position, value in enumerate(isbn):
        score += (10-position)*value
    return score%11==0
