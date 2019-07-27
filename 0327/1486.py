import sys

sys.stdin = open('1486.txt')

T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())

    X = list(map(int, input().split()))

    result = 0xffffff

    for i in range(2**len(X)):
        temp = 0
        for j in range(len(X)):
            if i & 1 << j:
                temp += X[j]
                if temp > result:
                    break
        if result > temp >= B:
            result = temp

    print('#{} {}'.format(t, result-B))
