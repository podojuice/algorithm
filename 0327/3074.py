T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    X = []

    for _ in range(N):
        X.append(int(input()))
    end = max(X) * M
    start = 0
    while start < end:
        check = True
        mid = (start + end) // 2
        result = 0
        for i in X:
            result += mid // i
            if result >= M:
                break
        else:
            check = False
        if check:
            end = mid
        else:
            start = mid + 1
    print('#{} {}'.format(t, start))





