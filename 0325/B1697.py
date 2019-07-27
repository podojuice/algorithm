import sys

sys.stdin = open('B1697.txt')


def check(Q):
    global used, cnt
    while Q:
        cnt += 1
        temp = []
        for i in Q:
            if i+1 <= 100000 and i+1 not in used and i + 1 not in temp:
                if i+1 == B:
                    return cnt
                temp.append(i+1)
            if i - 1 >= 0 and i - 1 not in used and i - 1 not in temp:
                if i-1 == B:
                    return cnt
                temp.append(i-1)
            if i * 2 <= 100000 and i * 2 not in used and i * 2 not in temp:
                if i*2 == B:
                    return cnt
                temp.append(i*2)
        used += Q
        Q = temp
        print(used, Q)


S, B = map(int, input().split())

Q = [S]

used = []
cnt = 0
print(check(Q))


