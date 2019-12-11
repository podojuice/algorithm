N = int(input())

arr= []

for i in range(N):
    arr.append(list(map(int, input().split())))

dp = [[0, 0, 0] for _ in range(N)]
MIN = 1000000

dp[1][0] = 2000
dp[1][1] = arr[0][0]+arr[1][1]
dp[1][2] = arr[0][0] + arr[1][2]

for i in range(2, N):
    if dp[i-1][1] > dp[i-1][2]:
        dp[i][0] = dp[i-1][2] + arr[i][0]
    else:
        dp[i][0] = dp[i-1][1] + arr[i][0]

    if dp[i-1][0] > dp[i-1][2]:
        dp[i][1] = dp[i-1][2] + arr[i][1]
    else:
        dp[i][1] = dp[i-1][0] + arr[i][1]

    if dp[i-1][1] > dp[i-1][0]:
        dp[i][2] = dp[i-1][0] + arr[i][2]
    else:
        dp[i][2] = dp[i-1][1] + arr[i][2]

MIN = min(dp[N-1][1], dp[N-1][2], MIN)

dp[1][1] = 2000
dp[1][0] = arr[0][1]+arr[1][0]
dp[1][2] = arr[0][1] + arr[1][2]

for i in range(2, N):
    if dp[i-1][1] > dp[i-1][2]:
        dp[i][0] = dp[i-1][2] + arr[i][0]
    else:
        dp[i][0] = dp[i-1][1] + arr[i][0]

    if dp[i-1][0] > dp[i-1][2]:
        dp[i][1] = dp[i-1][2] + arr[i][1]
    else:
        dp[i][1] = dp[i-1][0] + arr[i][1]

    if dp[i-1][1] > dp[i-1][0]:
        dp[i][2] = dp[i-1][0] + arr[i][2]
    else:
        dp[i][2] = dp[i-1][1] + arr[i][2]

MIN = min(dp[N-1][0], dp[N-1][2], MIN)

dp[1][2] = 2000
dp[1][1] = arr[0][2]+arr[1][1]
dp[1][0] = arr[0][2] + arr[1][0]

for i in range(2, N):
    if dp[i-1][1] > dp[i-1][2]:
        dp[i][0] = dp[i-1][2] + arr[i][0]
    else:
        dp[i][0] = dp[i-1][1] + arr[i][0]

    if dp[i-1][0] > dp[i-1][2]:
        dp[i][1] = dp[i-1][2] + arr[i][1]
    else:
        dp[i][1] = dp[i-1][0] + arr[i][1]

    if dp[i-1][1] > dp[i-1][0]:
        dp[i][2] = dp[i-1][0] + arr[i][2]
    else:
        dp[i][2] = dp[i-1][1] + arr[i][2]

MIN = min(dp[N-1][1], dp[N-1][0], MIN)

print(MIN)