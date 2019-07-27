import sys

sys.stdin = open('4408.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    X = []
    for _ in range(N):
        x, y = map(int, input().split())
        x, y = (x+1)//2, (y+1)//2
        if x > y:
            X.append([y, x])
        else:
            X.append([x, y])

    X.sort(key=lambda x : x[1])
    dp = [0]*(X[-1][1]+1)
    for i in X:
        for j in range(i[0], i[1]+1):
            dp[j] += 1
    cnt = max(dp)

    print('#{} {}'.format(t, cnt))