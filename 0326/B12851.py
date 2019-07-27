import sys

sys.stdin = open('B12851.txt')

from collections import deque

def check(B):
    while Q:

        if street[B]:
            print(street[B]-1)
            return
        now = Q.popleft()

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

Q = deque()

Q.append(S)

street[S] = 1

check(B)



Q2= deque()
Q2.append(B)
i = 0
cnt = 0
while Q2:
    now = Q2.popleft()

    if street[now] == 1:
        cnt += 1
    if now+1 <= 100000:
        if street[now+1] == street[now]-1:
            Q2.append(now+1)
    if now-1 >= 0:
        if street[now-1] == street[now]-1:
            Q2.append(now-1)
    if not now % 2:
        if street[now//2] == street[now]-1:
            Q2.append(now//2)

    i += 1

print(cnt)