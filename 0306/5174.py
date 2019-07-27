import sys

sys.stdin = open('5174.txt')

T = int(input())

def inorder(N):
    global order
    if N == 0:
        return
    order.append(N)
    # print(N)
    inorder(L[N])
    inorder(R[N])



for test_case in range(1, T+1):
    E, N = map(int, input().split())
    L = [0] * (E + 2)
    R = [0] * (E + 2)
    # P = [0] * (E + 2)
    temp = list(map(int, input().split()))
    for i in range(E):
        if not L[temp[2*i]]:
            L[temp[2*i]] = temp[2 * i+1]
        else:
            R[temp[2 * i]] = temp[2 * i+1]
    order = []
    inorder(N)
    print('#{} {}'.format(test_case, len(order)))

