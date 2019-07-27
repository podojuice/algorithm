import sys

sys.stdin = open('5207.txt')


def bi(key, start, end):
    global A, cnt
    l = False
    r = False
    while start <= end:
        mid = (start+end)//2

        if A[mid] == key:
            print(A[mid], l, r)
            cnt += 1
            return
        if A[mid] < key:
            if r:
                return
            else:
                start = mid + 1
                r = True
                l = False
        else:
            if l:
                return
            else:
                end = mid - 1
                r = False
                l = True



T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))

    B = list(map(int, input().split()))
    cnt = 0

    for i in B:
        bi(i, 0, len(A)-1)

    print(cnt)
