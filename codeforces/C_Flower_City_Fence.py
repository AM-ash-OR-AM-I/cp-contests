ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())

for _ in range(inp()):
    n = inp()
    arr = ints()
    if n==1: 
        print("YES" if arr[0]==1 else "NO"); continue
    
    ans = 1
    prev = arr[0]
    i = 1
    count = 1
    hw = []
    while i<n:
        x = arr[i]
        if prev == x:
            count+=1
        else:
            width = count
            height = prev-x
            hw.extend([width, height])
            count = 1
        i+=1
        prev = x
    height = x
    width = count
    hw.extend([width, height])   
    print("YES" if hw==hw[::-1] else "NO")