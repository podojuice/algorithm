import sys

sys.stdin = open('workshop.txt', 'r')

for test_case in range(1, 11):
    N = list(map(int, input().split()))
    temp = list(map(int, input().split()))

    X = [[] for i in range(101)]
    visit = [False]*(101)
    length = [0]*(101)
    Q = []

    for i in range(N[0]//2):
        if temp[2 * i + 1] not in X[temp[2 * i]]:
            X[temp[2 * i]] += [temp[2 * i + 1]]

    Q += [N[1]]
    visit[N[1]] = True
    while Q:
        now = Q.pop(0)

        for i in X[now]:
            if not visit[i]:
                visit[i] = True
                Q.append(i)
                length[i] = length[now] + 1
    max_num = 0
    for i in range(len(length)):
        if max_num <= length[i]:
            max_num = length[i]
            idx = i
    print(idx)


