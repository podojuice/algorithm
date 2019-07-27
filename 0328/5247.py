import sys

sys.stdin = open('5247.txt')

from collections import deque



def BFS(key):
    while Q:
        now = Q.popleft()
        if 1000000 >= now + 1:
            if not D[now + 1]:
                D[now + 1] = D[now] + 1
                Q.append(now+1)
        if now-1> 0:
            if not D[now-1]:
                D[now-1] = D[now] + 1
                Q.append(now-1)

        if now*2 <= 1000000:
            if not D[now*2]:
                D[now*2] = D[now]+1
                Q.append(now*2)
        if now-1 > 0 :
            if not D[now - 10]:
                D[now - 10] = D[now]+1
                Q.append(now-10)

        if D[key]:
            return D[key]



T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())

    D = [0]*1000001

    Q = deque()

    Q.append(N)

    print('#{} {}'.format(t, BFS(M)))

