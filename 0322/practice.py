arr = []

for i in range(1, 4):
    arr.append(i)

tr = [0, 0]
result = []

def comb(n, r):
    if r == 0:
        if tr[0] <= tr[1]:
            result.append([tr[0], tr[1]])
        else:
            result.append([tr[1], tr[0]])
    elif n < r : return
    else:
        tr[r-1] = arr[n-1]
        comb(n-1, r-1)
        comb(n-1, r)


comb(3, 2)
print(result)
print(arr)

