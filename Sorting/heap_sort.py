def heap_sort(arr):
    n = len(arr)

    # 인수로 받은 배열을 힙으로 변환
    for i in range(n):
        parent = (i - 1) // 2
        while parent >= 0 and arr[parent] < arr[i]:
            arr[parent], arr[i] = arr[i], arr[parent]
            i = parent
            parent = (i - 1) // 2

    # 힙에서 최댓값을 삭제하고 힙으로 재구성하는 과정 반복
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0] # 최댓값 삭제

        # 힙 재구성
        parent = 0
        while True:
            left = 2 * parent + 1
            right = 2 * parent + 2
            if left >= i:
                break
            if right < i and arr[left] < arr[right]:
                left = right
            if arr[left] > arr[parent]:
                arr[left], arr[parent] = arr[parent], arr[left]
                parent = left
            else:
                break

    return arr


arr = [32, 27, 68, 1, 34, 6, 8, 2, 1, 7]
print(heap_sort(arr))
