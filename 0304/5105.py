
import sys

sys.stdin = open('5105.txt', 'r')

T = int(input())


def BFS(Q):

    while Q:
        q = Q.pop(0)
        visit[q[0]][q[1]] = True
        route = [[q[0] + 1, q[1]], [q[0] - 1, q[1]], [q[0], q[1] + 1], [q[0], q[1] - 1]]
        for i in route:
            if 0 <= i[0] and 0 <= i[1] and N > i[0] and N > i[1] and not visit[i[0]][i[1]] and X[i[0]][i[1]] != 1:
                Q.append([i[0], i[1]])
                visit[i[0]][i[1]] = True
                D[i[0]][i[1]] = D[q[0]][q[1]] + 1


for test_case in range(1, T+1):
    N = int(input())
    X = []
    visit = [[False for k in range(N)] for i in range(N)]
    D = [[0 for k in range(N)] for i in range(N)]
    for i in range(N):
        X += [str(input())]
    for i in range(len(X)):
        X[i] = list(map(int, ' '.join(X[i]).split()))

    for i in range(N):
        for j in range(N):
            if X[i][j] == 3:
                x, y= i, j
            if X[i][j] == 2:
                rx, ry = i, j
    Q = [[x, y]]


    BFS(Q)
    if D[rx][ry]:
        print(D[rx][ry]-1)
    else:
        print(D[rx][ry])
