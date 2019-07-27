import sys

sys.stdin = open('5250.txt')


def di(Q):
    route = [[1,0], [-1,0], [0,1], [0,-1]]
    while Q:
        now = Q.pop(0)
        for i in route:
            a, b = now[0]+i[0], now[1]+i[1]

            if 0 <= a < N and 0 <= b < N and not (a == 0 and b == 0):
                if not result[a][b]: # 앞으로 갈 곳이 0일때, 새로 방문하는 곳일 때.
                    if X[a][b] > X[now[0]][now[1]]:
                        result[a][b] = result[now[0]][now[1]] + 1 + X[a][b]-X[now[0]][now[1]]
                        Q.append([a, b])
                    else:
                        result[a][b] = result[now[0]][now[1]] + 1
                        Q.append([a, b])
                else:
                    if X[a][b] > X[now[0]][now[1]]:
                        if result[a][b] > result[now[0]][now[1]] + 1 + X[a][b]-X[now[0]][now[1]]:
                            result[a][b] = result[now[0]][now[1]] + 1 + X[a][b]-X[now[0]][now[1]]
                            Q.append([a, b])
                    else:
                        if result[a][b] > result[now[0]][now[1]] + 1:
                            result[a][b] = result[now[0]][now[1]] + 1
                            Q.append([a, b])


T = int(input())

for t in range(1, T+1):
    N = int(input())

    X = []

    for _ in range(N):
        X.append(list(map(int, input().split())))

    result = [[0]*N for _ in range(N)]



    Q = [[0, 0]]

    di(Q)
    # print(result)
    print('#{} {}'.format(t, result[N-1][N-1]))
