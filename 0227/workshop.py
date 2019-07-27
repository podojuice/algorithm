import sys

sys.stdin = open('workshop.txt', 'r')


def cal(N):
    stack = []
    num = []
    for i in range(len(N)):
        if N[i].isdigit():
            N[i] = int(N[i])
            num += [N[i]]

    for i in range(len(N)):
        if type(N[i]) == int:
            stack += [N[i]]
        else:
            if len(stack) < 2:
                break
            else:
                if N[i] == '+':
                    stack[-2] = stack[-2] + stack[-1]
                elif N[i] == '*':
                    stack[-2] = stack[-2] * stack[-1]
                stack.pop()
    result_1 = stack[0]
    return result_1



for test_case in range(1, 11):
    N = int(input())
    X = input()
    result = []
    stack_1 = []
    for i in range(len(X)):
        if not X[i].isdigit():
            if X[i] == '(':
                stack_1.append(X[i])
            if X[i] == ')':
                while stack_1[-1] != '(':
                    result.append(stack_1.pop(-1))
                stack_1.pop(-1)
            if X[i] == '+':
                while stack_1[-1] != '(':
                    result.append(stack_1.pop(-1))
                stack_1.append('+')
            if X[i] == '*':
                while stack_1[-1] == '*':
                    result.append(stack_1.pop(-1))
                stack_1.append('*')
        else:
            result += [X[i]]
    print(f'#{test_case} {cal(result)}')


