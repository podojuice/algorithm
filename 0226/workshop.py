import sys
sys.stdin = open('workshop.txt', 'r')
for test_case in range(1, 11):
    N = int(input())
    X = []
    for i in range(N):
        X += [list(map(int, input().split()))]
    cnt = 0

    for i in range(100):
        stack = []
        for j in range(100):
            if X[j][i] != 0:
                stack += [X[j][i]]
        for j in range(len(stack)-1):
            if stack[j] == 1 and stack[j + 1] == 2:
                cnt += 1

    print(cnt)

