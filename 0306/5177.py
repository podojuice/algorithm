import sys

sys.stdin = open('5177.txt')

T = int(input())


def sum_number(a):
    global result
    if a == 0:
        return
    result += order[a]
    sum_number(a//2)


for test_case in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    order = [0]
    order += X
    for i in range(len(order)):
        a = i
        while a//2:
            if order[a//2] > order[a]:
                order[a], order[a//2] = order[a//2], order[a]
            a = a//2
    # print(order)
    result = 0
    sum_number((len(order)-1)//2)

    print('#{} {}'.format(test_case, result))
