import sys

sys.stdin = open('DFS_input.txt')

def DFS(start):
    visit = [False for _ in range(V+1)]
    S = []
    v = start
    visit[v] = True
    print(v, end=' ')
    S.append(v)
    # print(S)
    while len(S) > 0:
        # v의 방문하지 않은 인접 정점을 찾는다.
        for w in G[v]:
            if not visit[w]:
                visit[w] = True
                print(w, end=' ')
                S.append(v)
                # print(S)
                v = w
                break
        else:
            v = S.pop(-1)


V, E = map(int, input().split()) # 정점 수, 간선수

G = [[] for _ in range(V + 1)]

for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

print(G)

DFS(1)