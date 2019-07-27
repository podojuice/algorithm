import sys

sys.stdin = open('1267.txt', 'r')


def DFS(v):
    visit[v] = True

    for w in G[v]:
        if not visit[w]: DFS(w)
    S.append(v)




for test_case in range(1, 11):
    V, E = map(int, input().split())  # 정점 수, 간선수
    G = [[] for _ in range(V + 1)]
    arr = list(map(int, input().split()))
    indeg = [0] * (V + 1)
    visit = [False] * (V + 1)
    # print(G)
    for i in range(0, E * 2, 2):
        u, v = arr[i], arr[i+1]
        G[u].append(v)
        indeg[v] += 1
    # print(G)
    S = []
    for i in range(1, V + 1):
        if indeg[i] == 0:
            DFS(i)
    S.reverse()
    S = list(map(str, S))
    print(f'#{test_case} {" ".join(S)}')



    # while True:
    #     v = 0
    #     for i in range(1, V + 1):
    #         if not visit[i] and indeg[i] == 0:
    #             v = i
    #             break
    #     if v == 0: break
    #     print(v)
    #     visit[v] = True
    #     for w in G[v]:
    #         if indeg[w]: indeg[w] -= 1
