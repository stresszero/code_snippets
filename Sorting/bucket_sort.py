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

    # 버킷 별로 정렬 수행
    for i in range(len(bucket)):
        bucket[i] = sorted(bucket[i])

    # 버킷 순서대로 정렬된 배열에 추가
    for i in range(len(bucket)):
        sorted_arr += bucket[i]

    return sorted_arr


arr = [8, 3, 2, 7, 4, 6, 8, 1]
print(bucket_sort(arr))
