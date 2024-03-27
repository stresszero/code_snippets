def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    count_arr = [0] * (max_val - min_val + 1)

    for i in arr:
        count_arr[i - min_val] += 1
    sorted_arr = []

    for i in range(len(count_arr)):
        sorted_arr += [i + min_val] * count_arr[i]

    return sorted_arr
