def zero_safe(sides:list)->bool:
    a,b,c = sides
    return a!=0 and b!=0 and c!=0

def len_safe(sides:list)->bool:
    a,b,c = sides
    return a+b>=c and b+c>=a and a+c>=b

def equilateral(sides:list)->bool:
    a,b,c = sides
    return zero_safe(sides) and len_safe(sides) and (a==b==c)
        
def isosceles(sides:list)->bool:
    a,b,c = sides
    return zero_safe(sides) and len_safe(sides) and (a==b or b==c or a==c)

def scalene(sides:list)->bool:
    a,b,c = sides
    return zero_safe(sides) and len_safe(sides) and a!=b and b!=c and a!=c
