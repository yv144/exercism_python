# Compute the prime factors of a given natural number.

def factors(start_value: int) -> list[int]:
    
    output = []
    while start_value >1:
        for number in range(2,start_value+1):
            if start_value % number == 0:
                start_value = start_value // number
                output.append(number)
                break
    return output
