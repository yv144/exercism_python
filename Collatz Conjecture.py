# Calculate the number of steps to reach 1 using the Collatz conjecture.

def steps(number:int)->int:
    if number <=0 or type(number) != int:
        raise ValueError("Only positive integers are allowed")
    
    steps_count = 0 

    while number != 1:
        if number%2 == 0:
            number = number/2
            steps_count +=1
            continue
        elif number%2 ==1:
            number = number*3+1
            steps_count +=1
            continue
 
    return steps_count
 