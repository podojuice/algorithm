import sys

sys.stdin = open('test.txt')

from copy import deepcopy


def shot(i, j, k):
    global cnt
    s_list = [[N - 1, i], [N - 1, j], [N - 1, k]]
    po = [[], [], []]
    for p in range(len(s_list)):
        for q in range(len(enemy)):
            key = abs(s_list[p][0] - enemy[q][0]) + abs(s_list[p][1] - enemy[q][1])

            if key < D:
                if not po[p]:
                    po[p] = [q, key]
                else:
                    if key < po[p][1]:
                        po[p] = [q, key]
                    elif key == po[p][1] and enemy[po[p][0]][1] > enemy[q][1]:
                        po[p] = [q, key]

    temp = []

    for p in po:
        if p:
            if p[0] not in temp:
                temp.append(p[0])
    temp.sort(reverse=True)
    for p in temp:
        enemy.pop(p)
        cnt += 1


def come():
    temp = []
    for p in range(len(enemy)):
        if enemy[p][0] == N - 1:
            temp.append(p)
        else:
            enemy[p][0] += 1

    temp.sort(reverse=True)
    for p in temp:
        enemy.pop(p)

T = int(input())
for t in range(1, T+1):
    M, N, D = map(int, input().split())

    X = []

    for _ in range(N):
        X.append(list(map(int, input().split())))

    te = []

    for i in range(N):
        for j in range(M):
            if X[i][j]:
                te.append([i, j])

    MAX = 0

    for i in range(M - 2):
        for j in range(i + 1, M - 1):
            for k in range(j + 1, M):
                enemy = deepcopy(te)
                cnt = 0
                while enemy:
                    shot(i, j, k)
                    come()

                MAX = max(cnt, MAX)

    print(t, MAX)