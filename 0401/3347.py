import sys

sys.stdin = open('3347.txt')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())

    C = [0]

    C += list(map(int, input().split()))

    S = [0]

    S += list(map(int, input().split()))

    cnt = [0]*(N+1)

    for i in range(1, M+1):
        for j in range(1, N+1):
            if S[i] >= C[j]:
                cnt[j] += 1
                break
    print('#{} {}'.format(t, cnt.index(max(cnt))))
