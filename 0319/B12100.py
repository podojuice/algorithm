import sys

sys.stdin = open('B12100.txt')

from copy import deepcopy




def side(dp, s):
    X = deepcopy(dp)
    if s == 0:
        for i in range(N):
            for j in range(N-1):
                if X[j][i] != 0:
                    for k in range(1, N-j):
                        if X[j+k][i] != X[j][i] and X[j+k][i] != 0:
                            break
                        elif X[j+k][i] == X[j][i]:
                            X[j][i] = X[j][i]* 2
                            X[j+k][i] = 0
                            break
        for i in range(N):
            for j in range(N-1):
                if X[j][i] == 0:
                    for k in range(1, N - j):
                        if X[j + k][i] != 0:
                            X[j][i] = X[j+k][i]
                            X[j+k][i] = 0
                            break

    elif s == 1:
        for i in range(N):
            for j in range(N-1):
                if X[i][j] != 0:
                    for k in range(1, N-j):
                        if X[i][j+k] != X[i][j] and X[i][j+k] != 0:
                            break
                        elif X[i][j+k] == X[i][j]:
                            X[i][j] = X[i][j]* 2
                            X[i][j+k] = 0
                            break
        for i in range(N):
            for j in range(N-1):
                if X[i][j] == 0:
                    for k in range(1, N - j):
                        if X[i][j + k] != 0:
                            X[i][j] = X[i][j+k]
                            X[i][j+k] = 0
                            break

    elif s == 2:
        for i in range(N):
            for j in range(N-1):
                if X[-j-1][i] != 0:
                    for k in range(1, N-j):
                        if X[-(j+k)-1][i] != X[-1-j][i] and X[-(j+k)-1][i] != 0:
                            break
                        elif X[-(j+k)-1][i] == X[-j-1][i]:
                            X[-j-1][i] = X[-j-1][i]* 2
                            X[-(j+k)-1][i] = 0
                            break
        for i in range(N):
            for j in range(N-1):
                if X[-j-1][i] == 0:
                    for k in range(1, N - j):
                        if X[-(j+k)-1][i] != 0:
                            X[-j-1][i] = X[-(j+k)-1][i]
                            X[-(j+k)-1][i] = 0
                            break

    elif s == 3:
        for i in range(N):
            for j in range(N-1):
                if X[i][-j-1] != 0:
                    for k in range(1, N-j):
                        if X[i][-(j+k)-1] != X[i][-j-1] and X[i][-(j+k)-1] != 0:
                            break
                        elif X[i][-(j+k)-1] == X[i][-j-1]:
                            X[i][-j-1] = X[i][-j-1]* 2
                            X[i][-(j+k)-1] = 0
                            break
        for i in range(N):
            for j in range(N-1):
                if X[i][-j-1] == 0:
                    for k in range(1, N - j):
                        if X[i][-(j+k)-1] != 0:
                            X[i][-j-1] = X[i][-(j+k)-1]
                            X[i][-(j+k)-1] = 0
                            break

    return X


def DFS(X, k):
    if k == 5:
        global result
        for i in X:
            for j in i:
                if j > result:
                    result = j
        return
    for i in range(5):
        dp = side(X, i)
        DFS(dp, k+1)


N = int(input())

dp = []

result = 0

for _ in range(N):
    dp.append(list(map(int, input().split())))

DFS(dp, 0)

print(result)