import sys

sys.stdin = open('5189.txt')

def perm(k, n, temp = []):
    global result
    if k == n:
        a = [1]
        for i in temp:
            a.append(i)
        a.append(1)
        result.append(a)
    for i in range(2, N+1):
        if not used[i]:
            used[i] = True
            temp.append(i)
            perm(k+1, n, temp)
            used[i] = False
            temp.pop()

def check(x):
    global ans
    cnt = 0

    for p in range(len(x)-1):

        cnt += X[x[p]-1][x[p+1]-1]
    ans = min(ans, cnt)


T = int(input())

for t in range(1, T+1):
    N = int(input())


    X = []

    for _ in range(N):
        X.append(list(map(int, input().split())))

    # i = 출발 j = 도착

    used = [False]*(N+1)
    used[0] = True
    used[1] = True

    result = []
    perm(0, N-1)
    ans = 0xffffff
    for i in result:
        check(i)

    print('#{} {}'.format(t, ans))
