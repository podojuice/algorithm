import sys

sys.stdin = open('3752.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())

    X = list(map(int, input().split()))

    visit = [False]*(sum(X)+1)

    arr = [0]

    Q = X
    while Q:
        now = Q.pop(0)
        for i in range(len(arr)):
            if not visit[now + arr[i]]:
                visit[now + arr[i]] = True
                arr.append(now+arr[i])
    print('#{} {}'.format(t, len(arr)))
