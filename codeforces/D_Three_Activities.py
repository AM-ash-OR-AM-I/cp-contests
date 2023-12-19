import math
from collections import Counter


ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())


def diff_arr(sorted_arr, diff_arr):
    prev = sorted_arr[0][0]
    for i, (x, _) in enumerate(sorted_arr[1:]):
        diff_arr[i] = x - prev
        prev = x


for _ in range(inp()):
    n = inp()
    a = ints()
    b = ints()
    c = ints()
    a_sorted = sorted(((x, i) for i, x in enumerate(a)), reverse=True)
    b_sorted = sorted(((x, i) for i, x in enumerate(b)), reverse=True)
    c_sorted = sorted(((x, i) for i, x in enumerate(c)), reverse=True)
    a_diff = [0] * n
    b_diff = [0] * n
    c_diff = [0] * n
    diff_arr(a_sorted, a_diff)
    diff_arr(b_sorted, b_diff)
    diff_arr(c_sorted, c_diff)

    mx = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                max_a, index1 = a_sorted[i]
                max_b, index2 = b_sorted[j]
                max_c, index3 = c_sorted[k]
                if index1 != index2 != index3 != index1:
                    mx = max(mx, max_a + max_b + max_c)
    print(mx)


# Accepted
