import sys

sys.stdin = open('3.txt')

T = int(input())


for test_case in range(1, 11):
    N, K = map(int, input().split())

    X = []

    for i in range(N):
        X.append(list(map(int, input().split())))
    cnt = 0
    for i in range(N):
        for j in range(N-K+1):
            if X[i][j] == 1:
                if j == 0:
                    for p in range(K):
                        if X[i][j+p] == 0:
                            break
                    else:
                        if X[i][j+K] == 0:
                            cnt += 1
                elif j == N-K:
                    for p in range(K):
                        if X[i][j+p] == 0:
                            break
                    else:
                        if X[i][j-1] == 0:
                            cnt += 1
                else:
                    for p in range(K):
                        if X[i][j+p] == 0:
                            break
                    else:
                        if X[i][j+K] == 0 and X[i][j-1] == 0:
                            cnt += 1

    for i in range(N):
        for j in range(N-K+1):
            if X[j][i] == 1:
                if j == 0:
                    for p in range(K):
                        if X[j+p][i] == 0:
                            break
                    else:
                        if X[j+K][i] == 0:
                            cnt += 1
                elif j == N-K:
                    for p in range(K):
                        if X[j+p][i] == 0:
                            break
                    else:
                        if X[j-1][i] == 0:
                            cnt += 1
                else:
                    for p in range(K):
                        if X[j+p][i] == 0:
                            break
                    else:
                        if X[j+K][i] == 0 and X[j-1][i] == 0:
                            cnt += 1

    print('#{} {}'.format(test_case, cnt))