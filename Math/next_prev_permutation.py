# 주어진 순열 arr의 다음 순열을 반환하는 함수, arr이 마지막 순열이면 -1 반환
def next_permutation(arr):
    n = len(arr)
    i = n - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1

    if i == 0:
        return [-1]

    j = n - 1
    while arr[j] <= arr[i - 1]:
        j -= 1

    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    arr[i:] = arr[i:][::-1]
    return arr

# 이전 순열을 반환하는 함수
def prev_permutation(arr):
    n = len(arr)
    i = n - 1
    while i > 0 and arr[i - 1] <= arr[i]:
        i -= 1

    if i == 0:
        return [-1]

    j = n - 1
    while arr[j] >= arr[i - 1]:
        j -= 1

    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    arr[i:] = arr[i:][::-1]
    return arr

# is_next 플래그에 따라 이전 또는 다음 순열을 반환하는 함수
def find_permutation(arr, is_next=True):
    n = len(arr)
    i = n - 1 if is_next else n - 1
    while i > 0 and ((arr[i - 1] >= arr[i]) if is_next else (arr[i - 1] <= arr[i])):
        i -= 1

    if i == 0:
        return [-1]

    j = n - 1
    while (arr[j] <= arr[i - 1]) if is_next else (arr[j] >= arr[i - 1]):
        j -= 1

    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    arr[i:] = arr[i:][::-1]
    return arr
