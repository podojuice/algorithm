import sys

sys.stdin = open('B17071.txt')

from collections import deque



S, B = map(int, input().split())

Q = deque()

Q.append(S)

now = []

cnt = 0

temp = 0

now = deque()

while 1:
    l = len(Q)
    for _ in range(l):
        key = Q.popleft()
        if key == B:
            print(cnt)
            temp = 1
            break
        if key + 1 <= 500000 and key + 1 not in Q:
            now.append(key + 1)
        if key * 2 <= 500000 and key * 2 not in Q:
            now.append(key * 2)
        if key - 1 not in Q:
            now.append(key - 1)
    if temp:
        break
    cnt += 1
    B += cnt
    if B > 500000:
        print(-1)
        break

    for i in now:
        Q.append(i)
    now = deque()