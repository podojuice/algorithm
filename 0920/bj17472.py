def BFS(x, y):
    Q = []
    Q.append([x, y])
    numbering[x][y] = inum
    while(Q):
        now = Q.pop(0)
        nx = now[0]
        ny = now[1]
        for i in range(4):
            tx = nx+D[i][0]
            ty = nx+D[i][1]
            if (0 <= tx < N) & (0 <= ty < M):
                if (numbering[tx][ty] == 0) & (island[tx][ty] == 1) & (not visit[tx][ty]):
                    Q.append([tx, ty])
                    numbering[tx][ty] = inum
                    visit[tx][ty] = True


N, M = map(int, input().split(' '))

island = []

inum = 1

D = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for i in range(N):
    island.append(list(map(int, input().split(' '))))

numbering= [[0]*M for _ in range(N)]
visit = [[False]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if island[i][j] == 1:
            if (numbering[i][j] == 0) & (not visit[i][j]):
                BFS(i, j)
                inum +=1


print(numbering)