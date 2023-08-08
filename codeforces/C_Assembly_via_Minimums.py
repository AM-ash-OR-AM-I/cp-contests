from collections import Counter


ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())

for _ in range(inp()):
    n = inp()
    arr = ints()
    counts = Counter(arr)
    counts = sorted(counts.items(), key=lambda x: x[0])
    # print(counts)
    original_arr = [0] * n
    i = 0
    for x, count in counts:
        while count > 0:
            original_arr[i] = x
            i += 1
            count -= n - 1
            n -= 1
            if n == 0:
                break
    original_arr[-1] = original_arr[-2]
    print(*original_arr)
