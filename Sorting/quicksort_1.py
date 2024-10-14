def quicksort_lomuto(arr):
    def _quicksort(arr, low, high):
        if low < high:
            p = _partition(arr, low, high)
            _quicksort(arr, low, p - 1)
            _quicksort(arr, p + 1, high)

    def _partition(arr, low, high):
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    _quicksort(arr, 0, len(arr) - 1)
    return arr


def hoare_partition(arr, left, right):
    pivot = arr[right]  # 피벗을 오른쪽 끝 값으로 설정
    i = left - 1  # 왼쪽 포인터

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # 왼쪽 포인터보다 작거나 같은 값 교환

    # 피벗 값을 왼쪽 포인터 다음 위치로 이동
    arr[i + 1], arr[right] = arr[right], arr[i + 1]

    return i + 1


def quick_sort(arr, left, right):
    if left < right:
        pivot_index = hoare_partition(arr, left, right)
        quick_sort(arr, left, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, right)


# 로무토 분할 예시
arr = [5, 2, 4, 1, 3]
quicksort_lomuto(arr)
print(arr)  # [1, 2, 3, 4, 5]

# 호어 분할 예시
arr = [5, 2, 4, 1, 3]
quick_sort(arr, 0, len(arr) - 1)
print(arr)  # [1, 2, 3, 4, 5]
