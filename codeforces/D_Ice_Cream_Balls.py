ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())

for _ in range(inp()):
    n = inp()
    x = (1 + (1+8*n)**.5)/2
    if x != int(x):
        x = int(x)
        print(int(x+(n-(x*(x-1)/2))))
    else:
        print(int(x))