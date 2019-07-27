import sys

sys.stdin = open('B2193.txt')


def check():
    for i in range(K+1):
        if i == 1 or i == 2:
            D[i] = 1
        else:
            D[i] = D[i-1]+D[i-2]

K = int(input())

D = [0]*(K+1)

check()

print(D)


