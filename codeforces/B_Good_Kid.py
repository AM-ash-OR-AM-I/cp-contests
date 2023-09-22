import math
ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())

for _ in range(inp()):
    n = inp()
    arr = ints()
    m = min(arr)
    prod = 1
    found_min = 0
    for x in arr:
        if x != m or found_min:
            prod *= x
        else:
            prod *= m+1
            found_min = 1
    print(prod)