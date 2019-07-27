import sys

sys.stdin = open('B2167.txt')

N, M = map(int, input().split())

X = []

for _ in range(N):
    X.append(list(map(int, input().split())))

K = int(input())

for _ in range(K):
    now = list(map(int, input().split()))
    result = 0
    for i in range(now[0]-1, now[2]):
        for j in range(now[1]-1, now[3]):
            result += X[i][j]
    print(result)