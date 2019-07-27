import sys

sys.stdin = open('workshop.txt')


def check(i, j):
    while X[i+1][j] != 0:
        i += 1
    while X[i][j+1] != 0:
        j += 1
    dt = [i, j]
    return dt


T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    X = []
    visit = [[False]*N for _ in range(N)]

    for _ in range(N):
        X.append(list(map(int, input().split())))

    result = []
    cnt = 0
    for i in range(N):
        for j in range(N):
            if X[i][j] != 0 and not visit[i][j]:
                dt = check(i, j)
                cnt += 1
                x, y = dt[0]+1, dt[1]+1
                for k in range(i, x):
                    for p in range(j, y):
                        visit[k][p] = True
                result.append([x - i, y - j])

    result_sort = []

    for j in range(len(result)):
        min_s = [result[0][0], result[0][1]]
        min_idx = 0
        for i in range(len(result)):
            if result[i][0]*result[i][1] < min_s[0]*min_s[1]:
                min_s = [result[i][0],result[i][1]]
                min_idx = i
            elif result[i][0]*result[i][1] == min_s[0]*min_s[1]:
                if result[i][0] < min_s[0]:
                    min_s = [result[i][0], result[i][1]]
                    min_idx = i
        result_sort.append(min_s)
        result.pop(min_idx)

    print('#{} {}'.format(test_case, cnt), end=' ')
    for i in range(len(result_sort)):
        for j in range(2):
            print(result_sort[i][j], end=' ')
    print()