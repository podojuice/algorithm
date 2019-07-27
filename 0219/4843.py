import sys

sys.stdin = open('sample_input4.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))


    for i in range(len(X)-1):
        for j in range(len(X)-i-1):
            if X[i] > X[i+j+1]:
                X[i], X[i+j+1] = X[i+j+1], X[i]

    result =[]
    # print(X[-2])
    temp = 1
    for i in range(5):
        temp *= -1
        result += [X[temp]]
        temp *= -1
        temp += -1
        result += [X[temp]]
        temp += 2

    a = ''
    for x in result:
        a += ' ' +str(x)
    print(f'#{test_case}{a}')