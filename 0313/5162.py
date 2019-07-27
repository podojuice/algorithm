import sys

sys.stdin = open('5162.txt')

T = int(input())

for test_case in range(1, T+1):
    A, B, C = map(int, input().split())
    if A > B:
        key = B
    else:
        key = A
    result = C//key
    print('#{} {}'.format(test_case, result))