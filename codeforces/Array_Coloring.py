ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())

n = inp()
for _ in range(n):
    n = inp()
    arr = ints()
    if sum(arr) & 1 == 0:
        print("YES")
    else:
        print("NO")
