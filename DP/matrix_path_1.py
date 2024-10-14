# 주어진 행렬의 (0, 0)지점에서 출발하여 맨 아래쪽 끝 지점(n, n)까지 이동할 때,
# 오른쪽이나 아래쪽으로만 이동할 수 있는 경우 가능한 경로의 최대값을 구하는 함수
def max_matrix_path(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("The input matrix must be a square matrix.")

    dp = [[0] * n for _ in range(n)]
    dp[0][0] = matrix[0][0]

    # right
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + matrix[0][j]

    # down
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]
    
    # all possible paths
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]

    return dp[n - 1][n - 1]


matrix = [
    [6, 7, 12, 5], 
    [5, 3, 11, 18], 
    [7, 17, 3, 3], 
    [8, 10, 14, 9]
]

print(max_matrix_path(matrix)) # 68: 6 -> 5 -> 7 -> 17 -> 10 -> 14 -> 9