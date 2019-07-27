import sys

sys.stdin = open('B2.txt')

C = int(input())

order = []
number = []
E = W = S = N = 0

for i in range(6):
    o, n = map(int, input().split())
    order += [o]
    if o == 1:
        E += 1
    elif o == 2:
        W += 1
    elif o == 3:
        S += 1
    else:
        N += 1
    number += [n]
for i in range(6):
    if order[i] == 1:
        order[i] = E
    elif order[i] == 2:
        order[i] = W
    elif order[i] == 3:
        order[i] = S
    else:
        order[i] = N
for i in range(6):
    if order[i] == 1 and order[i-1] == 2:
        row_1 = number[i]
        col_2 = number[i-1]
    if order[i] == 1 and order[(i+1) % 6] == 2:
        col_1 = number[i]
        row_2 = number[(i+1) % 6]


result = (row_1*col_1) - ((row_1-row_2)*(col_1-col_2))

print(result*C)