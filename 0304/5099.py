import sys

sys.stdin = open('5099.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    H, P = list(map(int, input().split()))
    X = list(map(int, input().split()))
    temp = []
    for i in range(len(X)):
        temp += [[X[i], i+1]]
    Q =[]
    for i in range(H):
        Q.append(temp.pop(0))

    while len(Q) > 1:
        while Q[0][0]//2 != 0:
            Q[0][0] //= 2
            Q.append(Q.pop(0))
        Q.pop(0)
        if not len(Q) == 1:
            if temp:
                Q.append(temp.pop(0))

    print(Q[0][1])