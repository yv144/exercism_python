# Determine whether a given year is a leap year.

def leap_year(year) -> bool:
    return year % 400 ==0 or year % 4 ==0 and not year %100==0