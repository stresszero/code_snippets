def binary_search(arr, val):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == val:
            return mid
        if arr[mid] > val:
            end = mid - 1
        else:
            start = mid + 1
    return None

def recursive_bsearch(arr, val, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start > end:
        return None

    mid = (start + end) // 2
    if arr[mid] == val:
        return mid
    if arr[mid] > val:
        return recursive_bsearch(arr, val, start, mid - 1)
    return recursive_bsearch(arr, val, mid + 1, end)
