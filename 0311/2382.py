import sys

sys.stdin = open('2382.txt')


def check():
    global dt

    for i in dt:
        if i[3] == 1:
            i[0], i[1] = i[0] - 1, i[1]
        elif i[3] == 2:
            i[0], i[1] = i[0] + 1, i[1]
        elif i[3] == 3:
            i[0], i[1] = i[0], i[1] - 1
        elif i[3] == 4:
            i[0], i[1] = i[0], i[1] + 1

        if i[0] == 0 or i[0] == N-1 or i[1] == 0 or i[1] == N-1:
            i[2] = i[2]//2
            if i[3] == 1:
                i[3] = 2
            elif i[3] == 2:
                i[3] = 1
            elif i[3] == 3:
                i[3] = 4
            elif i[3] == 4:
                i[3] = 3

    for i in range(len(dt)-1):
        temp = [[i, dt[i][2]]]
        for j in range(1+i, len(dt)):

            if dt[i][0] == dt[j][0] and dt[i][1] == dt[j][1]:
                temp.append([j, dt[j][2]])
        if len(temp) > 1:
            temp_max = temp[0][1]
            temp_idx = temp[0][0]
            for k in range(len(temp)):
                if temp_max < temp[k][1]:
                    temp_max = temp[k][1]
                    temp_idx = temp[k][0]
            for k in range(1, len(temp)):
                dt[i][2] += temp[k][1]
                dt[temp[k][0]][0] = -1
            dt[i][3] = dt[temp_idx][3]
            # print(dt)
    w = 0
    while w < len(dt):
        if dt[w][0] == -1 or dt[w][2] == 0:
            dt.pop(w)
            w -= 1

        w += 1






T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())


    # 1, 2, 3, 4 상 하 좌 우

    dt = []

    for _ in range(K):
        x, y, v, d = map(int, input().split())
        dt.append([x, y, v, d])

    for _ in range(M):
        check()
    result = 0
    for i in dt:
        result += i[2]

    print('#{} {}'.format(test_case, result))
