import sys
sys.stdin = open('workshop.txt', 'r')
for test_case in range(1, 11):
    T = int(input())
    N = []
    for i in range(100):
        N += [list(map(int, input().split()))]
    for i in range(len(N)):
        if N[99][i] == 2:
            key = i
            break
    y = 99
    x = key
    while y > 0:
        if x == 0:
            if N[y][x+1] == 1:
                cnt = 0
                while N[y-1][x+1+cnt] == 0:
                    cnt += 1
                x += cnt + 1
                y -= 1
            else:
                y -= 1
        elif x == 99:
            if N[y][x-1] == 1:
                cnt = 0
                while N[y-1][x-1-cnt] == 0:
                    cnt += 1
                x -= cnt + 1
                y -= 1
            else:
                y -= 1

        elif N[y][x+1] == 1:
            cnt=0
            while N[y-1][x+1+cnt] == 0:
                cnt +=1
            x += cnt + 1
            y -= 1
        elif N[y][x-1] == 1:
            cnt = 0
            while N[y-1][x-1-cnt] == 0:
                cnt +=1
            x -= cnt + 1
            y -= 1
        else:
            y -= 1

    print(f'#{test_case} {x}')
