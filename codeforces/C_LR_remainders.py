ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())

for _ in range(inp()):
    n, m = ints()
    arr = ints()
    directions = input()
    tokens = [0]*n
    left = 0
    right = n-1
    index = n-1
    for x in directions:
        if x=='L':
            tokens[index] = arr[left]
            left+=1
        else:
            tokens[index] = arr[right]
            right-=1
        index-=1
    
    # print(tokens)
    remainders = [0]*n
    index = n-1
    rem = 1
    for token in tokens:
        rem = (rem*token) % m
        remainders[index] = rem
        index-=1
    
    print(*remainders)
