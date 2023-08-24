ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())
from math import comb, isqrt

for _ in range(inp()):
    n = inp()
    x = int((1 + isqrt(1+8*n))/2)
    x += n - comb(x, 2)
    print(x)