import sys

sys.stdin = open('B2304.txt')

N = int(input())

X = []

for _ in range(N):
    X.append(list(map(int, input().split())))

max_h = X[0][1]

for i in X:
    if i[1] > max_h:
        max_h = i[1]

for i in range(len(X)-1):
    for j in range(i+1, len(X)):
        if X[i][0] > X[j][0]:
            X[i], X[j] = X[j], X[i]

now = X[0]

temp = []

for i in X:
    if i[1] == max_h:
        temp.append((max_h-now[1])*(i[0]-now[0]))
        break
    if i[1] > now[1]:
        temp.append((max_h-now[1])*(i[0]-now[0]))
        now = i

X.reverse()

now = X[0]

for i in X:
    if i[1] == max_h:
        temp.append((max_h-now[1])*(-i[0]+now[0]))
        break
    if i[1] > now[1]:
        temp.append((max_h-now[1])*(now[0]-i[0]))
        now = i



print((X[0][0]+1-X[-1][0])*max_h-sum(temp))



