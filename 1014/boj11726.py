N = int(input())

arr = [[0,0], [1, 0]]

for i in range(2, N+1):
    arr.append([arr[i-1][0]+arr[i-1][1], arr[i-1][0]])

print((arr[N][0]+arr[N][1])%10007)