import math
from collections import Counter


ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())


for _ in range(inp()):
    n, k = ints()
    arr = list(range(1, n + 1))
    new_arr = arr[n - k - 1 :] + arr[: n - k - 1][::-1]
    print(*new_arr)

# Accepted
