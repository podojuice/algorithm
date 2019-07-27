import sys

sys.stdin = open('5201.txt')

T = int(input())

for t in range(1, T+1):

    N, M = map(int, input().split())

    bur = sorted(list(map(int, input().split())))

    truck = sorted(list(map(int, input().split())))

    ans = 0

    used = [False]*N

    for i in range(M):
        for j in range(N):
            if truck[-1-i] >= bur[-1-j] and not used[-1-j]:
                used[-1-j] = True
                ans += bur[-1-j]
                break

    print('#{} {}'.format(t, ans))