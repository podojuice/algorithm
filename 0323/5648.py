import sys

sys.stdin = open('5648.txt')


# 터질 가능성 있는 애들 모으는 함수
def po():
    for i in range(len(X)-1):
        for j in range(1+i, len(X)):
            a, b = X[i][0]-X[j][0], X[i][1]-X[j][1]
            dt1, dt2 = X[i][2], X[j][2]

            # 가로 세로에 대해
            if a == 0:
                if b > 0:
                    if dt1 == 1 and dt2 == 0:
                        crash.append([i, j, abs(b)/2])
                else:
                    if dt1 == 0 and dt2 == 1:
                        crash.append([i, j, abs(b)/2])
            elif b == 0:
                if a > 0:
                    if dt1 == 2 and dt2 == 3:
                        crash.append([i, j, abs(a)/2])
                else:
                    if dt1 == 3 and dt2 == 2:
                        crash.append([i, j, abs(a)/2])

            # 대각에 대해
            elif a/b == -1:
                if a < 0:
                    if (dt2 == 0 and dt1 == 3) or (dt2 == 2 and dt1 == 1):
                        crash.append([i, j, abs(a)])
                else:
                    if (dt1 == 0 and dt2 == 3) or (dt1 == 2 and dt2 == 1):
                        crash.append([i, j, abs(a)])
            elif a/b == 1:
                if a > 0:
                    if (dt2 == 0 and dt1 == 2) or (dt2 == 3 and dt1 == 1):
                        crash.append([i, j, abs(a)])
                else:
                    if (dt1 == 0 and dt2 == 2) or (dt1 == 3 and dt2 == 1):
                        crash.append([i, j, abs(a)])

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    X = []

    for _ in range(N):
        X.append(list(map(int, input().split())))

    crash = []
    po()

    # 위에서 부딪힐 가능성이 있는 친구들을 crash에 모음.
    # crash에는 터질애의 인덱스 두 개와 만나는 시간이 담겨 있음.
    result = 0

    # 이제 부딪힐 가능성이 있는 애들 중 가장 빨리 만나는 애들 순으로 조질거임.
    # print(crash)
    # 가장 빨리 만나는 애들 찾고,
    while crash:
        min_num = crash[0][2]
        for i in range(len(crash)):
            if crash[i][2] < min_num:
                min_num = crash[i][2]
        temp = []
        # 동시에 만나는 애들도 있을테니 걔넬 찾아서 temp에 저장해준뒤, pop해줌.
        i = 0
        while i < len(crash):
            if crash[i][2] == min_num:
                # 이미 터진놈은 False가 되어 있음. 그니까 pass
                if X[crash[i][0]] and X[crash[i][1]]:
                    for j in range(2):
                        if crash[i][j] not in temp:
                            temp.append(crash[i][j])
                crash.pop(i)
                i -= 1
            i += 1
        # print(temp)
        for i in temp:
            if X[i]:
                result += X[i][3]
                # 터진 원자는 False로 바꿔줌.
                X[i] = False
    print('#{} {}'.format(test_case, result))