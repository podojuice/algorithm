import sys

sys.stdin = open('B3.txt')

N, M = map(int, input().split())

X = []

for i in range(N):
    X.append(list(map(int, input().split())))

route = [[1, 0], [-1, 0], [0, 1], [0, -1]]
temp = []
for i in range(len(X)):
    for j in range(len(X[i])):
        if X[i][j] == 1:
            temp.append([i, j])

while temp:
    for i in range(len(temp)):
        for j in range(len(route)):
            a = temp[i][0]+route[j][0]
            b = temp[i][1]+route[j][1]
            if X[a][b] == 0:
                while a != 0 or a != N or b != 0 or b != M:
                    for k in range(len(route)):
