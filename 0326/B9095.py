import sys

sys.stdin = open('B9095.txt')

N = int(input())

L = [0]*12

L[1] = 1
L[2] = 2
L[3] = 4
for i in range(4, 12):
    L[i] = L[i-3]+L[i-2]+L[i-1]

for _ in range(N):
    temp = int(input())
    print(L[temp])