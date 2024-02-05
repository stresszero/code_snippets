def make_moser_de_bruijn_seq(N):
    if N < 1:
        return None

    dp = [0] * (2**N)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, 2**N):
        if i % 2 == 0:
            dp[i] = 4 * dp[i // 2]
        else:
            dp[i] = 4 * dp[i // 2] + 1
    return dp
