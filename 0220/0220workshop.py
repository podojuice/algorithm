import sys

sys.stdin = open('GNS_test_input.txt', 'r')

T = int(input())
number_set = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
for test_case in range(1, T+1):
    N = list(map(str, input().split()))
    X = list(map(str, input().split()))

    result = [0]*10

    for i in X:
        if i == 'ZRO':
            result[0] += 1
        elif i == 'ONE':
            result[1] += 1
        elif i == 'TWO':
            result[2] += 1
        elif i == 'THR':
            result[3] += 1
        elif i == 'FOR':
            result[4] += 1
        elif i == 'FIV':
            result[5] += 1
        elif i == 'SIX':
            result[6] += 1
        elif i == 'SVN':
            result[7] += 1
        elif i == 'EGT':
            result[8] += 1
        elif i == 'NIN':
            result[9] += 1

    temp =''
    for i in range(len(result)):
        temp += (' '+number_set[i])*result[i]

    print(f'{N[0]}{temp}')

