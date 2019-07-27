import sys

sys.stdin = open('B1697.txt')

from collections import deque

def check(B):
    while Q:

        if street[B]:
            print(street[B]-1)
            return
        now = Q.pop(0)

        if now+1 <= 100000 and not street[now+1]:
            street[now+1] = street[now]+1
            Q.append(now+1)
        if now-1 >= 0 and not street[now-1]:
            street[now-1] = street[now]+1
            Q.append(now-1)
        if now*2 <= 100000 and not street[now*2]:
            street[now*2] = street[now]+1
            Q.append(now*2)


S, B = map(int , input().split())

street = [0]*100001

Q = []

Q.append(S)

street[S] = 1

check(B)
