import sys

sys.stdin = open('2805.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    X = []

    for _ in range(N):
        X.append(str(input()))

    key = N//2
    result = 0
    for i in range(N):
        temp = abs(key-i)
        if temp:
            for j in range(temp, N-temp):
                print(i, j)
                result += int(X[i][j])
        else:
            for j in X[i]:

                result += int(j)

    print('#{} {}'.format(test_case, result))