import sys

sys.stdin = open('2105.txt')

T = int(input())
for t in range(1, 3):
    N = int(input())

    X = []

    for _ in range(N):
        X.append(list(map(int, input().split())))

    po = []


    print(po)
