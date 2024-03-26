# 유클리드 호제법
def euclidean(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Extended Euclidean Algorithm, 확장된 유클리드 알고리즘
def EEA(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = EEA(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y
