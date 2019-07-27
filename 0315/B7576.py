from collections import deque

C, R = map(int, input().split())
X = []
for i in range(R):
    X += [list(map(int, input().split()))]

Q = deque()

for i in range(len(X)):
    for j in range(len(X[i])):
        if X[i][j] == 1:
            Q.append([i, j])

route = [[1, 0], [-1, 0], [0, 1], [0, -1]]

while Q:
    now = Q.popleft()
    for i in route:
        a, b = now[0]+i[0], now[1]+i[1]
        if a >= 0 and b >=0 and a < R and b < C:
            if X[a][b] == 0:
                X[a][b] = X[now[0]][now[1]] + 1
                Q.append([a,b])

result = 0
for i in X:
    for j in i:
        if j > result:
            result = j
result -=1
for i in X:
    for j in i:
        if j == 0:
            result = -1
            break

print(result)