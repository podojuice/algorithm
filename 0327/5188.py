import sys

sys.stdin = open('5188.txt')


def DFS(visit, i, j, cnt):
    global result

    if cnt >= result:
        return
    if i == N - 1 and j == N - 1:
        cnt += X[i][j]
        if cnt < result:
            result = cnt
        return

    route = [[1, 0], [0, 1]]

    for k in route:
        a, b = i+k[0], j+k[1]
        if 0 <= a < N and 0 <= b < N:
            if not visit[a][b]:
                visit[i][j] = True
                DFS(visit, a, b, cnt+X[i][j])
                visit[i][j] = False


T = int(input())


for te in range(1, T+1):
    N = int(input())

    X = []

    for _ in range(N):
        X.append(list(map(int, input().split())))

    result = 0xffffff

    visit = [[False]*N for _ in range(N)]

    DFS(visit, 0, 0, 0)

    print('#{} {}'.format(te, result))
