

def BFS(Q):
    route = [[-3, -2], [-3, 2], [-2, 3], [2, 3], [3, 2], [3, -2], [2, -3], [-2, -3]]
    while Q:
        now = Q.pop(0)
        for i in route:
            a, b = now[0] + i[0], now[1] + i[1]
            if 0 <= a < N and 0 <= b < N:
                if not maps[a][b]:
                    maps[a][b] = maps[now[0]][now[1]] + 1
                    Q.append([a, b])

        if maps[tx][ty]:
            return


T = int(input())

for t in range(1, T+1):
    N = int(input())

    x, y, tx, ty = map(int, input().split())

    maps = [[0]*N for _ in range(N)]

    maps[x][y] = 1

    Q = [[x, y]]

    BFS(Q)

    print('#{} {}'.format(t, maps[tx][ty]-1))
