import sys

sys.stdin = open('4871.txt', 'r')

T = int(input())
def DFS(a, b):
    visit = [False for _ in range(V+1)]
    S = []
    v = a
    visit[v] = True
    S += [v]
    while len(S) > 0:
        for w in G[v]:
            if visit[w] == False:
                visit[w] = True
                S += [w]
                if w == b:
                    return 1
                v = w
                break
        else:
            v = S.pop(-1)
    return 0




for test_case in range(1, T+1):
    V, E = map(int, input().split())  # 정점 수, 간선수
    G = [[] for _ in range(V+1)]
    for i in range(E):
        A, B = map(int, input().split())
        G[A] += [B]
    C, D = map(int, input().split())
    print(f'#{test_case} {DFS(C, D)}')