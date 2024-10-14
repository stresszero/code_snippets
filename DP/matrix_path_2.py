# 1차원 DP 배열 활용
def max_matrix_path(matrix):
    if not matrix or not matrix[0]:
        return 0

    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("The input matrix must be a square matrix.")

    dp = [0] * n
    dp[0] = matrix[0][0]

    for j in range(1, n):
        dp[j] = dp[j - 1] + matrix[0][j]

    for i in range(1, n):
        dp[0] += matrix[i][0]

        for j in range(1, n):
            dp[j] = max(dp[j], dp[j - 1]) + matrix[i][j]

    return dp[-1]
