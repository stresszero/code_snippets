# 최장 공통 부분 수열(Long Common Subsequence)
def get_LCS_length_arr(x, y):
    n = len(x)
    m = len(y)
    LCS = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i - 1] == y[j - 1]:
                LCS[i][j] = LCS[i - 1][j - 1] + 1
            else:
                LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

    return LCS


def get_LCS(x, y):
    i = len(x)
    j = len(y)
    LCS = get_LCS_length_arr(x, y)
    idx = LCS[i][j]

    result = [""] * (idx + 1)
    while idx > 0:
        if x[i - 1] == y[j - 1]:
            result[idx - 1] = x[i - 1]
            i -= 1
            j -= 1
            idx -= 1
        elif LCS[i][j - 1] > LCS[i - 1][j]:
            j -= 1
        else:
            i -= 1

    return "".join(result)


print(get_LCS_length_arr("abc", "bdc"))
print(get_LCS("abc", "bdc"))
print(get_LCS("SNOWY", "SUNNY"))
