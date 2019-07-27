import sys

sys.stdin = open('5653.txt')

def check():
    global Q

    Q_new = []
    route = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for i in Q:
        maps[i[0]][i[1]][1] += 1
        H = maps[i[0]][i[1]][0]
        T = maps[i[0]][i[1]][1]
        if H+1 == T:
            for k in route:
                a, b = i[0]+k[0], i[1]+k[1]
                if maps[a][b] == 0:
                    Q_new.append([a, b, H])

    temp = 0
    while temp < len(Q):
        i = Q[temp]
        H = maps[i[0]][i[1]][0]
        T = maps[i[0]][i[1]][1]
        if H * 2 == T:
            Q.pop(temp)
            temp -= 1
        temp += 1
    temp = 0
    while temp < len(Q_new):
        for j in range(temp+1, len(Q_new)):
            if Q_new[temp][0] == Q_new[j][0] and Q_new[temp][1] == Q_new[j][1]:
                if Q_new[temp][2] < Q_new[j][2]:
                    Q_new[temp][2] = Q_new[j][2]
                Q_new.pop(j)
                temp -=1
                break
        temp += 1
    for i in Q_new:
        maps[i[0]][i[1]] = [i[2], 0]
        Q.append([i[0], i[1]])



T = int(input())
for test_case in range(1, 6):
    N, M, K = map(int, input().split())

    X = []
    R, C = N + 2*K, M + 2*K
    maps = [[0]*C for _ in range(R)]

    Q = []


    for i in range(N):
        X = list(map(int, input().split()))
        for j in range(M):
            if X[j] != 0:
                maps[K+i][K+j] = [X[j], 0]
                Q.append([K+i, K+j])


    for _ in range(K):
        check()

    print('#{} {}'.format(test_case, len(Q)))



