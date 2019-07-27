import sys

sys.stdin = open('1.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    M, P = map(int, input().split())

    X = []

    for _ in range(M):
        X.append(list(map(int, input().split())))
    max_num = 0
    for i in range(M-P+1):
        for j in range(M-P+1):
            temp = 0
            for x in range(P):
                for y in range(P):
                    temp += X[i+x][j+y]
            if temp >= max_num:
                max_num = temp

    print('#{} {}'.format(test_case, max_num))