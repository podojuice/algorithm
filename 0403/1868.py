import sys

sys.stdin = open('1868.txt')

def check(x, y):
    cnt = 0
    route = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
    for k in route:
        a, b = x + k[0], y+k[1]
        if 0 <= a < N and 0 <= b < N:
            if X[a][b] == '*':
                cnt += 1
    zido[x][y] = cnt

def BFS(x, y):
    global MAX
    Q = [[x,y]]
    route = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
    MAX += 1
    while Q:
        now = Q.pop(0)
        zido[now[0]][now[1]] = -1
        for k in route:
            a, b = now[0]+k[0], now[1]+k[1]
            if 0 <= a < N and 0 <= b < N:
                if zido[a][b] == 0:
                    Q.append([a, b])
                    zido[a][b] = -1
                elif zido[a][b] > 0:
                    zido[a][b] = -1





T = int(input())
for t in range(1, T+1):
    N = int(input())

    X = []

    for _ in range(N):
        X.append(list(input()))

    zido = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if X[i][j] == '.':
                check(i, j)
            else:
                zido[i][j] = -1

    MAX = 0

    for i in range(N):
        for j in range(N):
            if zido[i][j] == 0:
                BFS(i, j)

    for i in range(N):
        for j in range(N):
            if zido[i][j] > 0:
                MAX += 1

    print('#{} {}'.format(t, MAX))