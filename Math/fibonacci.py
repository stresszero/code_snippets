import math


def fibo_recursion(n):
    if n <= 1:
        return n
    else:
        return fibo_recursion(n - 1) + fibo_recursion(n - 2)


def fibo_dp(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def fibo_swap(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
    return x


def fibonacci_formula(n):
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2
    return int((1 / sqrt_5) * (phi**n - psi**n))

