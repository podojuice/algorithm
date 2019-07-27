import sys

sys.stdin = open('2.txt')

def sum_num(row, col1, col2):
    min_sum = 3000
    max_sum = -3000

    temp = 0
    for i in range(row):
        for j in range(col1):
            temp += X[i][j]
    if temp > max_sum:
        max_sum = temp
    if temp < min_sum:
        min_sum = temp

    temp = 0
    for i in range(row):
        for j in range(col1, col2):
            temp += X[i][j]
    if temp > max_sum:
        max_sum = temp
    if temp < min_sum:
        min_sum = temp

    temp = 0
    for i in range(row):
        for j in range(col2, M):
            temp += X[i][j]
    if temp > max_sum:
        max_sum = temp
    if temp < min_sum:
        min_sum = temp

    temp = 0
    for i in range(row, N):
        for j in range(col1):
            temp += X[i][j]
    if temp > max_sum:
        max_sum = temp
    if temp < min_sum:
        min_sum = temp

    temp = 0
    for i in range(row, N):
        for j in range(col1, col2):
            temp += X[i][j]
    if temp > max_sum:
        max_sum = temp
    if temp < min_sum:
        min_sum = temp

    temp = 0
    for i in range(row, N):
        for j in range(col2, M):
            temp += X[i][j]
    if temp > max_sum:
        max_sum = temp
    if temp < min_sum:
        min_sum = temp

    return max_sum - min_sum


T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    X = []

    for _ in range(N):
        X.append(list(map(int, input().split())))
    result = -0xfffffff
    for row in range(1, N):
        for col1 in range(1, M-1):
            for col2 in range(col1+1, M):
                # print(row, col1, col2)
                key = sum_num(row, col1, col2)

                if key > result:
                    result = key

    print('#{} {}'.format(t, result*2))
