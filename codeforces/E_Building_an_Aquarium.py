import math
from collections import Counter
ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())

for _ in range(inp()):
    n, x = ints()
    arr = ints()
    if n == 1: 
        print(x+arr[0])
        continue
    ctr = Counter(arr)
    sorted_arr = sorted(list(ctr.items()), key=lambda x: x[0])
    start_height = sorted_arr[0][0]
    max_height = start_height
    actual_index = 0
    for i, (curr_height, count) in enumerate(sorted_arr[:-1]):
        next_height = sorted_arr[i+1][0]
        diff = next_height - curr_height
        new_cap = (diff * count) + (actual_index * diff)
        if x >= new_cap: 
            x -= new_cap
            max_height += diff
        else: 
            added_height = x // (actual_index + count)
            max_height += added_height 
            x = 0
            break
        actual_index += count
    if x>0:
        added_height = x // n
        max_height += added_height
    print(max_height)
