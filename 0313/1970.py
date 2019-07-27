import sys

sys.stdin = open('1970.txt')

T = int(input())

arr= [50000, 10000, 5000, 1000, 500, 100, 50, 10]



for test_case in range(1, T+1):
    N = int(input())
    print('#{}'.format(test_case))
    for i in arr:
        temp = 0
        while N >= i:
            N -= i
            temp += 1
        print(temp, end=' ')
    print()
