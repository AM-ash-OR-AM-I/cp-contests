import math
ints = lambda: list(map(int, input().split()))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())

n = inp()
for _ in range(n):
    points = 0
    grid = [list(input()) for _ in range(10)]
    for i in range(10):
        for j in range(10):
            if grid[i][j] == "X":
                if 4<=j<=5 and 4<=i<=5:
                    points += 5
                elif 3<=j<=6 and 3<=i<=6:
                    points += 4
                elif 2<=j<=7 and 2<=i<=7:
                    points += 3
                elif 1<=j<=8 and 1<=i<=8:
                    points += 2
                else:
                    points += 1
    print(points)