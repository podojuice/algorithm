import sys

sys.stdin = open('5097.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = list(map(int, input().split()))
    X = list(map(int, input().split()))
    print(X[N[1]%N[0]])