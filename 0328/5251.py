import sys

sys.stdin = open('5251.txt')

def prim(key):
    Q = []
    Q.append(key)

    while Q:
        now = Q.pop(0)
        for i in range(len(MST[now])):
            if MST[now][i]:
                if not D[i]:
                    D[i] = D[now] + MST[now][i]
                    Q.append(i)
                else:
                    if D[i] > D[now] + MST[now][i]:
                        D[i] = D[now] + MST[now][i]
                        Q.append(i)




T = int(input())

for t in range(1, T+1):
    N, E = map(int, input().split())

    MST = [[0]*(N+1) for _ in range(N+1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        MST[s][e] = w

    D = [0]*(N+1)

    prim(0)

    print('#{} {}'.format(t, D[-1]))
