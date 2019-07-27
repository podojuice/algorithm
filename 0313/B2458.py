import sys

sys.stdin = open('B2458.txt')

def DFS(key, a):
    global cnt
    visit[key] = True
    for i in a[key]:
        if visit[i] == False:
            cnt += 1
            DFS(i, a)


N, M = map(int, input().split())

G1 = [[]for i in range(N+1)]

G2 = [[]for i in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())

    G1[u] += [v]
    G2[v] += [u]
temp = [0]*(N+1)
for i in range(1, N+1):
    cnt = 0
    visit = [False] * (N + 1)
    DFS(i, G1)
    temp[i] += cnt

for i in range(1, N+1):
    cnt = 0
    visit = [False] * (N + 1)
    DFS(i, G2)
    temp[i] += cnt

result = 0
for i in temp:
    if i == (N-1):
        result += 1

print(result)