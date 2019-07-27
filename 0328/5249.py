import sys

sys.stdin = open('5249.txt')


def prim(key):
    global cnt
    while cnt < V:
        min_num = 11
        idx = 0
        for i in range(V+1):
            if MST[key][i] and not used[i]:
                if D[i] > MST[key][i]:
                    D[i] = MST[key][i]
                if min_num > D[i]:
                    min_num = D[i]
                    idx = i
        cnt += 1
        used[key] = True
        key = idx


T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())

    MST = [[0]*(V+1) for _ in range(V+1)]

    used = [False]*(V+1)

    D = [0xfffff for _ in range(V+1)]
    D[0] = 0

    for _ in range(E):
        u, v, w = map(int, input().split())
        MST[u][v] = w
        MST[v][u] = w

    cnt = 0

    prim(0)

    result = 0
    for i in range(len(D)):
        result += D[i]
    print('#{} {}'.format(t, result))


