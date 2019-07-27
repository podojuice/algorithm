import sys

sys.stdin = open('B2437.txt')

def check():
    global key
    for i in range(len(X)):
        if i == len(X)-1:
            print(X[-1])
        if X[i+1] <= X[i] + 1:
            X[i+1] += X[i]
        else:
            key = i
            return

N = int(input())

X = sorted(list(map(int, input().split())))

arr = 0


if X[0] != 1:
    print(1)
else:
    key = False
    check()
    if key:
        print(X[key]+1)
    else:
        print(X[-1])
