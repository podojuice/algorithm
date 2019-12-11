

def quick(s, e, arr):
    if s < e:
        pivot = s
        ts = s
        te = e
        while ts < te:
            while (arr[ts] <= arr[pivot]) & (ts< e):
                ts += 1
            while arr[te] > arr[pivot]:
                te -=1
            if ts < te:
                tmp = arr[ts]
                arr[ts] = arr[te]
                arr[te] = tmp
        print(arr, pivot, te)
        tmp = arr[pivot]
        arr[pivot] = arr[te]
        arr[te] = tmp
        
        quick(s, te-1, arr)
        quick(te+1, e, arr)


def merge(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    arr1 = merge(arr[:mid])
    arr2 = merge(arr[mid:])
    tmp = []
    while (len(arr1) > 0) & (len(arr2)>0):
        if arr1[0] < arr2[0]:
            tmp.append(arr1.pop(0))
        else:
            tmp.append(arr2.pop(0))
    if arr1:
        while arr1:
            tmp.append(arr1.pop(0))
    if arr2:
        while arr2:
            tmp.append(arr2.pop(0))

    return tmp
    



arr = [50, 10, 100, 13, 199, 56, 333, 1, 7]

quick(0, len(arr)-1, arr)
# print(merge(arr))

