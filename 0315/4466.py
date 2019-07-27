import sys

sys.stdin = open('4466.txt')

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())

    X = list(map(int, input().split()))

    X.sort()

    result = 0

    for i in range(K):
        result += X[-1-i]

    print('#{} {}'.format(test_case, result))