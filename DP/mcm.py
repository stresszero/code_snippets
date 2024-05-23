# matrix chain multiplication
def min_mat_mult(n, d):
    C = [[0 for x in range(n)] for y in range(n)]
    P = [[0 for x in range(n)] for y in range(n)]

    for s in range(n):
        for i in range(n - s):
            j = i + s

            temp = []
            for k in range(i, j):
                temp.append([k, C[i][k] + C[k + 1][j] + d[i] * d[k + 1] * d[j + 1]])
            if temp:
                min_k, min_val = min(temp, key=lambda x: x[1])
                P[i][j] = min_k + 1
                C[i][j] = min_val

    return C, P


print(min_mat_mult(3, [4, 2, 3, 1]))
print(min_mat_mult(5, [5, 4, 2, 3, 1, 6]))

from functools import cache


def matrix_chain_order(dims: list[int]) -> int:
    @cache
    def a(i, j):
        return min(
            (a(i, k) + dims[i] * dims[k] * dims[j] + a(k, j) for k in range(i + 1, j)),
            default=0,
        )

    return a(0, len(dims) - 1)


print(matrix_chain_order([4, 2, 3, 1]))
print(matrix_chain_order([5, 4, 2, 3, 1, 6]))