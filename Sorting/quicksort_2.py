def partition(arr, lo, hi):
    pivot = arr[lo]
    left = lo + 1
    right = hi

    while left <= right:
        while left <= hi and arr[left] < pivot:
            left += 1
        while right > lo and arr[right] >= pivot:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    arr[lo], arr[right] = arr[right], arr[lo]
    return right


def quicksort(arr, lo, hi):
    if lo < hi:
        pivot = partition(arr, lo, hi)
        quicksort(arr, lo, pivot - 1)
        quicksort(arr, pivot + 1, hi)


arr = [23, 10, 4, 1, 3, 7, 8, 45]
quicksort(arr, 0, len(arr) - 1)
print(arr)
