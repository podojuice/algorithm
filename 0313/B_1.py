import sys

sys.stdin = open('B_1.txt')

def DFS(key):
    global cnt
    visit[key] = True
    for i in G[key]:
        if visit[i] == False:
            cnt += 1
            DFS(i)

C = int(input())

N = int(input())

G = [[]for i in range(C+1)]

visit = [False]*(C+1)
for _ in range(N):
    u, v = map(int, input().split())
    G[u] += [v]
    G[v] += [u]
cnt = 0
DFS(1)
print(cnt)