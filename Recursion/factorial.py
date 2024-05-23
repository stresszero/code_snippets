def factorial_recursion(n):
    if n <= 1:
        return 1
    else:
        return n * factorial_recursion(n - 1)


def factorial_iteration(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_memo(n):
    if n <= 1:
        return 1

    memo = [0] * (n + 1)
    memo[0] = 1
    memo[1] = 1

    for i in range(2, n + 1):
        memo[i] = i * memo[i - 1]

    return memo[n]