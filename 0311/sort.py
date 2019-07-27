temp = [69, 10, 30, 2, 16, 8, 31, 22]

def merge_sort(m):
    if len(m) <= 1:
        return m

    mid = len(m)//2
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(l, r):
    result = []

    while len(l) > 0 and len(r) > 0:

        if l[0] <= r[0]:
            result.append(l.pop(0))
        else:
            result.append(r.pop(0))

    if len(l) > 0:
        result.extend(l)
    if len(r) > 0:
        result.extend(r)
    return result

print(merge_sort(temp))