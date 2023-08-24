ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())

for _ in range(inp()):
    n = inp()
    arr = ints()
    prev = arr[0]
    new_arr = [prev]
    for x in arr[1:]:
        if x>=prev:
            new_arr.append(x)
        else:
            new_arr.extend([x, x])
        prev = x
    print(len(new_arr))
    print(*new_arr)