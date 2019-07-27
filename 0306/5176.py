import sys

sys.stdin = open('5176.txt')

T = int(input())


def inorder(n):
    global order
    if n == 0: return
    inorder(L[n])
    order.append(n)
    inorder(R[n])


for test_case in range(1, T+1):
    N = int(input())
    L = [0]*(N+1)
    R = [0]*(N+1)
    for i in range(1, N):
        if i%2:
            L[(i+1)//2] = (i+1)//2*2
        else:
            R[(i+1)//2] = (i+1)//2*2+1

    order = []
    inorder(1)
    for i in range(len(order)):
        if order[i] == 1:
            a = i
        if order[i] == N//2:
            b = i
    print('#{} {} {}'.format(test_case, a+1, b+1))
