import math
ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())

def odd(a):
    for x in range(2, int(math.sqrt(a))+1):
        if a%x==0:
            print(x, a-x)
            return
    print(-1)
    return
    


for _ in range(inp()):
    l, r = ints()
    if r <=3: 
        print(-1)
        continue
    else:
        if l==r:
            if l%2==0:
                half = l//2
                print(half, half)
            else:
                odd(l)
                    
        else:
            half = r//2 if r%2==0 else (r-1)//2
            print(half, half)   

            