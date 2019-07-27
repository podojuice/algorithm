import sys

sys.stdin = open('5185.txt')

T = int(input())

for test_case in range(1, T+1):

    N, X = input().split()

    result = ''

    for i in range(int(N)):
        temp = bin(int(X[i], 16))[2:]
        if len(temp) == 0:
            temp = '0000'
        elif len(temp) == 1:
            temp = '000' + temp
        elif len(temp) == 2:
            temp = '00' + temp
        elif len(temp) == 3:
            temp = '0' + temp

        result += temp

    print('#{} {}'.format(test_case, result))