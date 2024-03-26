def cubesort(arr, low, high):
    if low < high:
        pivot = arr[(low + high) // 2]
        i = low
        j = high

        while i <= j:
            while arr[i] < pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
                
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        cubesort(arr, low, j)
        cubesort(arr, i, high)
