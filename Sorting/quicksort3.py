def partition(arr, n):
    left = 0
    right = n - 1

    while left < right:
        while left < n - 1 and arr[left] < arr[0]:
            left += 1
        while right >= 1 and arr[right] >= arr[0]:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]

    arr[right], arr[0] = arr[0], arr[right]
    return right


def quicksort(arr, n):
    if n > 1:
        # print(arr)
        pivot = partition(arr, n)
        quicksort(arr[:pivot], pivot)
        quicksort(arr[pivot + 1 :], n - pivot - 1)


arr2 = [40, 10, 20, 30, 50]
quicksort(arr2, len(arr2))
print(arr2)
