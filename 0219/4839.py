import sys

sys.stdin = open('sample_input3.txt', 'r')

T = int(input())


def bise(low, high, key, cnt=0):
    cnt += 1
    if low > high:
        return 0
    else:
        mid = (low+high)//2
        if key == mid:
            return cnt
        elif key < mid:

            return bise(low, mid, key, cnt)
        elif mid < key:

            return bise(mid, high, key, cnt)

for test_case in range(1, T+1):
    N = list(map(int, input().split()))
    if bise(1, N[0], N[1]) > bise(1, N[0], N[2]):
        result = 'B'
    elif bise(1, N[0], N[1]) < bise(1, N[0], N[2]):
        result = 'A'
    else:
        result = '0'
    print(f'#{test_case} {result}')