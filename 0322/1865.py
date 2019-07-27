import sys

sys.stdin = open('1865.txt')

def check(cnt, per):
    global result
    if cnt == N:
        result = per
        return
    for i in range(N):
        if not used[i]:
            temp = per*(X[cnt][i]/100)
            if temp <= result:
                continue
            used[i] = True
            check(cnt+1, temp)
            used[i] = False


T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    X = []

    for _ in range(N):
        X.append(list(map(int, input().split())))

    used = [False]*N

    result = 2
    check(0, 100)
    print('#{}'.format(test_case), end=' ')
    print(format(result, '6f'))


