import math
from collections import Counter


ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())


for _ in range(inp()):
    n, k = ints()
    a = ints()
    b = ints()
    a_sum = [0] * n
    _sum = 0
    for i in range(n):
        _sum += a[i]
        a_sum[i] = _sum

    b_max_arr = [0] * n
    mx = b[0]
    for i in range(n):
        mx = max(b[i], mx)
        b_max_arr[i] = mx

    max_sum = 0
    cur_sum = 0
    # print(a_sum, b_max_arr)
    for i in range(min(n, k)):
        cur_sum = a_sum[i] + b_max_arr[i] * (k - i - 1)
        max_sum = max(cur_sum, max_sum)

    print(max_sum)

# Accepted
