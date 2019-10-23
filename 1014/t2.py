N = int(input())

arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

ans = 0xfffffffff

for i in range(N):
    for j in range(N):
        if (i == 0) | (i == N-1) | (j >= N-2):
            continue
        for p in range(1, N):
            for q in range(1, N):
                if (j+p+q < N) & (i-p >= 0) & (i+q <N):
                    MAX = 0
                    MIN = 0xfffffffff
                    g = [0]*5
                    visit = [[False]*N for _ in range(N)]
                    for x in range(p+1):
                        visit[i-x][j+x] = True
                    for x in range(q+1):
                        visit[i-p+x][j+p+x] = True
                    for x in range(p+1):
                        visit[i-p+q+x][j+p+q-x] = True
                    for x in range(q+1):
                        visit[i+q-x][j+q-x] = True
                    for x in range(N):
                        now = 0
                        cnt = 0
                        while(now<N):
                            if visit[x][now]:
                                if cnt == 0:
                                    t1 = now
                                elif cnt == 1:
                                    t2 = now
                                cnt += 1
                            now += 1
                        if cnt == 2:
                            for y in range(t1, t2+1):
                                visit[x][y] = True
                                
                    for x in range(N):
                        for y in range(N):
                            if (x<i) & (y<=j+p) & (not visit[x][y]):
                                g[0] += arr[x][y]
                            elif (x<=i-p+q) & (y>j+p) & (not visit[x][y]):
                                g[1] += arr[x][y]
                            elif (x>=i) & (y<j+q) & (not visit[x][y]):
                                g[2] += arr[x][y]
                            elif (x>i-p+q) & (y>=j+q) & (not visit[x][y]):
                                g[3] += arr[x][y]
                            else:
                                g[4] += arr[x][y]

                    for x in range(5):
                        if g[x] > MAX:
                            MAX = g[x]
                        if g[x]<MIN:
                            MIN = g[x]
                    if ans > MAX-MIN:
                        ans = MAX-MIN

print(ans)