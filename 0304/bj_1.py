import sys

sys.stdin = open('bj_1.txt', 'r')

def DFS(used, x, y, order):
    global max_num

    route = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    order += [X[x][y]]


    for i in route:
        a, b = x+i[0], y+i[1]
        if a >= 0 and b >= 0 and a < N[0] and b < N[1]:
            if X[a][b] not in used:
                DFS(used + [X[a][b]], a, b, order)
                if order:
                    order.pop()
    if len(order) > max_num:
        max_num = len(order)


N = list(map(int, input().split()))
X = []

for i in range(N[0]):
    X += [' '.join(str(input())).split()]

used = [X[0][0]]

max_num = 0

order = []

DFS(used, 0, 0, order)

print(max_num)