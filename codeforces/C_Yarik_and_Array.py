# A subarray is a continuous part of array.

# Yarik recently found an array a
#  of n
#  elements and became very interested in finding the maximum sum of a non empty subarray. However, Yarik doesn't like consecutive integers with the same parity, so the subarray he chooses must have alternating parities for adjacent elements.

# For example, [1,2,3]
#  is acceptable, but [1,2,4]
#  is not, as 2
#  and 4
#  are both even and adjacent.

# You need to help Yarik by finding the maximum sum of such a subarray.

import math


ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())


for _ in range(inp()):
    n = inp()
    arr = ints()

    divisions = []

    start = end = 0

    if n == 1:
        print(arr[0])
        continue

    for i in range(1, n):
        if arr[i] % 2 != arr[i - 1] % 2:
            end = i
        else:
            divisions.append((start, end))
            start = end = i

    divisions.append((start, end))

    # print(divisions)
    max_subarr = -math.inf
    for start, end in divisions:
        sum_arr = [0] * (end + 1 - start)
        _sum = 0
        for i, x in enumerate(arr[start : end + 1]):
            _sum += x
            sum_arr[i] = _sum

        # print(sum_arr)
        min_sum_prefix = 0

        for i in range(len(sum_arr)):
            max_subarr = max(max_subarr, sum_arr[i] - min_sum_prefix)
            min_sum_prefix = min(min_sum_prefix, sum_arr[i])

        # max_subarr = max(max_subarr, sum_arr[-1] - min_sum_prefix)

    print(max_subarr)
