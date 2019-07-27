import sys

sys.stdin = open('B2628.txt')

C, R = map(int, input().split())

N = int(input())

c = [0, C]
r = [0, R]

for _ in range(N):
    x, y = map(int, input().split())
    if x == 0:
        r += [y]
    else:
        c += [y]

c.sort()
r.sort()

max_c = max_r = 0

for i in range(len(c)-1):
    if c[i+1] - c[i] > max_c:
        max_c = c[i+1] - c[i]
for i in range(len(r)-1):
    if r[i+1] - r[i] > max_r:
        max_r = r[i+1] - r[i]

print(max_c* max_r)