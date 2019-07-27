import sys

sys.stdin = open('1953.txt')


def BFS(r, c):
    Q = [[r, c]]
    while Q:
        now = Q.pop(0)
        for k in po[X[now[0]][now[1]]]:
            a, b = now[0]+k[0], now[1]+k[1]
            if 0 <= a < N and 0 <= b < M:
                if X[a][b] and not visit[a][b]:
                    key = [k[0]*(-1), k[1]*(-1)]
                    if key in po[X[a][b]]:
                        Q.append([a, b])
                        visit[a][b] = visit[now[0]][now[1]] + 1


T = int(input())

for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split())

    po = [
        [],
        [[1, 0], [0, 1], [-1, 0], [0, -1]],
        [[1, 0], [-1, 0]],
        [[0, 1], [0, -1]],
        [[-1, 0], [0, 1]],
        [[1, 0], [0, 1]],
        [[1, 0], [0, -1]],
        [[-1, 0], [0, -1]]
    ]

    X = []

    for i in range(N):
        X.append(list(map(int, input().split())))

    # 1 -> 상하좌우   2 -> 상하   3 - > 좌우    4 -> 상우
    # 5 -> 하우    6 -> 하좌     7 -> 상좌

    visit = [[0 for _ in range(M)] for _ in range(N)]

    visit[R][C] = 1

    BFS(R, C)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0 < visit[i][j] <= L:
                cnt += 1
    # print(visit)
    print('#{} {}'.format(t, cnt))
