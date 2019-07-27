import sys

sys.stdin = open('B1463.txt')

from collections import deque



N = int(input())

X = [0]*(N+1)

Q = deque()

Q.append(N)

while Q:
    now = Q.popleft()
    temp = []
    if now-1 > 0 and not X[now-1]:
        X[now-1] = X[now]+1
        Q.append(now-1)
    if now%2 == 0 and now//2 > 0 and not X[now//2]:
        X[now//2] = X[now]+1
        Q.append(now//2)
    if now%3 == 0 and now//3 > 0 and not X[now//3]:
        X[now//3] = X[now]+1
        Q.append(now//3)

print(X[1])