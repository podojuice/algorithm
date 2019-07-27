import sys

sys.stdin = open('2007.txt')

T = int(input())

for test_case in range(1, T+1):
    X = input()
    w = 1
    while 1:
        if X[:w] == X[w:2*w]:
            break
        w += 1

    print('#{} {}'.format(test_case, w))