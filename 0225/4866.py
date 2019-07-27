import sys

sys.stdin = open('4866.txt', 'r')

T = int(input())
start = ['(', '{', '[']
end = [')', '}', ']']


def check(n):
    stack = []
    for i in n:
        for j in range(len(start)):
            if i == start[j]:
                stack += [i]
            elif i == end[j]:
                if stack:
                    if stack[-1] == start[j]:
                        stack.pop(-1)
                    else:
                        return 0
                else:
                    return 0
    if stack:
        return 0
    else:
        return 1


for test_case in range(1, T+1):
    N = input()
    print(f'#{test_case} {check(N)}')



