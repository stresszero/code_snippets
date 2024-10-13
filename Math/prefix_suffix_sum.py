# 누적합: prefix sum, cumulative sum, inclusive scan

nums = list(map(int, input().split()))
N = len(nums)

# 0으로 시작하는 누적합 배열
sum_arr = [0] * (N + 1)
for i in range(1, N + 1):
    sum_arr[i] = sum_arr[i - 1] + nums[i - 1]
print(sum_arr)

# 원래 배열과 같은 크기의 누적합 배열
sum_arr = [0] * N
sum_arr[0] = nums[0]
for i in range(1, N):
    sum_arr[i] = sum_arr[i - 1] + nums[i]
print(sum_arr)

# suffix sum
sum_arr = [0] * N
sum_arr[N - 1] = nums[N - 1]
for i in range(N - 2, -1, -1):
    sum_arr[i] = sum_arr[i + 1] + nums[i]
print(sum_arr)
