import sys

sys.stdin = open('5521.txt')

def BFS(key):
    Q = []
    Q.append(key)
    while Q:
        now = Q.pop(0)
        for i in G[now]:
            if D[now]+1 < D[i]:
                D[i] = D[now]+1
                Q.append(i)


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())

    G = [[] for _ in range(N+1)]

    D = [0xfffffff]*(N+1)
    D[1] = 0


    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)


    BFS(1)
    cnt = 0
    for i in range(2, N+1):
        if D[i] <= 2:
            cnt += 1
    print(D, G)
    print('#{} {}'.format(t, cnt))
