

def check(i, j, used = False):
    global max_num
    visit[i][j] = True
    route = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for k in route:
        a, b = i + k[0], j + k[1]
        if a >= 0 and b >= 0 and a <= N-1 and b <= N-1 and not visit[a][b]:
            if X[a][b] < stack[-1]:
                stack.append(X[a][b])
                if len(stack) > max_num:
                    max_num = len(stack)
                if used == False:
                    check(a, b, False)
                else:
                    check(a, b, True)
                stack.pop()
            else:
                if used == False:
                    if stack[-1] > X[a][b]-K:
                        stack.append(X[i][j]-1)
                        if len(stack) > max_num:
                            max_num = len(stack)
                        check(a, b, True)
                        stack.pop()
            # hint: 하나만 낮게. i,j좌표에 있는 값보다 a,b의 값이 하나만 작게.
            # 그냥 조건에서 벗어나는 처음의 경우는 무시하고 스택을 뽑도록.
    visit[i][j] = False


import sys

sys.stdin = open('1949.txt')

T = int(input())


for test_case in range(1, T+1):
    N, K = map(int, input().split())

    X = []

    for _ in range(N):
        X.append(list(map(int, input().split())))

    visit = [[False]*N for _ in range(N)]

    H = []
    temp = 0
    for i in X:
        for j in i:
            if j > temp:
                temp = j
    for i in range(N):
        for j in range(N):
            if X[i][j] == temp:
                H.append([i, j])

    max_num = 0

    for i in H:
        stack = []
        stack.append(X[i[0]][i[1]])
        check(i[0], i[1])
    print('#{} {}'.format(test_case, max_num))

