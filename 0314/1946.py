import sys

sys.stdin = open('1946.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    result = []

    for _ in range(N):
        C, K = map(str, input().split())
        result += [C]*int(K)

    print('#{}'.format(test_case))
    for i in range(1, len(result)+1):
        if i % 10 == 0:
            print(result[i-1], end='')
            print()
        else:
            print(result[i - 1], end='')
    print()