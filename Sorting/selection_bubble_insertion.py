def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
                
        arr[i], arr[min_index] = arr[min_index], arr[i]

def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False

        for j in range(1, len(arr) - i):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swapped = True

        if not swapped:
            break

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        if key > arr[j]:
            continue

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

