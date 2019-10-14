M, N = map(int, input().split())

visit = [False]*(N+1)

for i in range(2, N+1):
   tmp = i
   if visit[tmp] == False:
    #    print(tmp)
       tmp = tmp+i
       while tmp <= N:
           visit[tmp] = True
           tmp = tmp+i

for i in range(M, N+1):
    if not visit[i]:
        print(i)