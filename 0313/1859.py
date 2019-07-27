import sys

sys.stdin = open('1859.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    X = list(map(int, input().split()))

    result = 0

    while X:
        max_num = X[0]
        max_idx = 0
        temp = 0
        for i in range(len(X)):
            if X[i] > max_num:
                max_num = X[i]
                max_idx = i

        for i in range(max_idx):
            temp += X[i]


        if max_idx != 0:
            result += X[max_idx]*(max_idx) - temp
        else:
            pass

        X = X[max_idx+1:]
    print('#{} {}'.format(test_case, result))