import math
ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())

for _ in range(inp()):
    a, b, c = ints()
    g, s = max(a, b), min(a, b)
    v = math.ceil(math.ceil((g-s)/2)/c)
    print(v)
