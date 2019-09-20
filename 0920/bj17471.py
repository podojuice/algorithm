def check(distict):
    global arr, M
    visit = [False]*(N+1)
    stack = []
    sum1 = 0
    sum2 = 0
    for i in range(1, N+1):
        if district[i] == 1:
            stack.append(i)
            visit[i] = True;
            sum1 += arr[i-1]
            break;
    # 이제 스택에서 꺼내면서 백트래킹으로 갈수잇는 1번 애들 다 갈거.
    
    while(stack):
        now = stack.pop()
        for i in M[now]:
            if (district[i] == 1) & (visit[i] == False):
                visit[i] = True;
                sum1 += arr[i-1]
                stack.append(i)
    # 이제 유효성 검사.

    for i in range(1, N+1):
        if district[i] == 1:
            if not visit[i]:
                return -1

    # visit = [False]*(N+1)
    for i in range(1, N+1):
        if district[i] == 0:
            stack.append(i)
            visit[i] = True;
            sum2 += arr[i-1]
            break;
    # 이제 스택에서 꺼내면서 백트래킹으로 갈수잇는 1번 애들 다 갈거.
    
    while(stack):
        now = stack.pop()
        # print(now)
        for i in M[now]:
            if (district[i] == 0) & (visit[i] == False):
                visit[i] = True;
                sum2 += arr[i-1]
                stack.append(i)

    for i in range(1, N+1):
        if district[i] == 0:
            if not visit[i]:
                return -1
    
    if (sum1 == 0) | (sum2 == 0):
        return -1

    ans = sum1 - sum2
    if ans < 0:
        return ans*-1
    return ans




N = int(input())
MIN = 0xfffffffff

arr = list(map(int, input().split(' ')))

M = [[] for _ in range(N+1)]

for i in range(1, N+1):
    tmp = list(map(int, input().split(' ')))
    for j in range(len(tmp)):
        if j == 0:
            continue
        M[i].append(tmp[j])

print(arr)
print(M)



# 입력 끝


for i in range(1<<N):
    tmp = i
    district = [0]*(N+1)
    cnt = 1
    print(tmp)
    while(cnt<=N):
        if(tmp & 1):
            district[cnt] = 1
        cnt+=1
        tmp = tmp>> 1
    print(district)
    ttmp = check(district)
    print(ttmp)
    if ttmp != -1:
        if MIN > ttmp:
            MIN = ttmp



if MIN == 0xfffffffff:
    print(-1)
else:
    print(MIN)
