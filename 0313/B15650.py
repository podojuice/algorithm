import sys

sys.stdin = open('B15650.txt')

def C(M, cnt, result):
    for i in range(len(temp)-M):
        result.append(temp[i])



N, M = map(int, input().split())

temp = []

for i in range(1, N+1):
    temp += [i]
cnt = 0
result = []
C(M, cnt, result)




