import sys

sys.stdin = open('input4.txt', 'r')

T=int(input())
for text_case in range(T):
        N, arr = input().split()
        N = int(N)
        print(N, arr)