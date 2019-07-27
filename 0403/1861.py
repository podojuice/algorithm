import sys

sys.stdin = open('1861.txt')

def DFS(dt, cnt, key):
    global result_max, result_num

    route = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    for k in route:
        a, b = dt[0] + k[0], dt[1] + k[1]
        if 0 <= a < N and 0 <= b < N:
            if X[a][b] == X[dt[0]][dt[1]] + 1:
                DFS([a, b], cnt+1, key)
    if cnt > result_max:
        result_num = key
        result_max = cnt


T = int(input())
for t in range(1, T+1):
    N = int(input())


    X = []

    for _ in range(N):
        X.append(list(map(int, input().split())))

    here = [[] for _ in range(N**2+1)]

    for i in range(N):
        for j in range(N):
            here[X[i][j]] = [i, j]
    result_num = 0

    result_max = 0
    for i in range(1, N**2+1):
        DFS(here[i], 1, i)

    print('#{} {} {}'.format(t, result_num, result_max))
