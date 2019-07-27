import sys

sys.stdin = open('B10815.txt')

def check(i, start, end):
    mid = (start+end)//2
    if S[mid] == i:
        print(1, end=' ')
        return
    if start >= end:
        print(0, end=' ')
        return
    if S[mid] > i:
        check(i, start, mid-1)
    else:
        check(i, mid+1, end)


N = int(input())

S = sorted(list(map(int, input().split())))

M = int(input())

X = list(map(int, input().split()))


for i in X:
    check(i, 0, len(S)-1)