ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())

for _ in range(inp()):
    n = inp()
    s = input()
    cts = 0
    prev = None
    for x in s:
        if x=="@":
            cts +=1
        elif x == prev == '*':
            break
        prev = x
    print(cts)
