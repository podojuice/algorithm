import sys

sys.stdin = open('workshop.txt')

for test_case in range(1, 11):
    N = int(input())
    order = [0]
    for i in range(N):
        X = input().split()
        if X[1].isdigit():
            order.append(int(X[1]))
        else:
            order.append([X[1], int(X[2]), int(X[3])])

    while type(order[1]) == list:
        for i in range(1, len(order)-1):
            if type(order[i]) == int:
                continue
            elif type(order[order[i][1]]) == int and type(order[order[i][2]]) == int:
                a, b = order[order[i][1]], order[order[i][2]]
                if order[i][0] == '+':
                    order[i] = a + b
                elif order[i][0] == '-':
                    order[i] = a - b
                elif order[i][0] == '*':
                    order[i] = a * b
                elif order[i][0] == '/':
                    order[i] = a // b

    print('#{} {}'.format(test_case, order[1]))