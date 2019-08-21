

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    key = [[]for i in range(col)]

    
    for i in range(1, col+1):
        makecols(i, set(), 0, 0, col, key, row, relation)

    print(key)


def check(row, cols, relation, key, now):
    tmp = set()
    for r in range(row):
        T = ""
        for c in cols:
            T += str(relation[r][c])
        tmp.add(T)
        print(T)
    if len(tmp)==row:
        key[now-1].append(cols)

def makecols(MAX, ret, cnt, now, col, key, row, relation):
    if ret in key[len(ret)-2]:
        return
    if MAX == cnt:
        check(row, ret, relation, key, MAX)
        return
    if cnt+now >= col:
        return
    for i in range(now, col):
        ret.add(i)
        makecols(MAX, ret, cnt+1, i+1, col, key, row, relation)


input = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

solution(input)