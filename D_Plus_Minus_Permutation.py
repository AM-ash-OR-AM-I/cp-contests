import math
ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())

for _ in range(inp()):
    n, x, y = ints()
    lcm_xy = math.lcm(x, y)
    x_times = n//x
    y_times = n//y
    xy_times = n//lcm_xy
    x_end = n-x_times+xy_times+1
    x_sum = (n+x_end)*(n-x_end+1)
    y_sum = (y_times-xy_times)*(y_times-xy_times+1)
    score = (x_sum-y_sum)//2
    print(score)
