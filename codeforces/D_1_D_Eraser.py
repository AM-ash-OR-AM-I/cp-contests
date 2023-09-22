import math
ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())

for _ in range(inp()):
    n, k = ints()
    s = input()
    i = 0
    cts = 0
    while i<n:
        if s[i] == 'B':
            i+=k
            cts+=1
        else:
            i+=1
    print(cts)