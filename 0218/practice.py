arr = [[9,20,2,18,11],[19,1,25,3,21],[8,24,10,17,7],[15,4,16,5,6],[12,13,22,23,14]]
result = 0
for i in range(5):
    for j in range(5):
        key = arr[i][j]
        if i == 0:
            if j == 0:
                result += abs(arr[i][j+1] - key) + abs(arr[i+1][j] - key)
            elif j == 4:
                result += abs(arr[i][j-1] - key) + abs(arr[i+1][j]-key)
            else:
                result += abs(arr[i][j-1]-key) + abs(arr[i+1][j]-key) + abs(arr[i][j+1]-key)
        elif j == 0:
            if i == 4:
                result += abs(arr[i-1][j]-key) + abs(arr[i][j+1])
            else:
                result += abs(arr[i-1][j]-key) + abs(arr[i][j+1]-key) + abs(arr[i+1][j]-key)
        elif i == 4:
            if j == 4:
                result += abs(arr[i-1][j]-key)+abs(arr[i][j-1])
            else:
                result += abs(arr[i][j-1]-key) + abs(arr[i][j+1]) + abs(arr[i-1][j])
        elif j == 4:
            result += abs(arr[i-1][j]-key) + abs(arr[i][j-1]-key) + abs(arr[i+1][j]-key)

        else:
            result += abs(arr[i-1][j]-key) + abs(arr[i+1][j]-key) + abs(arr[i][j+1]-key) + abs(arr[i][j-1]-key)

print(result)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 부분집합의 합이 10이 되는 경우 출력
n=len(arr)

for i in range(1<<n): # 1<<n = 2**6 = 64
    number = 0
    for j in range(n):
        if i & (1<<j) !=0:
            number += arr[j]
    if number == 10:
        for j in range(n):
            if i & (1<<j)!=0:
                print(arr[j], end=", ")
        print()


arr = [2,5,8,9,12,16,21,23,33,39,42,45,46,49,62,88]


def binarySearch(arr, key):
    start, end =  0, len(arr) - 1

    while start <=end:
        mid = (start + end) >> 1
        if arr[mid] == key: return mid
        elif arr[mid] > key:
            end = mid -1

        else:
            start = mid +1
    return -1

#재귀

def bise(arr, start, end, key):
    if start>end: return -1
    mid = (start+end)>>1
    if arr[mid] == key: return mid
    elif arr[mid]>key:
        return bise(arr, start, mid-1, key)
    else:
        return bise(arr, mid+1, end, key)









