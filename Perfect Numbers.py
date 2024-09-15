# Determine if a number is perfect, abundant, or deficient 
# based on Nicomachus' (60 - 120 CE) classification scheme for positive integers.

def classify(number:int) -> str:
    if type(number) != int or number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    divisors_sum = 0
    for x in range(1,number):
        if number % x == 0:
            divisors_sum += x
    if divisors_sum == number:
        output = "perfect"
    elif divisors_sum >= number:
        output =  "abundant"
    else:
        output = "deficient"
    return output 
