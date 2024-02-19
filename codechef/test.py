ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())

for _ in range(inp()):
    n, q = ints()
    s = input()
    longest_arr = [0]*(q+1)
    longest = 1
    prev = None
    same_count = 1
    for x in s:
        if x==prev:
            same_count+=1
        else:
            same_count = 1
        longest = max(longest, same_count)
        prev=x
    longest_arr[0]=longest
    for i in range(q):
        char = input()
        if char == prev:
            same_count += 1
        else:
            same_count = 1
        longest = max(longest, same_count)
        longest_arr[i+1] = longest
        prev = char
    print(*longest_arr)
    