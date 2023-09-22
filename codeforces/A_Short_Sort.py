import math
ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())

for _ in range(inp()):
    s = input()
    order = 'abc'
    v='NO'
    for i, x in enumerate(s):
        if x == order[i]: v='YES'
    print(v)
