import sys

sys.stdin = open('baek.txt', 'r')

T = int(input())
for i in range(T):
    C, R = list(map(int, input().split()))
    X = []
    for j in range(R):
        X += [' '.join(input()).split()]
    visit = [[] for i in range(len(X))]
    Q = [[]]

    for j in range(len(X)):
        for k in range(len(X[j])):
            if X[j][k] == '.':
                visit[j] += [0]
            elif X[j][k] == '@':
                visit[j] += [1]
                a, b = j, k
            elif X[j][k] == '*':
                visit[j] += ['|']
                Q += [[j, k]]
            else:
                visit[j] += ['|']

    #길 - 0 사람 - 1 불 - | 벽 - |

    Q[0] = [a, b]
    # print(visit, Q)
    #Q에는 불이 먼저 담겼다. 불이 다 움직이고 사람이 움직일건데, 불이건 벽이건 있으면 못간다. 2차원 배열의 0번째 열, 행, 혹은 마지막 열, 마지막 행에 사람이 도달하면 탈출.
    def DFS(Q):
        global result
        route = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while Q:
            now = Q.pop(0)
            if type(visit[now[0]][now[1]]) == int:
                for i in route:
                    a, b = now[0]+i[0], now[1]+i[1]
                    if visit[a][b] == 0:
                        visit[a][b] = visit[now[0]][now[1]] + 1
                        Q.append([a,b])
                        if a == 0 or b == 0 or a == len(visit)-1 or b == len(visit[0])-1:
                            result = visit[a][b]
                            Q = []
                            break
            else:
                for i in route:
                    a, b = now[0] + i[0], now[1] + i[1]
                    if a >= 0 and b >= 0 and a < len(visit) and b < len(visit[0]):
                        if type(visit[a][b]) == int:
                            visit[a][b] = '|'
                            Q.append([a, b])


    result = 'IMPOSSIBLE'
    DFS(Q)
    print(result)


