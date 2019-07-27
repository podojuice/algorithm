import sys

sys.stdin = open('1974.txt')

T = int(input())

for test_case in range(1, T+1):

    X = []

    for _ in range(9):
        X.append(list(map(int, input().split())))

    result = 1

    for i in range(9):
        visit = [False] * 11
        if result == 1:
            for j in range(9):
                if visit[X[i][j]]:
                    result = 0
                    break
                else:
                    visit[X[i][j]] = True

    if result == 1:
        for i in range(9):
            if result == 0:
                break
            visit = [False] * 11
            for j in range(9):
                if visit[X[j][i]]:
                    result = 0
                    break
                else:
                    visit[X[j][i]] = True


    if result == 1:
        temp = 0
        result = 0
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                visit = [False] * 11
                for k in range(3):
                    for v in range(3):
                        if visit[X[i+k][j+v]]:
                            temp = 1
                            break
                        else:
                            visit[X[i+k][j+v]] = True

                    if temp:
                        break
                if temp:
                    break
            if temp:
                break
        else:
            result = 1

    print('#{} {}'.format(test_case, result))


