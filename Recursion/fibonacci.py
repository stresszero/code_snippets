def factorial_recursion(n):
    if n <= 1:
        return 1
    else:
        return n * factorial_recursion(n - 1)


def factorial_memo(n):
    if n <= 1:
        return 1

    memo = [0] * (n + 1)
    memo[0] = 1
    memo[1] = 1

    for i in range(2, n + 1):
        memo[i] = i * memo[i - 1]

    return memo[n]


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
