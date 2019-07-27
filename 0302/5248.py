import sys

sys.stdin = open('5248.txt', 'r')

T = int(input())


def DFS(start):
    global cnt
    S = []
    v = start
    visit[v] = True
    if G[v]:
        S.append(v)
        while len(S) > 0:
            # v의 방문하지 않은 인접 정점을 찾는다.
            for w in G[v]:
                if not visit[w]:
                    visit[w] = True
                    S.append(v)
                    print(S)
                    v = w
                    break
            else:
                v = S.pop(-1)
    cnt += 1


for test_case in range(1, T+1):
    V, E = map(int, input().split())
    X = list(map(int, input().split()))
    G = [[] for _ in range(V + 1)]
    visit = [False for _ in range(V + 1)]
    visit[0]=True
    cnt = 0
    for i in range(E):
        G[X[2*i]] += [X[2*i+1]]
        G[X[2*i+1]] += [X[2*i]]
    for i in range(len(visit)):
        if not visit[i]:
            DFS(i)
    print(f'#{test_case} {cnt}')
