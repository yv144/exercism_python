# Given a number from 0 to 999,999,999,999, spell out that number in English

d0_9 = {
    0:"zero",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine"
}
d10_19 = {
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"ninteen"
}
d20_90 = {
    20:"twenty",
    30:"thirty",
    40:"forty",
    50:"fifty",
    60:"sixty",
    70:"seventy",
    80:"eighty",
    90:"ninety"
}

def two_digits(number:int,print_zero:bool = True) -> str:
    if print_zero == False and number == 0:
        return ""
    output = []
    if number in d0_9.keys():
        output.append(d0_9[number])
    elif number in d10_19.keys():
        output.append(d10_19[number])
    elif number in d20_90.keys():
        output.append(d20_90[number])
    elif number <= 99:
        n1 = number //10
        n2 = number % 10
        w1 = d20_90[n1*10]
        w2 = d0_9[n2]
        output.append(w1+"-"+w2)
    return "".join(output)

def three_digits(number: int) -> str:
    # less than 100
    if number <= 99:
        return two_digits(number)
    else:
        n0 = number //100
        w0 = d0_9[n0]+" hundred " 
        return w0 + two_digits(number%100,print_zero=False)


def split(number:int) -> dict[str:int]:
    billions   = number // 1e9
    number    -= billions * 1e9

    millions   = number // 1e6
    number    -= millions * 1e6

    thousands  = number // 1e3
    number -= thousands * 1e3

    units = number 

    output = {
        "billions": int(billions),
        "millions": int(millions),
        "thousands": int(thousands),
        "units": int(units)
    }
    return output

def say(number: int) -> str:
    # exception handling
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"
    
    output = ""
    for index,value in split(number).items():
        if value != 0:
            output += three_digits(value) +" " +index.removesuffix("s") + " "
    return output.strip().removesuffix(" unit").strip()
