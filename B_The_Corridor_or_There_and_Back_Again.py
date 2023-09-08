import math
ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())

for _ in range(inp()):
    n = inp()
    maxSteps = None
    for _ in range(n):
        d, s = ints()
        if maxSteps is None:
            maxSteps = d+math.ceil(s/2)-1
        else:
            maxSteps = min(maxSteps, d+math.ceil(s/2)-1)
    print(maxSteps)
    