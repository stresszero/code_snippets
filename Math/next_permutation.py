# 주어진 순열 arr의 다음 순열을 반환하는 함수, 마지막 순열이면 -1 반환
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
