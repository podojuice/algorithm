N, K = map(int,input().split())
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

knight = [[list() for _ in range(N)] for _ in range(N)]

loca = [[] for _ in range(K)]

for i in range(K):
    x, y, v = map(int, input().split())
    knight[x-1][y-1].append([i, v])
    loca[i] = [x-1, y-1]

    # 오왼위밑

print(arr, knight, loca)
turn = 0
while 1:
    check = True
    for i in range(K-1):
        if loca[i] != loca[i+1]:
            check = False
            break
    if check:
        break
    turn += 1
    if turn >= 1001:
        break

    for i in range(K):
        nx, ny = loca[0][0], loca[0][1]
        now = knight[nx][ny][0]
        if now[0] == i:
            # 이래야 움직일 수 있음.
            if now[1] == 1:
                if nx == N-1:
                    knight[nx][ny][1] = 2
                # elif arr[nx+1][ny] == 0:
                    
