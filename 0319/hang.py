arr = [[1, 2], [2, 4], [4, 5], [5, 3], [3, 7], [7, 5]]

new_arr = []
cnt = 0
MIN = 10000000
def check(arr, result=0):
    global MIN
    if len(arr) == 2:
        MIN = min(MIN, result)
        return
    for i in range(1, len(arr)-1):
        result += arr[i-1]*arr[i]*arr[i+1]
        new = arr[:]
        new.pop(i)
        check(new, result)



for i in range(len(arr)):
    if i == 0:
        new_arr.append(arr[i][0])
        new_arr.append(arr[i][1])
    elif i == len(arr)-1:
        new_arr.append(arr[i][1])
    else:
        new_arr.append(arr[i][1])

check(new_arr)
print(MIN)
