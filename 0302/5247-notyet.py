import sys

sys.stdin = open('5247.txt', 'r')

T = int(input())


def BFS(y):
    global cnt
    global stack

    temp = []
    for i in range(len(stack)):
        a, b, c, d = stack[i]+1, stack[i]-1, stack[i]*2, stack[i]-10
        if a == y or b == y or c == y or d == y:
            cnt += 1
            return cnt
        if c <= 1000000 and c not in stack and c not in temp:
            temp.append(c)
        if a <= 1000000 and a not in stack and a not in temp:
            temp.append(a)
        if b > stack[0] and b not in stack and b not in temp:
            temp.append(b)
        if d > stack[0] and d not in stack and d not in temp:
            temp.append(d)
    cnt += 1
    stack += temp
    BFS(y)


for test_case in range(1, T+1):
    N = list(map(int, input().split()))
    stack = [N[0]]
    cnt = 0
    BFS(N[1])

    print(cnt)
