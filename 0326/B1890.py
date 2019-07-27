import sys

sys.stdin = open('B1890.txt')

N = int(input())

X = []

result = [[0]*N for _ in range(N)]

for _ in range(N):
    X.append(list(map(int, input().split())))

result[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            break
        if result[i][j]:
            if i+X[i][j] < N:
                result[i+X[i][j]][j] += result[i][j]
            if j+X[i][j] < N:
                result[i][j+X[i][j]] += result[i][j]
print(result[N-1][N-1])