import sys

sys.stdin = open('5653.txt')

def check():

    for i in cells:
        if i[3] != -1:
            i[3] += 1

    route = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    for i in cells:
        if i[3] == i[2]+1:
            for j in route:
                a, b = i[0] + j[0], i[1] + j[1]
                if [a, b] not in dead_cells:
                    for k in cells:
                        if k[0] == a and k[1] == b:
                            if k[3] == 0:
                                if k[2] < i[2]:
                                    k[2] = i[2]
                            break
                    else:
                        cells.append([a, b, i[2], 0])

    for i in cells:
        if i[3] == i[2]*2:
            i[3] = -1
    h = 0
    while h < len(cells):
        if cells[h][3] == -1:
            dead_cells.append([cells[h][0], cells[h][1]])
            cells.pop(h)
            h -= 1
        h += 1


T = int(input())


for test_case in range(1, T+1):
    N, M, K = map(int, input().split())

    X = []

    for i in range(N):
        X.append(list(map(int, input().split())))

    cells = []

    for i in range(N):
        for j in range(M):
            if X[i][j] != 0:
                cells.append([i, j, X[i][j], 0])

    dead_cells = []

    for i in range(K):
        check()

    print('#{} {}'.format(test_case, len(cells)))