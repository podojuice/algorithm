import sys

sys.stdin = open('B2635.txt')

N = int(input())


def check(num1, num2):
    global max_num, result
    temp = []
    cnt = 0
    while num1 >= 0:
        cnt += 1
        temp.append(num1)
        num1, num2 = num2, num1 - num2
    if max_num < cnt:
        max_num = cnt
        result = temp


max_num = 0
result = []
for i in range(N//2, N+1):
    check(N, i)


print(max_num)
for i in result:
    print(i, end=' ')
