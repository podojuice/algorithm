import sys

sys.stdin = open('1289.txt')

T = int(input())
for test_case in range(1, T+1):
    X = input()
    temp = ['0']*len(X)
    key = len(temp)
    cnt = 0
    for i in range(key):
        if X[i] != temp[i]:
            temp[i] = X[i]
            cnt += 1
            for j in range(i, key):
                temp[j] = X[i]
    print('#{} {}'.format(test_case, cnt))