import sys

sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):

    N = int(input())

    X = []

    for _ in range(N):
        X.append(list(map(int, input().split())))

    P = int(input())
    cnt = [0]*(P)
    C = []

    for _ in range(P):
        C.append(int(input()))

    for i in X:
        for j in range(len(C)):
            if C[j] >= i[0] and C[j] <= i[1]:
                cnt[j] += 1
    cnt = list(map(str, cnt))

    print('#{} {}'.format(test_case, ' '.join(cnt)))
