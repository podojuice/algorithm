import sys

sys.stdin = open('5650.txt')


def check(x, y, i, j, dt, cnt):

    global max_num
    if dt == 0:
        now_x, now_y = i, j + 1
    elif dt == 1:
        now_x, now_y = i, j - 1
    elif dt == 2:
        now_x, now_y = i + 1, j
    else:
        now_x, now_y = i - 1, j
    while now_x != x and now_y != y:
        if 0 <= now_x < N and 0 <= now_y < N:
            key = X[now_x][now_y]
            if now_x == x and now_y == y:
                max_num = max(max_num, cnt)
                break
            elif key == -1:
                max_num = max(max_num, cnt)
                break

            elif key == 0:
                if now_x == 0 and dt == 3:

                    check(x, y, now_x, now_y, 2, cnt + 1)
                elif now_x == N-1 and dt == 2:
                    check(x, y, now_x, now_y, 3, cnt + 1)
                elif now_y == 0 and dt == 1:
                    check(x, y, now_x, now_y, 0, cnt + 1)
                elif now_y == N-1 and dt == 0:
                    check(x, y, now_x, now_y, 1, cnt + 1)
                else:
                    check(x, y, now_x, now_y, dt, cnt)
            elif 6 <= key <= 10:
                for h in warm[key-6]:
                    if h != [now_x, now_y]:
                        check(x, y, h[0], h[1], dt, cnt)

            elif key == 1:
                if dt == 0:
                    check(x, y, now_x, now_y, 1, cnt + 1)
                elif dt == 1:
                    check(x, y, now_x, now_y, 3, cnt + 1)
                elif dt == 2:
                    check(x, y, now_x, now_y, 0, cnt + 1)
                elif dt == 3:
                    check(x, y, now_x, now_y, 2, cnt + 1)

            elif key == 2:
                if dt == 0:
                    check(x, y, now_x, now_y, 1, cnt + 1)
                elif dt == 1:
                    check(x, y, now_x, now_y, 2, cnt + 1)
                elif dt == 2:
                    check(x, y, now_x, now_y, 3, cnt + 1)
                elif dt == 3:
                    check(x, y, now_x, now_y, 0, cnt + 1)

            elif key == 3:
                if dt == 0:
                    check(x, y, now_x, now_y, 2, cnt + 1)
                elif dt == 1:
                    check(x, y, now_x, now_y, 0, cnt + 1)
                elif dt == 2:
                    check(x, y, now_x, now_y, 3, cnt + 1)
                elif dt == 3:
                    check(x, y, now_x, now_y, 1, cnt + 1)

            elif key == 4:
                if dt == 0:
                    check(x, y, now_x, now_y, 3, cnt + 1)
                elif dt == 1:
                    check(x, y, now_x, now_y, 0, cnt + 1)
                elif dt == 2:
                    check(x, y, now_x, now_y, 1, cnt + 1)
                elif dt == 3:
                    check(x, y, now_x, now_y, 2, cnt + 1)

            elif key == 5:
                if dt == 0:
                    check(x, y, now_x, now_y, 1, cnt + 1)
                elif dt == 1:
                    check(x, y, now_x, now_y, 0, cnt + 1)
                elif dt == 2:
                    check(x, y, now_x, now_y, 3, cnt + 1)
                elif dt == 3:
                    check(x, y, now_x, now_y, 2, cnt + 1)


T = int(input())
for t in range(1, 3):
    N = int(input())

    X = []

    for _ in range(N):
        X.append(list(map(int, input().split())))

    warm = [[] for _ in range(5)]

    for i in range(N):
        for j in range(N):
            key = X[i][j]
            if key > 5:
                warm[key-6].append([i, j])
    max_num = 0
    for i in range(N):
        for j in range(N):
            if X[i][j] == 0:
                for k in range(4):
                    check(i, j, i, j, k, 0)

                    # 방향 0 = 동 1 = 서 2 = 남 3 = 북으로 가정.
    print(warm)
    print('#{} {}'.format(t, max_num))

