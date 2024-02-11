import math


def fibonacci_formula(n):
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2
    return int((1 / sqrt_5) * (phi**n - psi**n))


n = 10
print(fibonacci_formula(n))
