

import sys

sys.stdin = open('5102.txt', 'r')

T = int(input())

def BFS(S, G):
    Q = [S]
    while Q:
        now = Q.pop(0)
        visit[now] = True
        for i in temp[now]:
            if i == G:
                D[i] = D[now] + 1
                return
            if not visit[i]:
                Q.append(i)
                D[i] = D[now]+1



for test_case in range(1, T+1):
    V, E = list(map(int, input().split()))
    X = []
    for i in range(E):
        X += list(map(int, input().split()))
    S, G = list(map(int,input().split()))
    temp = [[] for i in range(V+1)]
    visit = [False]*(V+1)
    D = [0]*(V+1)
    for i in range(E):
        temp[X[2*i]].append(X[2*i+1])
        temp[X[2 * i+1]].append(X[2 * i])
    BFS(S, G)
    print(D[G])

