import sys

sys.stdin = open('6057.txt')

def tri(node, key, t = 0):
    global cnt
    if t == 3:
        # 3번째면 검증.
        if node == key:
            cnt += 1
            return
        else:
            return

    for i in G[node]:
        if visit[i] == False:
            visit[i] = True
            tri(i, key, t+1)
            visit[i] = False

T = int(input())

for test_case in range(1, T+1):

    N, M = map(int, input().split())

    G = [[] for _ in range(N+1)]

    visit = [False]*(N+1)

    nodes = []

    for _ in range(M):
        u, v = map(int, input().split())
        G[u] += [v]
        if u not in nodes:
            nodes += [u]
        if v not in nodes:
            nodes += [v]
        G[v] += [u]

    cnt = 0

    for node in nodes:
        visit = [False] * (N + 1)
        tri(node, node)

    print('#{} {}'.format(test_case, cnt//6))