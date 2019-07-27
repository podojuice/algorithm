import sys

sys.stdin = open('5203.txt')


T = int(input())

for t in range(1, T+1):
    a_set = [0] * 10
    b_set = [0] * 10

    X = list(map(int, input().split()))

    ans = 0

    for i in range(1, len(X)+1):
        if i % 2:
            a_set[X[i-1]] += 1
            for j in range(10):
                if a_set[j] == 3:
                    ans = 1
                    break
            for j in range(8):
                if a_set[j] and a_set[j+1] and a_set[j+2]:
                    ans = 1
                    break
            if ans:
                break
        else:
            b_set[X[i-1]] += 1
            for j in range(10):
                if b_set[j] == 3:
                    ans = 1
                    break
            for j in range(8):
                if b_set[j] and b_set[j+1] and b_set[j+2]:
                    ans = 2
                    break
            if ans:
                break
    print('#{} {}'.format(t, ans))
