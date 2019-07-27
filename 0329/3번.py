import sys

sys.stdin = open('3.txt')

def check(k, n, ans):
    global min_num
    if k == n:
        min_num = ans
        return

    for i in range(N):
        if not used[i]:
            used[i] = True
            key = abs(s_list[i][0] - r_list[k][0]) + abs(s_list[i][1] - r_list[k][1])
            if ans + key < min_num:
                check(k+1, n, ans+key)
            used[i] = False


T = int(input())

for t in range(1, T+1):
    N = int(input())

    S = list(map(int, input().split()))

    R = list(map(int, input().split()))

    s_list = []
    r_list = []

    for j in range(N):
        x, y = j*2, j*2+1
        s_list.append([S[x], S[y]])
        r_list.append([R[x], R[y]])

    used = [False]*N

    min_num = 0xffffff
    ans = 0
    check(0, N, ans)

    print('#{} {}'.format(t, min_num))



