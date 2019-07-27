import sys
sys.stdin = open('4874.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = list(map(str, input().split()))
    stack = []
    num = []
    strr = []
    for i in range(len(N)):
        if N[i].isdigit():
            N[i] = int(N[i])
            num += [N[i]]
        else:
            strr += [N[i]]
    for i in range(len(N)-1):
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
                elif N[i] == '/':
                    stack[-2] = stack[-2] // stack[-1]
                elif N[i] == '-':
                    stack[-2] = stack[-2] - stack[-1]
                stack.pop()

    result = stack[0]
    if len(num) != len(strr):
        result = 'error'
    print(f'#{test_case} {result}')