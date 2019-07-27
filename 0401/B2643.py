import sys

sys.stdin = open('B2643.txt')

N = int(input())

arr = []

for _ in range(N):
    x, y = map(int, input().split())
    if x > y:
        arr.append([x, y])
    else:
        arr.append([y, x])
arr.sort()

print(arr)
dp = [1]*N


for i in range(1, N):
    for j in range(i):
        if dp[j]+1 > dp[i] and arr[i][0] >= arr[j][0] and arr[i][1] >= arr[j][1]:
            dp[i] = dp[j] + 1
# print(dp)
print(max(dp))
