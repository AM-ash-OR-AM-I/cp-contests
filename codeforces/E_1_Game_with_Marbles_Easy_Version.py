ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())


def diff_arr(sorted_arr, diff_arr):
    prev = sorted_arr[0][0]
    for i, (x, index) in enumerate(sorted_arr[1:]):
        diff_arr[i] = x - prev
        prev = x


for _ in range(inp()):
    n = inp()
    a = ints()
    b = ints()
