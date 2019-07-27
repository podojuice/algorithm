import sys

sys.stdin = open('5186.txt')

T = int(input())
for test_case in range(1, T+1):
    N = float(input())

    result=''
    for i in range(1, 13):
        if not N:
            break
        if N >= 2**-i:
            N -= 2**-i
            result += '1'
        else:
            result += '0'

    if N:
        print('#{} overflow'.format(test_case))
    else:
        print('#{} {}'.format(test_case, result))
