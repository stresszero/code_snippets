import math

def max_decimal_digit_count(number):
    if number == 0:
        return 1
    return int(math.log10(abs(number))) + 1
