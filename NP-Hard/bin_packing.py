def approx_bin_packing_first_fit(items, bin_capacity=1):
    n = len(items)
    bin = [0] * n
    num = 0

    for i in range(n):
        first = num
        for j in range(num):
            if bin[j] + items[i] <= bin_capacity:
                first = j
                break
        bin[first] += items[i]
        if first >= num:
            num += 1

    return num


def approx_bin_packing_best_fit(items, bin_capacity=1):
    n = len(items)
    bin = [0] * n
    num = 0

    for i in range(n):
        best = num
        for j in range(num):
            if (
                bin[j] + items[i] <= bin_capacity
                and bin[j] + items[i] > bin[best] + items[i]
            ):
                best = j
        bin[best] += items[i]

        if best >= num:
            num += 1

    return num


def approx_bin_packing_desc_first_fit(items, bin_capacity=1):
    items.sort(reverse=True)
    return approx_bin_packing_first_fit(items, bin_capacity)


def approx_bin_packing_desc_best_fit(items, bin_capacity=1):
    items.sort(reverse=True)
    return approx_bin_packing_best_fit(items, bin_capacity)


print(approx_bin_packing_first_fit([0.3, 0.3, 0.3, 0.4, 0.3, 0.4]))
print(approx_bin_packing_best_fit([0.3, 0.3, 0.3, 0.4, 0.3, 0.4]))
print(approx_bin_packing_desc_first_fit([0.3, 0.3, 0.3, 0.4, 0.3, 0.4]))
print(approx_bin_packing_desc_best_fit([0.3, 0.3, 0.3, 0.4, 0.3, 0.4]))
