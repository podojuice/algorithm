import sys

sys.stdin = open('4613.txt')


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


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    X = []

    for _ in range(N):
        X.append(input())

    arr = []

    for i in range(1, N):
        arr.append(i)

    tr = [0, 0]

    result = []

    comb(N-1, 2)
    print(result)
    min_num = 100000000000
    for i in result:
        line_1, line_2 = i[0], i[1]
        temp = []
        cnt = 0
        for j in range(i[0]):
            temp.append('W'*M)
        for j in range(i[0], i[1]):
            temp.append('B'*M)
        for j in range(i[1], N):
            temp.append('R'*M)

        for p in range(N):
            for q in range(M):
                if X[p][q] != temp[p][q]:
                    cnt +=1
        if cnt < min_num:
            min_num = cnt

    print(min_num)

