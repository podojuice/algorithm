import sys

sys.stdin = open('append.txt')

T = int(input())

def bi_search(i):
    global C
    result = []
    for j in range(1<<len(i)):
        part = []
        for k in range(len(i)):
            if j & (1 << k):
                part.append(i[k])
        if sum(part) <= C:
            sum_n = 0
            for v in part:
                sum_n += v**2
            result.append(sum_n)
    result = max(result)
    return result


for test_case in range(1, T+1):
    N, M, C = map(int, input().split())
    X = []
    for i in range(N):
        X += [list(map(int, input().split()))]
    temp = []
    for i in range(N):
        b = []
        for k in range(N-M+1):
            a = []
            for j in range(M):
                a += [X[i][k+j]]
            b += [a]
        temp += [b]
    real = []
    for row in temp:
        numbers = []
        for l in row:
            numbers.append(bi_search(l))
        real.append(max(numbers))
    real.sort()
    real_result = real[-1]+real[-2]
    if M*2 <= N:
        div_num = []
        for k in range(len(X)):
            for i in range(N-M*2+1):
                for j in range(N-M*2+1-i):
                    a, b = X[k][i:i+M], X[k][i+M+j:i+M+j+M]
                    div_num.append(bi_search(a)+bi_search(b))
        for i in div_num:
            if i > real_result:
                real_result = i

    print('#{} {}'.format(test_case, real_result))
