import math


def get_div_mod(a, b):
    """
    a = bq + r = b * floor(a/b) + r
    r = a mod b
    """
    div = math.floor(a / b)
    mod = a - b * div
    return div, mod


# base^exp mod m 계산, 내장함수 pow(base, exp, mod)와 같음
def modular_exponentiation(base: int, exp: int, mod: int):
    assert mod > 0
    x = 1
    power = base % mod
    k = bin(exp)[2:]

    for i in k[::-1]:
        if int(i) == 1:
            x = (x * power) % mod
        power = (power * power) % mod

    return x


print(modular_exponentiation(3, 644, 645))  # 36
