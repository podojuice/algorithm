import sys
sys.stdin = open('B2589.txt')

from collections import deque

def BFS(d):
    x, y = d[0], d[1]

    visit = [[False] * C for _ in range(R)]
    D = [[0]*C for _ in range(R)]
    Q = deque()

    Q.append([x, y])
    visit[x][y] = True
    while Q:
        now = Q.popleft()
        route = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in route:
            a, b = now[0] + i[0], now[1] + i[1]
            if 0 <= a < R and 0 <= b < C and X[a][b] == 'L' and visit[a][b] == False:
                Q.append([a, b])
                visit[a][b] = True
                D[a][b] = D[now[0]][now[1]] + 1
    max_num = 0
    for i in D:
        for j in i:
            if j > max_num:
                max_num = j
    return max_num

R, C = map(int, input().split())

X = []

for _ in range(R):
    X.append(list(map(str, input())))

result = []
route = [[1,0], [-1,0], [0,1], [0,-1]]
for i in range(R):
    for j in range(C):
        if X[i][j] == 'L':

            result += [BFS([i, j])]

print(max(result))