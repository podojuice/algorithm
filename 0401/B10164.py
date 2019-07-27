import sys

sys.stdin = open('B10164.txt')

N, M, K = map(int, input().split())

X = [[0]*M for _ in range(N)]

visit = [[0]*M for _ in range(N)]

cnt = 1

key = False

for i in range(N):
    for j in range(M):
        if i == 0 or j == 0:
            visit[i][j] = 1
        if cnt == K:
            key = [i, j]
        X[i][j] = cnt
        cnt += 1

for i in range(N):
    for j in range(M):
        if not visit[i][j]:
            visit[i][j] = visit[i-1][j] + visit[i][j-1]

if not key:
    print(visit[N-1][M-1])
else:
    ans1 = visit[key[0]][key[1]]
    ans2 = visit[N-1-key[0]][M-1-key[1]]
    print(ans1*ans2)




