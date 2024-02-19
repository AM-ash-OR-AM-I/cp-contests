alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 10**5
inp = lambda: int(input())

for _ in range(inp()):
    n = inp()
    s = input()
    dig_sum = 0
    new_sum = [0]*(n+1)
    sum_arr = [0]*n
    for i, x in enumerate(s):
        dig_sum += int(x)
        sum_arr[i] = dig_sum
    
    carry = 0 
    for i in range(n-1, -1, -1):
        dig_sum = int(sum_arr[i]) + carry
        value, carry = dig_sum%10, dig_sum//10
        new_sum[i+1] = value

    if carry:
        new_sum[0] = carry

    start = 0
    while new_sum[start]==0:
        start+=1
    print(*new_sum[start:], sep="")