import sys

from copy import deepcopy

from itertools import combinations

# def wall(k, a):
#     global result
#
#     if k == a:
#         BFS(V)
#         cnt = 0
#         for i in range(N):
#             for j in range(M):
#                 if X[i][j] == 0:
#                     cnt += 1
#                     print(cnt)
#         result = max(result, cnt)
#         return
#
#     for i in range(N):
#         for j in range(M):
#             if X[i][j] == 0:
#                 X[i][j] = 1
#                 wall(k+1, 3)
#                 X[i][j] = 0


sys.stdin = open('14502.txt')

def BFS(V, temp):
    route = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while V:
        now = V.pop(0)
        for i in route:
            a, b = now[0] + i[0], now[1] + i[1]
            if N > a >= 0 and M > b >= 0 and temp[a][b] == 0:
                temp[a][b] = 2
                V.append([a, b])
    return temp





N, M = map(int, input().split())

X = []

result = 0

for _ in range(N):
    X.append(list(map(int, input().split())))

V = []

O = []

for i in range(N):
    for j in range(M):
        if X[i][j] == 2:
            V.append([i, j])
        elif X[i][j] == 0:
            O.append([i, j])

O_list = list(combinations(O, 3))




for i in O_list:
    temp = deepcopy(X)
    B = deepcopy(V)
    temp[i[0][0]][i[0][1]] = 1
    temp[i[1][0]][i[1][1]] = 1
    temp[i[2][0]][i[2][1]] = 1

    A = BFS(B, temp)
    cnt = 0

    for i in range(N):
        for j in range(M):
            if A[i][j] == 0:
                cnt += 1
    # print(cnt)
    result = max(result, cnt)



print(result)

# V 벽 세운 뒤 할 것.
    # BFS(V)
    #
    # cnt = 0
    # for i in range(N):
    #     for j in range(M):
    #         if X[N][M] == 0:
    #             cnt += 1
    #
    # result = min(result, cnt)



