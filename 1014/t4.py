
def dfs(cnt):
    global order
    if cnt == 10:
        check(order)
        return
    for i in range(4):
        order[cnt] = i
        dfs(cnt+1)

def check(orde):
    global MAX
    ans = 0
    isarrive = [False]*4
    loca = [[0, 0] for _ in range(4)]
    visit = [[False]*20, [False]*3, [False]*2, [False]*3, [False]*4]
    for i in range(10):
        now = orde[i]
        if isarrive[now]:
            continue
        nownum = dice[i]
        nx = loca[now][0]
        ny = loca[now][1]
        tx = loca[now][0]
        ty = loca[now][1]
        if nx == 0:
            if ny == 5:
                tx = 1
                ty = -1
            elif ny == 10:
                tx = 2
                ty = -1
            elif ny == 15:
                tx = 3
                ty = -1
        ty += nownum
        if (tx == 0) & (ty == 20):
            if not visit[4][3]:
                ans += pan[4][3]
                visit[nx][ny] = False
                visit[4][3] = True
                loca[now] = [4, 3]
            continue

        if ty >= len(pan[tx]):
            if tx == 0:
                visit[nx][ny] = False
                isarrive[now] = True
                continue
            elif tx == 4:
                visit[nx][ny] = False
                isarrive[now] = True
                continue
            else:
                ty -= len(pan[tx])
                tx = 4
                if ty >= len(pan[tx]):
                    visit[nx][ny] = False
                    isarrive[now] = True
                    continue

        if not visit[tx][ty]:
            ans += pan[tx][ty]
            visit[nx][ny] = False
            visit[tx][ty] = True
            loca[now] = [tx, ty]
        else:
            return
    if ans>MAX:
        print(orde, loca)
        MAX = ans


# dice = list(map(int, input().split()))
dice = [5,4,3,5,4,1,3,5,4,2]
order = [0]*10
MAX = 0
pan = [[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38],  [13, 16, 19],  [22, 24],  [28, 27, 26], [25, 30, 35, 40]]
dfs(0)


print(MAX)