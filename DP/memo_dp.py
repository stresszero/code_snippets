memo = dict()


def dp(i, j):
    if (i, j) in memo:
        return memo[(i, j)]
    memo[(i, j)] = ...

    return memo[(i, j)]

# n = int(input())
# dp = [0] * (n + 1)

# bottom-up
def fibo_tabulation(n):
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# top-down
def fibo_memoization(n):
    if n <= 1:
        return n
    
    if dp[n]:
        return dp[n]
    
    dp[n] = fibo_memoization(n - 1) + fibo_memoization(n-2)
    return dp[n]