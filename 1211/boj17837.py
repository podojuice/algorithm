N , K = map(int, input().split())

zido = []

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

turn = 1

for i in range(N):
    zido.append(list(map(int , input().split())))
# 1 빨강 2 파랑 0 흰

mal = [[[] for _ in range(N)] for __ in range(N)]

knight =[]

# 1부터 오왼위아
for i in range(K):
    x, y, v = map(int, input().split())
    knight.append([x-1, y-1, v])
    mal[x-1][y-1].append(i)


# print(zido)
go = True
while go:
    # print(mal)
    # print(knight)
    # print('--------------------')
    for i in range(len(knight)):
        nx = knight[i][0]
        ny = knight[i][1]
        nv = knight[i][2]
        tmp = []
        # print(mal, nx, ny)
        for j in range(len(mal[nx][ny])-1, -1, -1):
            if mal[nx][ny][j] != i:
                tmp.append(mal[nx][ny].pop())
            else:
                tmp.append(mal[nx][ny].pop())
                break
        # 내 위에 있는 애들 전부 tmp 배열에 넣었음.
        tx = nx + dx[nv]
        ty = ny + dy[nv]
        if (tx < 0) | (tx >= N) | (ty < 0) | (ty >= N):
            # 벽에 부딪힘. 파랑이랑 같은 일  해야됨.
            if nv == 1:
                nv = 2
            elif nv == 2:
                nv = 1
            elif nv == 3:
                nv = 4
            else:
                nv = 3
            tx = nx + dx[nv]
            ty = ny + dy[nv]
            knight[i][2] = nv
            if (tx < 0) | (tx >= N) | (ty < 0) | (ty >= N):
                
                mal[nx][ny] += list(reversed(tmp))
                
            elif zido[tx][ty] == 2:

                mal[nx][ny] += list(reversed(tmp))
            elif zido[tx][ty] == 1:
                # 빨강
                mal[tx][ty] += tmp
                if len(mal[tx][ty]) >= 4:
                    print(turn)
                    go = False
                    break
                # 위치 갱신
                for k in tmp:
                    knight[k][0] = tx
                    knight[k][1] = ty
            else:
                mal[tx][ty] += list(reversed(tmp))
                if len(mal[tx][ty]) >= 4:
                    print(turn)
                    go = False
                    break
                # 위치 갱신
                for k in tmp:
                    knight[k][0] = tx
                    knight[k][1] = ty
            
            

        elif zido[tx][ty] == 2:
            if nv == 1:
                nv = 2
            elif nv == 2:
                nv = 1
            elif nv == 3:
                nv = 4
            else:
                nv = 3
            tx = nx + dx[nv]
            ty = ny + dy[nv]
            knight[i][2] = nv
            if (tx < 0) | (tx >= N) | (ty < 0) | (ty >= N):
                
                mal[nx][ny] += list(reversed(tmp))
            elif zido[tx][ty] == 2:

                mal[nx][ny] += list(reversed(tmp))
            elif zido[tx][ty] == 1:
                # 빨강
                mal[tx][ty] += tmp
                if len(mal[tx][ty]) >= 4:
                    print(turn)
                    go = False
                    break
                # 위치 갱신
                for k in tmp:
                    knight[k][0] = tx
                    knight[k][1] = ty
            else:
                mal[tx][ty] += list(reversed(tmp))
                if len(mal[tx][ty]) >= 4:
                    print(turn)
                    go = False
                    break
                # 위치 갱신
                for k in tmp:
                    knight[k][0] = tx
                    knight[k][1] = ty

        elif zido[tx][ty] == 1:
            # 빨강
            mal[tx][ty] += tmp
            if len(mal[tx][ty]) >= 4:
                print(turn)
                go = False
                break
            for k in tmp:
                knight[k][0] = tx
                knight[k][1] = ty
        else:
            mal[tx][ty] += list(reversed(tmp))
            if len(mal[tx][ty]) >= 4:
                print(turn)
                go = False
                break
            for k in tmp:
                knight[k][0] = tx
                knight[k][1] = ty
    if go:
        turn += 1
        if turn >=1000:
            print(-1)
            go=False
            break
# print(mal, knight)