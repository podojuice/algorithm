import sys

sys.stdin = open('6190.txt')

T = int(input())



for test_case in range(1, T+1):
    N = int(input())

    X = list(map(int, input().split()))


    real = -1
    for i in range(len(X)):
        for j in range(1, len(X)-i):
            a = str(X[i]*X[i+j])
            if len(a) > 1:
                for k in range(len(a)-1):
                    if a[k] > a[k+1]:
                        break
                else:
                    if real < int(a):
                        real = int(a)

    print('#{} {}'.format(test_case, real))