def prep_KMP(pat: str):
    m = len(pat)
    F = [0] * m
    F[0] = -1
    idx = -1

    for i in range(1, m):
        while idx >= 0 and pat[i] != pat[idx + 1]:
            idx = F[idx]
        if pat[i] == pat[idx + 1]:
            idx += 1
        F[i] = idx

    return F


def KMP(txt: str, pat: str):
    n = len(txt)
    m = len(pat)
    F = prep_KMP(pat)
    idx = -1
    matches = []

    for i in range(n):
        while idx >= 0 and txt[i] != pat[idx + 1]:
            idx = F[idx]
        if txt[i] == pat[idx + 1]:
            idx += 1
        if idx == m - 1:
            matches.append(i - m + 1)
            idx = F[idx]

    return matches


print(prep_KMP("aabaa"))  # [-1, 0, -1, 0, 1]
print(KMP("aabaabaaa", "aabaa"))  # [0, 3]
