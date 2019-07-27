import sys

sys.stdin = open('B2591.txt')

N = input()

dp = [0]*len(N)

dp[0] = 1

if len(N) >= 2:
    if int(N[:2]) > 34 or not int(N[:2]) % 10:
        dp[1] = 1
    else:
        dp[1] = 2

for i in range(2, len(N)):
    if N[i] == '0':
        if N[i-1] == '0' or int(N[i-1]) >=4:
            dp[-1] = 0
            break
        dp[i] = dp[i - 2]
    elif N[i] != '0':
        if N[i - 1] == '0':
            dp[i] = dp[i - 1]
        elif int(N[i-1:i+1]) <= 34:
            dp[i] = dp[i-2]+dp[i-1]
        else:
            dp[i] = dp[i-1]

print(dp[-1])