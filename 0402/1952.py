import sys

sys.stdin = open('1952.txt')


def check(n, cnt, result):
    global min_num
    if result > min_num:
        return
    if cnt >= n:
        min_num = min(min_num, result)
        return
    for i in range(3):
        if i == 0:
            if sc[cnt]:
                check(n, cnt+1, result+d*sc[cnt])
            else:
                check(n, cnt+1, result)
        elif i == 1:
            if sc[cnt]:
                check(n, cnt+1, result+m)
            else:
                check(n, cnt+1, result)
        elif i == 2:
            if sc[cnt]:
                check(n, cnt+3, result+mmm)
            else:
                check(n, cnt+1, result)

T = int(input())

for t in range(1, T+1):
    d, m, mmm, y = map(int, input().split())

    sc = list(map(int, input().split()))
    print(sc)
    yo = [0] * 12

    min_num = y

    check(12, 0, 0)

    print('#{} {}'.format(t, min_num))
