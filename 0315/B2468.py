import sys

sys.stdin = open('B2468.txt')


def BFS(i, j):
    route = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    Q = [[i, j]]
    while Q:
        now = Q.pop(0)
        for k in route:
            a, b = now[0] + k[0], now[1] + k[1]
            if 0 <= a < N and 0 <= b < N and not visit[a][b]:
                visit[a][b] = True
                Q.append([a, b])



N = int(input())

X = []

for _ in range(N):
    X.append(list(map(int, input().split())))

height = [0]

for i in range(N):
    for j in range(N):
        if X[i][j] not in height:
            height.append(X[i][j])

result = []
for h in height:
    visit = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if X[i][j] <= h:
                visit[i][j] = True
    for i in range(N):
        for j in range(N):
            if visit[i][j] == False:
                cnt += 1
                BFS(i, j)
    result.append(cnt)

print(max(result))