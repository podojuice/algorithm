import sys

sys.stdin = open('5648.txt')

T = int(input())

N = int(input())

X = []

for _ in range(N):
    X.append(list(map(int, input().split())))

