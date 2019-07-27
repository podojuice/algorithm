import sys

sys.stdin = open('5208.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N = list(map(int, input().split()))
    result, cnt = N[1], 0
    stop = 1
    while result < N[0] - 1:
        max_num = 1
        if stop + N[stop] >= N[0]:
            break
        for i in range(N[stop]):
            a = N[stop + 1 + i] + i
            if a >= max_num:
                max_num = N[stop + 1 + i]+i
                b = i + 1
                c = i
        stop += b
        result += max_num - c-c
        cnt += 1
    # if result == N[0]-1:
    #     cnt +=1

    print('#{} {}'.format(test_case, cnt))
