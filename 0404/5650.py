import sys

sys.stdin = open('5650.txt')


def check(x, y, a, b, dt):
    global MAX
    route = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    cnt = 0
    while 1:
        a, b = a + route[dt][0], b + route[dt][1]
        if a == -1:
            cnt += 1
            dt = 2
            continue
        elif b == -1:
            cnt += 1
            dt = 0
            continue
        elif a == N:
            cnt += 1
            dt = 3
            continue
        elif b == N:
            cnt += 1
            dt = 1
            continue

        if X[a][b] == 1:
            cnt += 1
            if dt == 0:
                dt = 1
            elif dt == 1:
                dt = 3
            elif dt == 2:
                dt = 0
            elif dt == 3:
                dt = 2

        elif X[a][b] == 2:
            cnt += 1
            if dt == 0:
                dt = 1
            elif dt == 1:
                dt = 2
            elif dt == 2:
                dt = 3
            elif dt == 3:
                dt = 0

        elif X[a][b] == 3:
            cnt += 1
            if dt == 0:
                dt = 2
            elif dt == 1:
                dt = 0
            elif dt == 2:
                dt = 3
            elif dt == 3:
                dt = 1

        elif X[a][b] == 4:
            cnt += 1
            if dt == 0:
                dt = 3
            elif dt == 1:
                dt = 0
            elif dt == 2:
                dt = 1
            elif dt == 3:
                dt = 2

        elif X[a][b] == 5:
            cnt += 1
            if dt == 0:
                dt = 1
            elif dt == 1:
                dt = 0
            elif dt == 2:
                dt = 3
            elif dt == 3:
                dt = 2

        if X[a][b] >= 6:
            for p in warm[X[a][b]-6]:
                if p != [a, b]:
                    a, b = p[0], p[1]
                    break
            continue

        if (a == x and b == y) or X[a][b] == -1:
            MAX = max(MAX, cnt)
            return


T = int(input())

for t in range(1, T+1):
    N = int(input())

    X = []

    for _ in range(N):
        X.append(list(map(int, input().split())))

    warm = [[] for _ in range(5)]

    for i in range(N):
        for j in range(N):
            if X[i][j] >= 6:
                warm[X[i][j]-6].append([i, j])

    MAX = 0
    for i in range(N):
        for j in range(N):
            if X[i][j] == 0:
                for k in range(4):
                    check(i, j, i, j, k)

    print('#{} {}'.format(t, MAX))
