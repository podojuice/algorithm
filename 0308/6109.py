import sys

sys.stdin = open('6109.txt')

T = int(input())

for test_case in range(1, T+1):
    N = list(input().split())

    N, S = int(N[0]), N[1]

    X = []

    for _ in range(N):
        X.append(list(map(int, input().split())))

    if S == 'up':
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

    elif S == 'left':
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

    elif S == 'down':
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

    elif S == 'right':
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

    print('#{}'.format(test_case))


    for i in range(N):
        for j in range(N):
            print(X[i][j], end=' ')
        print()