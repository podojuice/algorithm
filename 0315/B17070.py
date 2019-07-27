import sys

sys.stdin = open('B17070.txt')

N = int(input())

X = []


for _ in range(N):
    X.append(list(map(int, input().split())))
if X[1][1] == 1:
    X[1][1] = -1
for i in range(N):
    for j in range(2, N):
        if X[i][j] == 1:
            X[i][j] = -1
        else:
            X[i][j] = [0, 0, 0]

if X[N-1][N-1] == -1:
    print(0)
else:
    if X[0][2] != -1:
        X[0][2][0] += 1
    if X[1][2] != -1 and X[0][2] != -1 and X[1][1] != -1:
        X[1][2][2] += 1

    for i in range(N):
        for j in range(2):
            X[i][j] = -1

    route = [[0, -1], [-1, 0], [-1, -1]]

    for i in range(N):
        for j in range(2, N):
            if X[i][j] != -1:
                for k in range(len(route)):
                    a, b = i + route[k][0], j + route[k][1]
                    key = X[a][b]
                    if a < N and b < N:
                        if k == 0:
                            if key != -1:
                                X[i][j][0] = key[0] + key[2]
                        elif k == 1:
                            if X[a][b] != -1:
                                X[i][j][1] = key[1] + key[2]
                        else:
                            if key != -1 and X[a+1][b] != -1 and X[a][b+1] != -1:
                                X[i][j][2] = key[0] + key[1] + key[2]

    print(sum(X[N-1][N-1]))



