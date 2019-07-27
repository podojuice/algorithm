import sys

sys.stdin = open('4008.txt')

def cal(p):
    global MAX, MIN

    t = X[0]
    for i in range(len(p)):
        if p[i] == 0:
            t += X[i+1]
        elif p[i] == 1:
            t -= X[i+1]
        elif p[i] == 2:
            t *= X[i+1]
        else:
            t = int(t/X[i+1])
    if t > MAX:
        MAX = t
    if t < MIN:
        MIN = t


def perm(n, k, temp=[]):
    if n == k:
        cal(temp)
        return
    for i in range(N-1):
        if not used[i] and (i == 0 or l[i-1] != l[i] or used[i-1]):
            temp.append(l[i])
            used[i] = True
            perm(n, k+1, temp)
            used[i] = False
            temp.pop()

T = int(input())

for t in range(1, T+1):
    N = int(input())

    p, m, b, s = map(int, input().split())


    X = list(map(int, input().split()))

    # 0 = '+' 1 = '-', 2 = '*', 3 = '/'

    l = [0]*p + [1]*m + [2]*b + [3]*s

    used = [False]*(N-1)

    result = []

    MAX = -0xfffffff

    MIN = 0xfffffffff

    perm(N-1, 0)

    print('#{} {}'.format(t, MAX - MIN))
