import sys

sys.stdin = open('4130.txt')


def check(num, dt):

    if dt == 1:
        if not used[num]:
            M[num] = [M[num][7]] + M[num][:7]
            used[num] = True
            for i in G[num]:
                check(i, dt*(-1))
    else:
        if not used[num]:
            M[num] = M[num][1:] + [M[num][0]]
            used[num] = True
            for i in G[num]:
                check(i, dt*(-1))

T = int(input())
for t in range(1, T+1):
    K = int(input())

    M = []

    for _ in range(4):
        M.append(list(map(int, input().split())))

    spin = []

    for _ in range(K):
        spin.append(list(map(int, input().split())))

    # N = 0 S = 1

    # 자석 번호, 시계방향 1 반시계 -1

    for j in spin:
        G = [[] for _ in range(4)]
        used = [False]*4
        for i in range(3):
            if M[i][2] != M[i + 1][6]:
                G[i].append(i+1)
                G[i+1].append(i)
        # 스핀에는 자석 번호하고 방향이 적혀있음.

        check(j[0]-1, j[1])

    result = 0
    for i in range(4):
        if M[i][0] == 1:
            result += 2**i

    print('#{} {}'.format(t, result))
