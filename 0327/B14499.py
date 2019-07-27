import sys

sys.stdin = open('B14499.txt')

N, M, x, y, K = map(int, input().split())

maps = [[0]*M for _ in range(N)]

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(M):
        maps[i][j] = temp[j]

order = list(map(int, input().split()))

# 도착한 위치 지도 바닥에 쓰여있는 수가 0 --> 주사위의 바닥면이 지도에 복사.
# 0이 아닌 경우 --> 지도 바닥에 쓰여있는 수가 주사위 바닥으로 복사. 지도 바닥은 0.

# 1 동 2 서 3 북 4 남

dice = [0]*7

for i in order:
    if i == 1:
        if y+1 < M:
            y += 1
            if maps[x][y] == 0:
                maps[x][y] = dice[3]
            else:
                dice[3] = maps[x][y]
                maps[x][y] = 0
            print(dice[4])
            dice[3], dice[1], dice[4], dice[6] = dice[1], dice[4], dice[6], dice[3]

    elif i == 2:
        if y-1 >= 0:
            y -= 1
            if maps[x][y] == 0:
                maps[x][y] = dice[4]
            else:
                dice[4] = maps[x][y]
                maps[x][y] = 0
            print(dice[3])
            dice[3], dice[6], dice[4], dice[1] = dice[6], dice[4], dice[1], dice[3]

    elif i == 3:
        if x - 1 >= 0:
            x -= 1
            if maps[x][y] == 0:
                maps[x][y] = dice[2]
            else:
                dice[2] = maps[x][y]
                maps[x][y] = 0
            print(dice[5])
            dice[1], dice[2], dice[6], dice[5] = dice[5], dice[1], dice[2], dice[6]
    elif i == 4:
        if x + 1 < N:
            x += 1
            if maps[x][y] == 0:
                maps[x][y] = dice[5]
            else:
                dice[5] = maps[x][y]
                maps[x][y] = 0
            print(dice[2])
            dice[1], dice[2], dice[6], dice[5] = dice[2], dice[6], dice[5], dice[1]
