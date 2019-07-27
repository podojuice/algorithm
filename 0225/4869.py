import sys
sys.stdin = open('4869.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    N = N//10 - 1
    A, B, C, cnt = 1, 0, 0, 0
    while cnt < N:
        A, B, C = A+B+C, A, A
        cnt +=1
    print(A+B+C)

