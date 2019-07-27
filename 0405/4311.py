import sys

sys.stdin = open('4311.txt')

def check():
    global result
    for i in range(3, M):
        for j in range(M):
            for k in range(M):
                a, b = j, k
                if a < 3:
                    a += 1
                if b < 3:
                    b += 1
                print(a, b, j, k)
                if a+b+1 <= i:
                    for x in Q[j]:
                        for y in Q[k]:
                            for p in oper:
                                if p == 1:
                                    key = int(x)+int(y)
                                    if key < 1000:
                                        if key == W:
                                            result = i
                                            return
                                        if not dp[key]:
                                            dp[key] = i
                                            Q[i].append(str(key))
                                elif p == 2:
                                    key = int(x)-int(y)
                                    if key >= 0:
                                        if key == W:
                                            result = i
                                            return
                                        if not dp[key]:
                                            dp[key] = i
                                            Q[i].append(str(key))
                                elif p == 3:
                                    key = int(x)*int(y)
                                    if key < 1000:
                                        if key == W:
                                            result = i
                                            return
                                        if not dp[key]:
                                            dp[key] = i
                                            Q[i].append(str(key))
                                elif p == 4:
                                    if int(y):
                                        key = int(x)//int(y)
                                        if key == W:
                                            result = i
                                            # print(i, j, k, a, b, x, y, key, W, p)
                                            return
                                        if not dp[key]:
                                            dp[key] = i
                                            Q[i].append(str(key))


T = int(input())

for t in range(1, 2):
    N, O, M = map(int, input().split())

    # 터치 가능한 숫자들의 개수 N 터치 가능한 연산자들의 개수 O, 최대 가능 M
    numbers = (list(input().split()))

    oper = (list(map(int, input().split())))

    # 1 = + 2 = - 3 = * 4 = /

    W = int(input())
    dp = [0]*1000

    Q = [[] for _ in range(M)]

    result = -1

    for i in numbers:
        dp[int(i)] = 1
        Q[0].append(i)
        if int(i) == W:
            result = 1
            break
    if result < 0:
        for i in numbers:
            for j in numbers:
                key = int(i+j)
                if not dp[key]:
                    dp[key] = 2
                    Q[1].append(str(key))
                    if key == W:
                        result = 2
                        break
    if result < 0:
        for i in numbers:
            for j in numbers:
                for k in numbers:
                    key = int(i + j+k)
                    if not dp[key]:
                        dp[key] = 3
                        Q[2].append(str(key))
                        if key == W:
                            result = 3
                            break

    # print(Q)
    if result > 0:
        pass
    else:
        check()
        # 연산자가 존재할때 W가 나올 경우가 있는 지 확인.
        if result == -1:
            pass
        else:
            result += 1
    print('#', end='')
    print(t, end=' ')

    print(result)

    # 1 = + 2 = - 3 = * 4 = /





