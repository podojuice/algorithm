import sys

sys.stdin = open('4.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    B = [[0 for _ in range(N)]for _ in range(N)]

    B[N//2][N//2] = B[N//2-1][N//2-1] = 'W'
    B[N//2-1][N//2] = B[N//2][N//2-1] = 'B'

    X = []

    for i in range(M):
        X.append(list(map(int, input().split())))


    for i in X:
        a, b = i[0] - 1, i[1] - 1
        if i[2] == 1:
            B[a][b] = 'B'
            key = 'B'
        else:
            B[a][b] = 'W'
            key = 'W'
        x, y = a, b
        #좌우
        cnt = 0
        while y+1 < N:
            if B[a][y + 1] == key:
                break
            if B[a][y+1] == 0 or y+1 == N-1:
                cnt = 0
                break
            cnt += 1
            y += 1
        for e in range(cnt+1):
            B[a][b+e] = key

        cnt = 0
        y = b

        while y - 1 >= 0:
            if B[a][y-1] == key:
                break
            elif B[a][y-1] == 0 or y-1 == 0:
                cnt = 0
                break
            y -= 1
            cnt += 1
        for e in range(cnt+1):
            B[a][b-e] = key

        cnt = 0
        y = b

        while x+1 < N:
            if B[x+1][b] == key:
                break
            elif B[x+1][b] == 0 or x+1 == N-1:
                cnt = 0
                break

            x += 1
            cnt +=1
        for e in range(cnt+1):
            B[a+e][b] = key

        cnt = 0
        x = a

        while x-1 >= 0:
            if B[x-1][b] == key:
                break
            elif B[x-1][b] == 0 or x-1 == 0:
                cnt = 0
                break
            x -= 1
            cnt += 1
        for e in range(cnt+1):
            B[a-e][b] = key

        x = a
        cnt = 0

        #대각
        while x-1 >= 0 and y-1 >= 0:
            if B[x-1][y-1] == key:
                break
            elif B[x-1][y-1] == 0 or x-1 == 0 or y - 1 == 0:
                cnt = 0
                break
            x -= 1
            y -= 1
            cnt +=1

        for e in range(cnt+1):
            B[a-e][b-e] = key

        cnt = 0
        x, y = a, b

        while x+1 < N and y+1 < N:
            if B[x+1][y+1] == key:
                break
            elif B[x+1][y+1] == 0 or x+1 == N-1 or y+1 == N-1:
                cnt = 0
                break
            x += 1
            y += 1
            cnt += 1
        for e in range(cnt+1):
            B[a+e][b+e] = key

        cnt = 0
        x, y = a, b

        while x+1 < N and y-1 >= 0:
            if B[x+1][y-1]==key:
                break
            elif B[x+1][y-1] == 0 or x+1 == N-1 or y-1 == 0:
                cnt = 0
                break
            x += 1
            y -= 1
            cnt += 1

        for e in range(cnt+1):
            B[a+e][b-e] = key

        cnt = 0
        x, y = a, b

        while x-1 >= 0 and y+1 < N:
            if B[x-1][y+1] == key:
                break
            elif B[x-1][y+1] == 0 or x-1 == 0 or y+1 == N-1:
                cnt = 0
                break
            x -= 1
            y += 1
            cnt += 1

        for e in range(cnt+1):
            B[a-e][b+e] = key

        black = 0
        white = 0
        for i in B:
            for j in i:
                if j == 'B':
                    black += 1
                elif j == 'W':
                    white += 1

    print('#{} {} {}'.format(test_case, black, white))
