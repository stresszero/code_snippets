def binary_search (arr, val):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == val:
            return mid
        if arr[mid] > val:
            end = mid - 1
        else:
            start = mid + 1
    return None

def recursive_bsearch(arr, val, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low > high:
        return None
    
    mid = (low + high) // 2
    if arr[mid] == val:
        return mid
    elif arr[mid] < val:
        return recursive_bsearch(arr, val, mid + 1, high)
    else:
        return recursive_bsearch(arr, val, low, mid - 1)
