import math


def get_div_mod(a, b):
    """
    a = bq + r = b * floor(a/b) + r
    r = a mod b
    """
    div = math.floor(a / b)
    mod = a - b * div
    return div, mod


# 모듈로 거듭제곱법: base^exp mod m 을 계산하는 알고리즘, 내장함수 pow(base, exp, mod)와 같음
def modular_exponentiation(base: int, exp: int, mod: int):
    assert mod > 0
    x = 1
    power = base % mod
    k = format(exp, "b")[::-1]

    for i in k:
        if int(i) == 1:
            x = (x * power) % mod
        power = (power * power) % mod

    return x


print(modular_exponentiation(3, 644, 645))  # 36
