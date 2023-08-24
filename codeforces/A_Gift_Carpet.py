ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())

for _ in range(inp()):
    n, m = ints()
    arr = [list() for _ in range(m)]
    # print(arr)
    for _ in range(n):
        s = input()
        for i,x in enumerate(s):
            arr[i].append(x)
    s = "vika"
    i=0
    # print(arr)
    possible = 0
    for col in arr:
        if s[i] in col:
            i+=1
            if i==4: 
                possible=1; break
    print("YES" if possible else "NO")
