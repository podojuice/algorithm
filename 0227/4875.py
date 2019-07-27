import sys

sys.stdin = open('4875.txt', 'r')

T = int(input())

def miro(X, visit, a, b):
    global result
    visit[a][b] = True
    if a > 0:
        if not visit[a-1][b]:
            if X[a-1][b] == 2:
                result = 1
            miro(X, visit, a-1, b)

    if a < len(X)-1:
        if not visit[a+1][b]:
            if X[a+1][b] == 2:
                result = 1
            miro(X, visit, a+1, b)

    if b > 0:
        if not visit[a][b-1]:
            if X[a][b-1] == 2:
                result = 1
            miro(X, visit, a, b-1)

    if b < len(X)-1:
        if not visit[a][b+1]:
            if X[a][b+1] == 2:
                result = 1
            miro(X, visit, a, b+1)


for test_case in range(1, T+1):

    N = int(input())
    X = []
    for i in range(N):
        X += [list(map(int, ' '.join(input()).split()))]
    visit = []
    for i in range(N):
        visit += [[False]*N]

    for i in range(len(X)):
        for j in range(len(X)):
            if X[i][j] == 3:
                a = i
                b = j
                # visit[a][b] = True
            if X[i][j] == 1:
                visit[i][j] = True
    result = 0
    miro(X, visit, a, b)
    print(f'#{test_case} {result}')

