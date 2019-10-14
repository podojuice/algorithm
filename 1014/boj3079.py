N, M = map(int, input().split())
MIN = 10**14+1
arr = []

for i in range(N):
    arr.append(int(input()))

def binary(s, arr):
    global MIN, M
    e = max(arr)*M
    while(s+1<e):
        mid = (s+e)//2
        tmp = 0
        for i in range(len(arr)):
            tmp += mid//arr[i]
        if tmp >= M:
            if MIN > mid:
                MIN = mid
            e = mid
        else:
            s = mid


binary(0, arr)

print(MIN)