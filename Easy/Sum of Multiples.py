# Given a number, find the sum of all the multiples of 
# particular numbers up to but not including that number.

def sum_of_multiples(limit, multiples):
    output = set()
    for num in range (limit):
        for divisor in multiples:
            if divisor!= 0 and num % divisor == 0:
                output |= set([num])
    return sum(output)
