import sys
# from collections import deque

sys.stdin = open('2117.txt')


def check(Q, visit):
    global max_num, cnt, S
    temp = []
    if not Q:
        return
    route = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while Q:
        now = Q.pop(0)
        for k in route:
            a, b = now[0]+k[0], now[1]+k[1]
            if N > a >= 0 and N > b >= 0 and not visit[a][b]:
                temp.append([a, b])
                visit[a][b] = True
                if X[a][b] == 1:
                    cnt += 1
    if S*S+(S-1)*(S-1) <= cnt*M and max_num < cnt:
        max_num = cnt
    for p in temp:
        Q.append(p)
    S += 1
    check(Q, visit)




T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    X = []

    for _ in range(N):
        X.append(list(map(int, input().split())))

    #N 지도 크기 M 가구 당 지불 능력
    max_num = 1
    for i in range(N):
        for j in range(N):
            if X[i][j] == 1:
                cnt = 1
            else:
                cnt = 0
            Q = []
            Q.append([i, j])
            visit = [[False]*N for _ in range(N)]
            visit[i][j] = True

            S = 2
            check(Q, visit)
    print('#{} {}'.format(test_case, max_num))