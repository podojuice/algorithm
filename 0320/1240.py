import sys

sys.stdin = open('1240.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int,input().split())

    password = [
        '0001101',
        '0011001',
        '0010011',
        '0111101',
        '0100011',
        '0110001',
        '0101111',
        '0111011',
        '0110111',
        '0001011'
    ]


    key = 0
    check = []

    for _ in range(N):
        temp = input()
        if '1' in temp:
            for i in range(len(temp)):
                if temp[-1-i] == '1':
                    result = temp

    for i in range(len(result)):
        if result[-1-i] == '1':
            key = -1-i
            break

    code = result[M+key+1-56:M+key+1]
    for i in range(0, 56, 7):
        for j in range(len(password)):
            if password[j] == code[i:i+7]:
                check.append(j)

    even = 0
    odd = 0

    for i in range(8):
        if i % 2 and i != 7:
            even += check[i]
        elif not i % 2 :
            odd += check[i]
        else:
            last = check[i]

    if (odd*3 + even + last) % 10:
        print('#{} {}'.format(test_case, 0))
    else:
        print('#{} {}'.format(test_case, odd+even+last))