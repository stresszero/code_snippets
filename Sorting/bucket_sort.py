def bucket_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    bucket_range = (max_val - min_val) / len(arr)
    bucket = [[] for _ in range(len(arr) + 1)]
    sorted_arr = []

    for i in range(len(arr)):
        bucket_index = int((arr[i] - min_val) / bucket_range)
        if bucket_index == len(arr):
            bucket_index -= 1
        bucket[bucket_index].append(arr[i])

    for i in range(len(bucket)):
        bucket[i] = sorted(bucket[i])

    for i in range(len(bucket)):
        sorted_arr += bucket[i]

    return sorted_arr
