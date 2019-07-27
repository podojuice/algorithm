import sys

sys.stdin = open('5205.txt')

T = int(input())
for te in range(1, T+1):
    N = int(input())

    X = list(map(int,input().split()))

    print('#{} {}'.format(te, sorted(X)[N//2]))