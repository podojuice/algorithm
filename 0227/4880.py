import sys

sys.stdin = open('4880.txt', 'r')

T = int(input())


def quick(X):
    global result
    N = len(X)
    if N <= 2:
        if N == 1:
            return X[0]
        else:
            if X[0][0] == X[1][0] or X[0][0] == 1 and X[1][0] or X[0][0] == 2 and X[1][0] == 1 or X[0][0] == 3 and X[1][0] == 2:
                return X[0]
            else:
                return X[1]
    else:
        a = quick(X[:(1+N)//2])
        b = quick(X[(1 + N) // 2:])
        if a[0] == b[0] or a[0] == 1 and b[0] == 3 or a[0] == 2 and b[0] == 1 or a[0] == 3 and b[0] == 2:
            return a
        else:
            return b


for test_case in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    arr = []
    for i in range(len(X)):
        arr += [[X[i], i+1]]

    result = quick(arr)
    print(f'#{test_case} {result[1]}')
