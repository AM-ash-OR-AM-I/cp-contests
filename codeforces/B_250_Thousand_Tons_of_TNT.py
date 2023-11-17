import math
from collections import Counter

ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())

for _ in range(inp()):
    n = inp()
    arr = ints()
    sum_arr = [0] * (n + 1)
    _sum = 0
    for i, x in enumerate(arr):
        _sum += x
        sum_arr[i + 1] = _sum

    abs_diff_truck_weight = 0
    for k in range(1, n // 2 + 1):
        min_truck_weight = math.inf
        max_truck_weight = -math.inf
        if n % k == 0:
            for i in range(0, n - k + 1, k):
                curr_truck_weight = sum_arr[i + k] - sum_arr[i]
                min_truck_weight = min(min_truck_weight, curr_truck_weight)
                max_truck_weight = max(max_truck_weight, curr_truck_weight)
                abs_diff_truck_weight = max(
                    abs_diff_truck_weight, abs(max_truck_weight - min_truck_weight)
                )
    print(abs_diff_truck_weight)
