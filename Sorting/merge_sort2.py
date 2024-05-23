def merge_sort(arr):
    def merge(b, c):
        i = j = k = 0
        while (i < len(b)) and (j < len(c)):
            if b[i] < c[j]:
                arr[k] = b[i]
                i += 1
            else:
                arr[k] = c[j]
                j += 1
            k += 1

        for i in range(i, len(b)):
            arr[k] = b[i]
            k += 1

        for j in range(j, len(c)):
            arr[k] = c[j]
            k += 1

        return arr

    n = len(arr)
    if n > 1:
        mid = n // 2
        b = merge_sort(arr[:mid])
        c = merge_sort(arr[mid:])
        arr = merge(b, c)

    return arr


arr = [32, 27, 68, 1, 34, 6, 8, 2, 1, 7]
print(merge_sort(arr))
