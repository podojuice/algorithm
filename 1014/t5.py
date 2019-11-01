N, M, T = map(int, input().split())

arr = [[]]

for i in range(N):
    arr.append(list(map(int, input().split())))





query = []

for i in range(T):
    query.append(list(map(int, input().split())))
# query[i][0]의 배수인 원판을 query[i][1]의 방향으로(0 -> 오 , 1-> 왼) query[i][2] 칸만큼
for i in range(T):
    # 쿼리 들어옴.
    x = query[i][0]
    d = query[i][1]
    k = query[i][2]
    tx = x
    while tx <= N:
        if d == 0:
            arr[tx] = arr[tx][M-k:] + arr[tx][:M-k]
        else:
            arr[tx] =   arr[tx][k:] + arr[tx][:k]
        tx += x
    check = [[False]*M for _ in range(N+1)]
    for p in range(1, N+1):
        for q in range(M):
            if arr[p][q] == 0:
                continue
            if p+1 <= N:
                if arr[p+1][q] == arr[p][q]:
                    check[p+1][q] = True
                    check[p][q] = True
            if q-1 < 0:
                tq = M-1
            else:
                tq = q-1
            if arr[p][tq] == arr[p][q]:
                check[p][tq] = True
                check[p][q] = True
            if q+1>=M:
                tq = 0
            else:
                tq = q+1
            if arr[p][q] == arr[p][tq]:
                check[p][q] = True
                check[p][tq] = True

    tmp = 0
    cnt = 0
    isbomb = False
    for p in range(1, N+1):
        for q in range(M):
            if check[p][q]:
                arr[p][q] = 0
                isbomb = True
            else:
                if arr[p][q] != 0:
                    cnt += 1
                    tmp += arr[p][q]
    if not isbomb:
        if cnt == 0:
            break
        pm = (tmp/cnt)
        for p in range(1, N+1):
            for q in range(M):
                if arr[p][q] != 0:
                    if arr[p][q]>pm:
                        arr[p][q] -=1
                    elif arr[p][q] < pm:
                        arr[p][q] +=1

ans = 0
for i in range(1, N+1):
    for j in range(M):
        if arr[i][j] != 0:
            ans += arr[i][j]



print(ans)