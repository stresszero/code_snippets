def two_way_string_matching(text, pattern):
    """
    Two-Way 문자열 매칭 알고리즘 구현

    Args:
        text (str): 검색할 텍스트
        pattern (str): 찾을 패턴

    Returns:
        list: 패턴이 텍스트에서 발견된 모든 시작 위치 목록
    """
    results = []
    n = len(text)
    m = len(pattern)

    if m == 0:
        return [i for i in range(n + 1)]

    if n < m:
        return []

    # bad character 테이블 계산 (Boyer-Moore)
    bad_char = {}
    for i in range(m - 1):
        bad_char[pattern[i]] = m - 1 - i

    # 최대 접미사 계산 및 factorization 위치 결정
    i = max_suffix(pattern)
    j = max_suffix(pattern[::-1])

    if i > j:
        pos = i
    else:
        pos = m - j - 1

    # 주기 계산
    period = m - pos if i >= j else pos + 1

    # 메인 검색 루프
    k = 0
    while k <= n - m:
        # 접미사 매칭 시도
        j = m - 1
        while j >= pos and pattern[j] == text[k + j]:
            j -= 1

        if j < pos:
            # 접두사 매칭 시도
            j = pos - 1
            while j >= 0 and pattern[j] == text[k + j]:
                j -= 1

            if j < 0:
                # 매치 발견
                results.append(k)

            # 주기만큼 이동
            k += period
        else:
            # 접미사에서 불일치 발생
            char = text[k + j]
            shift = bad_char.get(char, m)
            k += max(1, shift)

    return results


def max_suffix(s):
    """
    최대 접미사의 위치 계산

    Args:
        s (str): 문자열

    Returns:
        int: 최대 접미사의 위치
    """
    m = len(s)
    ms = -1  # 최대 접미사 위치
    j = 0  # 현재 후보의 위치
    k = 1  # 현재 비교 길이

    while j + k < m:
        if s[j + k] < s[ms + k]:
            j += k
            k = 1
            ms = j - 1
        elif s[j + k] > s[ms + k]:
            ms = j
            j = ms + 1
            k = 1
        else:
            k += 1

    return j


# 사용 예시
if __name__ == "__main__":
    text = "ABABABCABABABABCABABABA"
    pattern = "ABABCABABA"

    positions = two_way_string_matching(text, pattern)
    print(f"패턴이 발견된 위치: {positions}")

    for pos in positions:
        print(f"{pos}: {text[pos:pos+len(pattern)]}")
