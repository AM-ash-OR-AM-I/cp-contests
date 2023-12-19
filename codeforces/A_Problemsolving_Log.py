import math
from collections import Counter


ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())


for _ in range(inp()):
    n = inp()
    s = input()
    c = 0
    cts = Counter(s)
    for x in cts:
        if cts[x] >= ord(x) - 64:
            c += 1
    print(c)


# Accepted
