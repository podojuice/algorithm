N = int(input())

arr = []

for i in range(N):
    arr.append(int(input()))

# print(arr)


ret = []

ans = []

for i in range(N):
    tmp = 0
    if i-1>=0:
        tmp = ret[i-1][0]
    ret.append([0, tmp+arr[i]])
    tmp = 0
    if i-2>=0:
        tmp = max(ret[i-2])
    ret[i][0] = tmp+arr[i]
    if ret[i][0]> ret[i][1]:
        ans.append(ret[i][0])
    else:
        ans.append(ret[i][1])

print(ans[N-1])