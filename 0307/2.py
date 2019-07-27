import sys

sys.stdin = open('2.txt')

T = int(input())
for test_case in range(1, T+1):
    ml = 0
    X = []
    for i in range(5):
        X.append(input())
        if len(X[i]) > ml:
            ml = len(X[i])
    col = [[] for _ in range(ml)]

    for i in range(len(X)):
        for j in range(len(X[i])):
            col[j] += [X[i][j]]
    result = ''
    for i in range(len(col)):
        for j in range(len(col[i])):
            result += col[i][j]
    print('#{} {}'.format(test_case, result))
