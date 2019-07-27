import sys

sys.stdin = open('4881.txt', 'r')


T = int(input())


def perm(k, n):
    global min_num
    if k == n:
        num = 0
        for i in order:
            num += i
        if num < min_num:
            min_num = num
        return
    for i in range(n):
        if used[i]: continue
        used[i] = True
        order.append(X[k][i])
        perm(k + 1, n)
        used[i] = False
        order.pop()


for test_case in range(1, T+1):
    N = int(input())
    X = []
    for i in range(N):
        X += [list(map(int, input().split()))]
    order = []  # 순열 저장
    used = [False] * N  # 사용된 요소들 정보
    min_num = 100
    perm(0, N)
    print(f'#{test_case} {min_num}')

