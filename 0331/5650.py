import sys

sys.stdin = open('5650.txt')

def check(x, y):
    pass


T = int(input())

N = int(input())

X = []

for _ in range(N):
    X.append(list(map(int, input().split())))

print(X)

# 1은 왼쪽 아래. 2는 왼쪽 위. 3은 오른쪽 위. 4는 오른쪽아래. 5는 네모. 6~10은 웜홀. -1는 블랙홀

warm = [[] for _ in range(5)]
for i in range(N):
    for j in range(N):
        key = X[i][j]
        if key > 5:
            warm[key-6].append([i, j])

for i in range(N):
    for j in range(N):
        if X[i][j] == 0:
            check(i, j)
