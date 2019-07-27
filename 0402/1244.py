import sys

sys.stdin = open('1244.txt')

#
def check(n, k):
    global max_num, cnt, m
    if m:
        return
    if n == k:
        cnt = n
        result = 0
        for j in range(l):
            result += num_list[-1-j]*(10**j)
        max_num = max(max_num, result)
        return
    for j in range(l - 1):
        if num_list[j] < num_list[j + 1]:
            break
    else:
        m = True
        cnt = n
        result = 0
        for j in range(l):
            result += num_list[-1 - j] * (10 ** j)
        max_num = max(max_num, result)
        return
    for j in range(len(num)-1):
        for p in range(j+1, len(num)):
            num_list[j], num_list[p] = num_list[p], num_list[j]
            if num_list[0] == key:
                check(n+1, k)
            if m:
                return
            num_list[j], num_list[p] = num_list[p], num_list[j]


T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    #전처리
    num = str(N)
    l = len(num)
    num_list = []
    du = [0]*10
    for i in num:
        du[int(i)] += 1
        num_list.append(int(i))
    key = max(num_list)
    cnt = 0
    m = False
    max_num = N



    check(0, K)



    # 후처리
    if cnt < K:
        for i in range(len(du)):
            if du[i] >= 2:
                print('#{} {}'.format(t, max_num))
                break
        else:
            if (K-cnt)%2:
                max_num = str(max_num)
                max_num = max_num[:-2] + max_num[-1] + max_num[-2]
                print('#{} {}'.format(t, max_num))
                break
            else:
                print('#{} {}'.format(t, max_num))
    else:
        print('#{} {}'.format(t, max_num))
