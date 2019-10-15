N = int(input())

arr = list(map(int, input().split()))

# print(arr)

ans = 0

def dfs(a, cnt):
    global ans

    if cnt == N-1:
        if a == arr[N-1]:
            ans+=1
        return
    for i in range(2):
        if i == 0:
            if a + arr[cnt] <= 20:
                dfs(a+arr[cnt], cnt+1)
        else:
            if a - arr[cnt] >=0:
                dfs(a -arr[cnt], cnt+1)
    
dfs(0, 0)
print(ans)
