ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())

for _ in range(inp()):
    n = inp()
    arr1 = ints()
    arr2 = ints()
    diff = [(i + 1, arr1[i] - arr2[i]) for i in range(n)]
    max_val = max(diff, key=lambda x: x[1])
    strong_vertices = []
    for i, val in enumerate(diff):
        if val[1] == max_val[1]:
            strong_vertices.append(val[0])
    print(len(strong_vertices))
    print(*strong_vertices)
