import sys

sys.stdin = open('B2667.txt')

def BFS(i, j):
    global cnt
    route = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visit[i][j] = True
    Q = [[i, j]]
    while Q:
        now = Q.pop(0)
        cnt += 1
        for k in route:
            a, b = now[0] + k[0], now[1] + k[1]
            if 0 <= a < N and 0 <= b < N and visit[a][b] == False and X[a][b] != '0':
                Q.append([a, b])
                visit[a][b] = True




N = int(input())

X = []

for i in range(N):
    X.append(list(map(str, input())))

visit = [[False]*N for i in range(N)]
result = []
volume = 0
for i in range(N):
    for j in range(N):
        if X[i][j] != '0' and visit[i][j] == False:
            cnt = 0
            BFS(i, j)
            volume += 1
            result.append(cnt)

result.sort()
print(volume)
for i in result:
    print(i)



