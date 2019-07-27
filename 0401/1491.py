import sys

sys.stdin = open('1491.txt')

def check(key):
    global min_num
    r = c = 1
    while r <= key:
        while r * c <= N:
            min_num = min(min_num, A*abs(r-c)+B*(N-r*c))
            c += 1
        c = 1
        r += 1


T = int(input())

for t in range(1, T+1):
    N, A, B = map(int, input().split())
    min_num = B*(N-1)
    key = int(N**(1/2))
    check(key)
    print('#{} {}'.format(t, min_num))

