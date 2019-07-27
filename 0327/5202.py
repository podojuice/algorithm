import sys

sys.stdin = open('5202.txt')

T = int(input())

for t in range(1, T+1):

    N = int(input())

    X = []

    for _ in range(N):
        X.append(list(map(int, input().split())))


    for i in range(len(X)-1):
        for j in range(1+i, len(X)):
            if X[i][1] > X[j][1]:
                X[i], X[j] = X[j], X[i]

    cnt = 1
    now = X[0][1]
    for i in range(1, len(X)):
        if X[i][0] >= now:
            cnt += 1
            now = X[i][1]

    print('#{} {}'.format(t, cnt))