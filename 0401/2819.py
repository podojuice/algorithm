import sys

sys.stdin = open('2819.txt')


def DFS(i, j, k, n, st):
    if k == n:
        if st not in po:
            po.append(st)
        return
    route = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for p in route:
        a, b = i + p[0], j + p[1]
        if 0 <= a < 4 and 0 <= b < 4:
            st += X[a][b]
            DFS(a, b, k+1, n, st)
            st = st[:-1]

T = int(input())

for t in range(1, T+1):
    X = []

    for _ in range(4):
        X.append(list(map(str, input().split())))

    po = []

    for i in range(4):
        for j in range(4):
            key = X[i][j]
            DFS(i, j, 0, 6, key)
    print('#{} {}'.format(t, len(po)))
