from KMP import prep_KMP


def bad_char(pat, alphabet):
    m = len(pat)
    bad_char = {c: -1 for c in alphabet}
    for i in range(m):
        bad_char[pat[i]] = i
    return bad_char


def good_suffix(pat):
    m = len(pat)
    rev_F = prep_KMP(pat[::-1])
    good_suffix = [m - 1 - rev_F[m - 1]] * (m + 1)

    for i in range(m - 1, -1, -1):
        good_suffix[m - 1 - rev_F[i]] = i - rev_F[i]

    return good_suffix


def boyer_moore(text, pat, alphabet):
    n = len(text)
    m = len(pat)
    bc = bad_char(pat, alphabet)
    gs = good_suffix(pat)
    matches = []

    i = m - 1
    while i < n:
        j = m - 1
        while j >= 0 and pat[j] == text[i]:
            j -= 1
            i -= 1
        if j == -1:
            matches.append(i + 1)
            i += gs[-1] + m
        else:
            i += max(gs[j], j - bc[text[i]]) + m - j - 2

    return matches


print(bad_char("ababcab", ["a", "b", "c", "d"]))
print(good_suffix("ababcab"))  # [5, 5, 5, 5, 5, 3, 3, 1]
print(boyer_moore("abababcababcaba", "ababcab", ["a", "b", "c", "d"]))  # [2, 9]
