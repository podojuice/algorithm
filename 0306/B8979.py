import sys

sys.stdin = open('B8979.txt')

N, K = map(int, input().split())
temp = []
for _ in range(N):
    temp.append(list(map(str, input().split())))

X = [[] for _ in range(N)]

for i in temp:
    X[int(i[0])-1] = i

for i in range(len(X)):
    X[i] = X[i][1:]

SM = BM = 0
for i in range(len(X)):
    if len(X[i][1]) > SM:
        SM = len(X[i][1])
    if len(X[i][2]) > BM:
        BM = len(X[i][2])

for i in range(len(X)):
    if len(X[i][1]) < SM:
        X[i][1] = '0'*(SM-len(X[i][1])) + X[i][1]
    if len(X[i][2]) < BM:
        X[i][2] = '0'*(BM-len(X[i][2])) + X[i][2]

for i in range(len(X)):
    X[i] = int(''.join(X[i]))

key = X[K-1]
cnt = 1
for i in X:
    if i > key:
        cnt += 1

print(cnt)