import sys

sys.stdin = open('sample_input4.txt', 'r')

T = int(input())

for test in range(1, T+1):
    N = list(map(int, input().split()))
    X = list(map(int, input().split()))

    result = []
    for i in range(len(X)-N[1]+1):
        a=0
        for j in range(N[1]):
            a += X[i+j]
        result += [a]
    maxnum = result[0]
    for i in result:
        if i >= maxnum:
            maxnum = i
    minnum = result[0]
    for i in result:
        if i <= minnum:
            minnum = i

    print(maxnum - minnum)
