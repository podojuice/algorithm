import sys

sys.stdin = open('4111.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())

    K = int(input())

    X = sorted(list(map(int, input().split())))

    d = []

    for i in range(N-1):
        d.append(X[i+1]-X[i])

    d = sorted(d)

    print('#{} {}'.format(t, sum(d[:-K+1])))