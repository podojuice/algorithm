import sys

sys.stdin = open('B1268.txt')

N = int(input())

X =[]

result = [[] for _ in range(N)]

for i in range(1, N+1):
    X.append(list(map(int, input().split())))


for i in range(N-1):
    for j in range(5):
        for k in range(i+1, N):
            if X[i][j] == X[k][j]:
                if k not in result[i]:
                    result[i].append(k)
                    result[k].append(i)

max_num = 0
max_idx = 0
for i in range(N):
    if len(result[i]) > max_num:
        max_num = len(result[i])
        max_idx = i
print(max_idx+1)
