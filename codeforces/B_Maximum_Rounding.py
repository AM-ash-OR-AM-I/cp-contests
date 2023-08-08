ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())

for _ in range(inp()):
    str_n = input()
    rounded_n = [0] + list(int(x) for x in str_n)
    index = len(str_n)
    for i, x in enumerate(str_n):
        if int(x) >= 5:
            rounded_n[i] += 1
            rounded_n[i + 1 :] = [0] * (len(str_n) - i)
            for j in range(i, 0, -1):
                if rounded_n[j] == 5:
                    rounded_n[j - 1] += 1
                    index = j
            rounded_n[index:] = [0] * (len(str_n) - index + 1)
            break
    print("".join(str(x) for x in rounded_n).lstrip("0"))
