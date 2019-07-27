#snail
#
# arr = [
#     [1, 2, 3, 4, 5,],
#     [16, 17, 18, 19, 6],
#     [15, 24, 25, 20, 7],
#     [14, 23, 22, 21, 8],
#     [13, 12, 11, 10, 9]
# ]
#
# arr = [
#     [1,2,3,4,5,6],
#     [20,21,22,23,24,7],
#     [19,32,33,34,25,8],
#     [18,31,36,35,26,9],
#     [17,30,29,28,27,10],
#     [16,15,14,13,12,11]
# ]
#
# arr = [
#     [1,2,3,4],
#     [10,11,12,5],
#     [9,8,7,6]
#
# ]

arr = [
    [1,2,3,4,5,6],
    [22,23,24,25,26,7],
    [21,36,37,38,27,8],
    [20,35,42,39,28,9],
    [19,34,41,40,29,10],
    [18,33,32,31,30,11],
    [17,16,15,14,13,12]
]

cnt = 0
result = []

if len(arr)>=len(arr[0]):
    key = len(arr[0])
else:
    key = len(arr)

for i in range(key//2+1):
    for j in range(len(arr[0])-2*cnt):
        result += [arr[cnt][j+cnt]]
    if len(result) == len(arr)*len(arr[0]):
        break
    for j in range(len(arr)-2*cnt-1):
        result += [arr[j+cnt+1][len(arr[0])-1-cnt]]
    for j in range(len(arr[0])-2*cnt-1):
        result += [arr[len(arr)-1-cnt][-j-cnt-1-1]]
    for j in range(len(arr)-2*cnt-2):
        result += [arr[-j-2-cnt][cnt]]
    cnt +=1

print(result)