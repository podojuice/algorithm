import sys

sys.stdin = open('3750.txt')

T = int(input())

memo = []

for test_case in range(1, T+1):
    X = input()
    number = int(X)
    temp = 0
    while number >= 10:
        temp += number % 10
        if temp >= 10:
            temp = (temp % 10) + 1
        number = number//10
    temp += number
    if temp >= 10:
        temp = (temp % 10) + 1

    memo += ['#{} {}'.format(test_case, temp)]

for i in memo:
    print(i)