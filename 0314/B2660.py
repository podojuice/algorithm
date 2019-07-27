import sys

sys.stdin = open('B2660.txt')


def pick(k):
    visit = [False] * (man+1)
    D = [0]*(man+1)
    Q = []
    visit[k] = True
    Q.append(k)
    while Q:
        now = Q.pop(0)
        for p in G[now]:
            if not visit[p]:
                visit[p] = True
                D[p] = D[now] + 1
                # print(D)
                Q.append(p)

    max_num = 0
    for i in D:
        if i > max_num:
            max_num = i
    return max_num


man = int(input())

mans = []

for i in range(1, man+1):
    mans += [i]
G = [[]for _ in range(man+1)]

while True:
    u, v = map(int, input().split())

    if u == -1:
        break
    G[u] += [v]
    G[v] += [u]

result = []

for i in mans:
    result += [pick(i)]

min_num = min(result)

cnt = 0
ans = []
for i in range(len(result)):
    if result[i] == min_num:
        cnt += 1
        ans += [mans[i]]

print(min_num, cnt)
for i in ans:
    print(i, end=' ')
print()
