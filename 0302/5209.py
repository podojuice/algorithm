import sys

sys.stdin = open('5209.txt', 'r')

T = int(input())

def perm(k, n):
    global min_num
    if k == n:
        num = 0
        for i in order:
            num += i
        if min_num > num:
            min_num = num

    else:
        for i in range(n):
            if visit[i]: continue
            visit[i] = True
            order.append(X[k][i])
            # num = 0
            # for j in order:
            #     num += j
            # if min_num > num:
            perm(k+1, n)
            visit[i] = False
            order.pop()


for test_case in range(1, T+1):
    N = int(input())
    X = []
    for i in range(N):
        X += [list(map(int, input().split()))]
    min_num = 0
    for i in range(len(X)):
        min_num += X[i][i]
    visit = [False]*N
    order = []
    perm(0, N)
    print(f'#{test_case} {min_num}')